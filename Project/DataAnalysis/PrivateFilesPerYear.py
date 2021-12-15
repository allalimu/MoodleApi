import json,os,re;
import pandas as pd;
from datetime import datetime;
from Project.DataAnalysis.UsersReport import getData,groupByYear,getOldUsersReport;
##############################
from dotenv import load_dotenv;

def getPFilesData(user_id):
    load_dotenv();
    MY_ENV_PROJECTDIR = os.getenv('project_directory');
    with open(MY_ENV_PROJECTDIR + "/ApiCallsResults/UsersPrivateFilesData/"+str(user_id)+".json") as json_file:
        data = json.load(json_file);
    return data;

def getSummationOfFileSizes(accounts):
    sum=0;
    for account in accounts:
        if "files_size" in account:
            sum=sum+account["files_size"];
    return sum /1024.0/1024.0;

def addFileSizeToData(accounts):
    for account in accounts:
        try:
            file_size=getPFilesData(account["id"]);
            if "filesize" in file_size["private_files_data"]:
                account["files_size"]=file_size["private_files_data"]["filesize"];
        except Exception as error:
            print(account);
    return accounts;

def getPerYearReport():
    PerYear=groupByYear(getData());
    #print(PerYear);
    for key,value in PerYear.items():
        PerYear[key]=addFileSizeToData(value);

    #print(json.dumps(PerYear));
    
    statistics={};
    for key,value in PerYear.items():
        statistics[key]={
            "SizeOfFiles":getSummationOfFileSizes(value)
        };
    print(statistics);