##########################################################################################
################### Todo: Still needs Work ###############################################
##########################################################################################
import sys,json,os;
sys.path.append("/home/alla/MoodleApiProject");

###############################
# Loading Moodle API Library
from Library.MoodleApi import MoodleApi; 
##############################

#########################
# This part still needs enhancing
from dotenv import load_dotenv;
load_dotenv();
MY_ENV_URL = os.getenv('URL');
MY_ENV_USERNAME = os.getenv('username');
MY_ENV_PASSWORD = os.getenv('password');
########################

mapi= MoodleApi(MY_ENV_URL,MY_ENV_USERNAME,MY_ENV_PASSWORD);
mapi.login();

#json_result=mapi.GetCategories();
json_result=mapi.GetCoursesBy("category",2);
os.Path("../ApiCallsResults/Categories/2").mkdir(parents=True, exist_ok=True);
f = open("../ApiCallsResults/Categories/2/courses.json", "w");
f.write(json.dumps(json_result));
f.close();