import subprocess; import sys; sys.path.append(".");
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

from MoodleApi import MoodleApi;
import json;
import os; from dotenv import load_dotenv;
from pathlib import Path;
load_dotenv();
MY_ENV_URL = os.getenv('URL');
MY_ENV_USERNAME = os.getenv('username');
MY_ENV_PASSWORD = os.getenv('password');

mapi= MoodleApi(MY_ENV_URL,MY_ENV_USERNAME,MY_ENV_PASSWORD);
mapi.login();

#json_result=mapi.GetCategories();
json_result=mapi.GetCoursesBy("category",2);
Path("ApiCallsResults/Categories/2").mkdir(parents=True, exist_ok=True);
f = open("ApiCallsResults/Categories/2/courses.json", "w");
f.write(json.dumps(json_result));
f.close();