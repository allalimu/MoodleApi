import os,sys;

Packages=["click","requests","json","subprocess","python-dotenv"];

for pack in Packages:
    try:
        __import__(pack);
    except ImportError as e:
        os.system(sys.executable+" -m pip install "+pack);