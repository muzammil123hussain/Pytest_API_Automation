
# for DEMO ENV
DEMO_USER = 'admin123'
DEMO_PASSWORD = 'admin12345678'
DEMO_HOST = 'aasbef5029j8kk.c8rvvgsozn2b.us-west-2.rds.amazonaws.com' 
DEMO_DATABASE = 'ebdb'
BASE_URI_DEMO = 'http://demo.thor.smartbenefits.pk/'
DEMO_AUTHENTICATION_TOKEN = 'Token 702f1315af0b916072ff2b7c641de8807df290fd'
DEMO_AGENT = 111



# for LOCAL ENV
LOCAL_USER = 'muzammil'
LOCAL_PASSWORD = 'muzammil123'
LOCAL_HOST = 'localhost' 
LOCAL_DATABASE = 'thor'
BASE_URI_LOCAL = "http://127.0.0.1:8000"
LOCAL_AUTHENTICATION_TOKEN = 'Token e10ce454df01f777683125ba3177b321ec021ad4'
LOCAL_AGENT = 17

BASE_URI = BASE_URI_DEMO
AUTHENTICATION_TOKEN = DEMO_AUTHENTICATION_TOKEN
AGENT = DEMO_AGENT
USER = DEMO_USER
PASSWORD = DEMO_PASSWORD
HOST = DEMO_HOST
DATABASE = DEMO_DATABASE



CONTENT_TYPE = 'application/json'
headers = {
    'Authorization': AUTHENTICATION_TOKEN,
    'Content-Type': CONTENT_TYPE
}
