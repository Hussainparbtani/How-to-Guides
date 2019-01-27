Business Problem Overview:

In any Business Integlligence Organization, analysts tend to create new processes every so often. These processes, especially ETL processes, requires you to download files. Depending on the frequency of the process and the size of the files, this might take a toll on the memory of your server, or wherever it is that you're storing these files. This guides attempts to solve this problem with an automted solution.


Languages Used:

Python
SQL


Sequence of Steps:

Step 1: Script to Create Backend SQL Tables
Step 2: Python Script to Automatically Remove Files


Final Notes:

In this process we read from SQL tables to figure out which directories we want to delete. This can easily be done from an csv or excel file. Deleting files can often be scary so putting more logic to ensure you don't remove anything important is highly recommended. I'm also keeping a log of what i delete but that is also not necessary depending on the needs of your business. 
