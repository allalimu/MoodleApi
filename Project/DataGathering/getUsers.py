import sys,json,os;
# Loading Moodle API Library
from Project.Library.MoodleApi import MoodleApi; 
##############################
from dotenv import load_dotenv;

def getUsers():
    load_dotenv();
    MY_ENV_URL = os.getenv('URL');
    MY_ENV_USERNAME = os.getenv('username');
    MY_ENV_PASSWORD = os.getenv('password');
    MY_ENV_SERVICE = os.getenv('service_name');
    MY_ENV_PROJECTDIR = os.getenv('project_directory');
    ########################

    mapi= MoodleApi(MY_ENV_URL,MY_ENV_USERNAME,MY_ENV_PASSWORD,MY_ENV_SERVICE);
    
    mapi.login();
    
    json_result=mapi.GetUsers();

    f = open(MY_ENV_PROJECTDIR+"/ApiCallsResults/Users.json", "w");
    f.write(json.dumps(json_result));
    f.close();