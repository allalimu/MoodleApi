import json,os,re;
import pandas as pd;
from datetime import datetime;
##############################
from dotenv import load_dotenv;
def getData():
    load_dotenv();
    MY_ENV_PROJECTDIR = os.getenv('project_directory');
    with open(MY_ENV_PROJECTDIR + "/ApiCallsResults/Users.json") as json_file:
        data = json.load(json_file);
    return data;

def groupByYear(data):
    PerYear={};

    #Categorize to per year group, and never accessed Groups
    for user in data["users"]:

        if user["lastaccess"]==0:
            year=0;
        else:
            dt_object = datetime.fromtimestamp(user["lastaccess"]);
            year=dt_object.year;

        if str(year) in PerYear:
            PerYear[str(year)].append({"id":user["id"],"email":user["email"]});
        else:
            PerYear[str(year)]=[];
            PerYear[str(year)].append({"id":user["id"],"email":user["email"]});
    return PerYear;

def getStudentsCount(email_list):
    sum=0;
    for user in email_list:
        regex_result=re.search("\d+@limu",user["email"])
        if regex_result:
            sum=sum+1;
    return sum;

def getOthersCount(count,student_count):
    return count-student_count;

def getOldUsersReport():
    
    data=getData();
    PerYear=groupByYear(data);

    statistics={};
    
    for key,value in PerYear.items():
        statistics[key]={
            # Get Count Per Year
            "count": (count:=len(value)),
            # Get Students' Count Per Year
            "Students": (student_count:=getStudentsCount(value)),
            "others": (others:=getOthersCount(count,student_count))
        };

    # print(pd.DataFrame(statistics));

    return statistics;