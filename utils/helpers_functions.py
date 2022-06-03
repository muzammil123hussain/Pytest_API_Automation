import config
import requests
from utils.db_connection import database_connection

def generate_random_cnic_no():
    from random import randint
    number = randint(1000000000000, 9999999999999)
    return str(number)

def generate_random_plan_id():
    from random import randint
    number = randint(1000, 9999)
    return str(number)

def generate_random_phone_no():
    from random import randint
    number = randint(1000000, 9999999)
    return str(number)

def get_otp_from_db():

    connection =  database_connection()
    cursor = connection.cursor()

    #qurey to get latest otp from database
    sql = '''SELECT otp from smartbenefits_otp_token order by 1 desc'''

    cursor.execute(sql)
    result = cursor.fetchone();
    otp = str(result).strip("('',)")
    connection.close()
    return otp

def truncate_otp_table():
    connection =  database_connection()
    cursor = connection.cursor()
    #qurey to truncate otp table from database
    sql = '''delete from smartbenefits_otp_token'''
    cursor.execute(sql)
    connection.close()
    return True

def get_by_uuid(unique_id):
    url = f'{config.BASE_URI}/sb/api/corporates/'
    headers = {
        'Authorization': config.LOCAL_AUTHENTICATION_TOKEN,
        'Content-Type': config.CONTENT_TYPE
    }
    response = requests.get(url, headers=headers)
    response_json = response.json()

    user = [result for result in response_json['results'] if result['domain_name'] == unique_id]
    return user