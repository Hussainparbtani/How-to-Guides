--This table will be used to figure out what path we want to delete from and a dynamic field that will help us set criteria for how old the files 
--have to be. Also, includes a active/inactive indicator incase we want an easy way to filter on that. 
CREATE TABLE File_Cleanup_List(
    ID int IDENTITY(1,1) PRIMARY KEY,
    Process_Name varchar(max) NOT NULL,
    Process_Path varchar(max),
	Retention_Period_Days int, 
	Active int,
);


-- This table will be used to log what files were deleted and when. 
CREATE TABLE File_Cleanup_Log(
    ID int IDENTITY(1,1) PRIMARY KEY,
    Process_Name varchar(max) NOT NULL,
    File_Name varchar(max),
	Deleted_Date Date, 
);
