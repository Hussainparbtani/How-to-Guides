#importing all the libs needed for this script
import time
import datetime
import os 
import pyodbc
import pandas as pd
import urllib
import sqlalchemy

#defining connection to backend database of backend sql tables.Example is that of a SQL-Server Database
cnxn = pyodbc.connect(
            "DRIVER={SQL Server Native Client 11.0};SERVER=servername;Trusted_Connection=yes;DATABASE=databasename")


#reading from sql table where all the directory path lies
sql = """select process_name, process_path, retention_period_days from file_cleanup_list where active = 1"""

#converting to a dataframe
df = pd.read_sql(sql,cnxn)

#creating empty lists which we will append to later
process_name = []

deleted_files = []

#getting todays date
today = datetime.datetime.today().strftime('%Y-%m-%d')

#looping through list of directories in dataframe
for i in range(len(df)):
    
    #getting path from df
    path = df['process_path'][i]

    
    #getting retention period from df
    retention_period = df['retention_period_days'][i]

    
    #getting process name 
    process_name_actual = df['process_name'][i]

    
    #dynamic date which based on retention period which will be used to determine if file in dir should be deleted
    cut_off_date = datetime.datetime.today() - datetime.timedelta(days=int(retention_period))

    
    #getting a list of files in the directory
    list_of_files = os.listdir(path)

    
    #looping through list of files 
    for i in range(len(list_of_files)):
    
        
        #getting full path of files
        full_path = path+list_of_files[i]

        
        #determinig the time the files were created
        time_of_file = datetime.datetime(*time.gmtime(os.path.getctime(full_path))[:6])

        
        #if file was created before the cut off date 
        if time_of_file < cut_off_date:
            
            #remove file
            os.remove(full_path)
            
            #add file name to deleted files list
            deleted_files.append(list_of_files[i])

            #add process name to process name list                         
            process_name.append(process_name_actual)

    
    else:
        pass

#creating ddata frame based on the files that were deleted            
file_cleanup_log = pd.DataFrame({'File_Name':deleted_files,'Process_Name':process_name})

#adding today's date to dataframe
file_cleanup_log['Deleted_Date'] = today

#defining database connection again(different because using different lib to upload then to read the first sql table)
Database = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};SERVER=servername;Trusted_Connection=yes;DATABASE=databasename')
    
#creating Engine
Engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(Database))

#uploading dataframe to log table 
file_cleanup_log.to_sql("File_Cleanup_Log",Engine,if_exists='append',index=False)   