import sys,json,os,time;
# Loading Moodle API Library
from Project.Library.MoodleApi import MoodleApi; 
##############################
from dotenv import load_dotenv;

def getUsersPrivateFilesData():
    load_dotenv();
    MY_ENV_URL = os.getenv('URL');
    MY_ENV_USERNAME = os.getenv('username');
    MY_ENV_PASSWORD = os.getenv('password');
    MY_ENV_SERVICE = os.getenv('service_name');
    MY_ENV_PROJECTDIR = os.getenv('project_directory');
    ########################

    mapi= MoodleApi(MY_ENV_URL,MY_ENV_USERNAME,MY_ENV_PASSWORD,MY_ENV_SERVICE);
    
    mapi.login();
    count=0;
    users=mapi.GetUsers();
    user_files={};

    for user in users["users"]:
    
        json_result=mapi.GetPrivateFilesInfoByUserId(user["id"]);        
        user_files={"id":user["id"],"email":user["email"],"private_files_data":json_result};
        if user["id"]>2339:
            f = open(MY_ENV_PROJECTDIR+"/ApiCallsResults/UsersPrivateFilesData/"+str(user["id"])+".json", "w");
            f.write(json.dumps(user_files));
            f.close();
            
            count=count+1;
            if(count == 50):
                time.sleep(0.1);
                count=0;