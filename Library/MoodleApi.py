import requests;
import json;
class MoodleApi:
    """Token and other stuff"""
    moodlewsrestformat="json";
    service=None;
    wstoken=None;
    
    def __init__(self,url,username,password,service):
        self.url=url;
        self.username=username;
        self.password=password;
        self.service=service;

######################################################################

    def valuesToMap(self,key,strArr):
        if key in strArr:
            return strArr[key];
        else:
            return "";

    def build_url(self,uri,params):
        url=self.url+uri+"?";
        tmp={key+"="+str(value) for key,value in params.items()};
        params_str='&'.join(tmp);
        url=url+params_str;
        return url;

    def getMap(self,api_to_call,fn):
        api_map={
            "LogIn":{
                "uri":"/login/token.php",
                "params":{
                    "service":self.service,
                    "moodlewsrestformat":self.moodlewsrestformat,
                    "username":self.username,
                    "password":self.password
                }
            },
            "Get_Categories":{
                "uri":"/webservice/rest/server.php",
                "params":{
                    "moodlewsrestformat":self.moodlewsrestformat,
                    "wsfunction":"core_course_get_categories",
                    "wstoken":self.wstoken
                }
            },
            "Get_Courses_by_field":{
                "uri":"/webservice/rest/server.php",
                "params":{
                    "moodlewsrestformat":self.moodlewsrestformat,
                    "wsfunction": "core_course_get_courses_by_field",
                    "field":fn("field"),
                    "wstoken":self.wstoken,
                    "value":fn("value")
                }
            },
            "Get_Users":{
                "uri":"/webservice/rest/server.php",
                "params":{
                    "moodlewsrestformat":self.moodlewsrestformat,
                    "wsfunction": "core_user_get_users",
                    "wstoken":self.wstoken,
                    "criteria[0][key]":"eamil",
                    "criteria[0][value]":"%"
                }
            }
        };

        return api_map[api_to_call];

    def theRequest(self,url,r_type="GET",body=None):
        response=requests.request(method=r_type,url=url,data=body);
        json_response=json.loads(response.text);
        return json_response;
###################################################################
    def GetUsers(self):

        request_map=self.getMap("Get_Users", lambda key: self.valuesToMap(key,{}));
        url=self.build_url(request_map["uri"],request_map["params"]);

        json_response=self.theRequest(url,r_type="POST");

        return json_response;

    def GetCoursesBy(self,field,value):
        request_map=self.getMap("Get_Courses_by_field", lambda key: self.valuesToMap(key,{"field":field,"value":value}));
        url=self.build_url(request_map["uri"],request_map["params"]);

        json_response=self.theRequest(url);

        return json_response;

    def GetCategories(self):
        request_map=self.getMap("Get_Categories", lambda key: self.valuesToMap(key,{}));
        url=self.build_url(request_map["uri"],request_map["params"]);

        json_response=self.theRequest(url);

        return json_response;

    def login(self):
        request_map=self.getMap("LogIn", lambda key: self.valuesToMap(key,{}));
        url=self.build_url(request_map["uri"],request_map["params"]);
        
        json_response=self.theRequest(url);

        if 'token' in json_response:
            self.wstoken=json_response['token'];
        return self.wstoken;