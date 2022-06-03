
from json import dumps
import pytest
from utils import helpers_functions
from uuid import uuid4
import config

pytest.phone_no = None
pytest.password = 'secret11'

def create_employee_payload():
    cnic = helpers_functions.generate_random_cnic_no()
    create_employee_payload = dumps({
            "first_name": "Demo",
            "last_name": "Employee",
            "cnic": cnic,
            "gender": "M",
            "date_of_birth": "2000-02-03",
            "corporate": pytest.corp_id,
            "is_hr": False,
            "products": [
                {
                "product": 2,
                "plan_id": pytest.health_plan_id
                }
            ],
            "dependents": [
                {
                "first_name": "Dependent",
                "last_name": "11",
                "cnic": "",
                "gender": "M",
                "date_of_birth": "2012-02-03",
                "relation": 1
                }
            ]
        })
    return create_employee_payload

def update_employee_payload():

    update_employee_payload = dumps({
            "email": "demo@example.com",
            "date_of_birth": "1999-02-03",
            "bank_name": "MCB",
            "iban": "AD1400080001001234567890"
        })
    return update_employee_payload

def create_bulk_employee_payload():
    cnic = helpers_functions.generate_random_cnic_no()
    cnic_two = helpers_functions.generate_random_cnic_no()
    create_bulk_employee_payload = dumps([
    {
        "first_name": "Demo",
        "last_name": "Employee",
        "cnic": cnic,
        "gender": "M",
        "date_of_birth": "2000-02-03",
        "corporate": pytest.corp_id,
        "is_hr": True,
        "phone1": "232",
        "dependents": [
        {
            "first_name": "Demo",
            "last_name": "Wife",
            "cnic": "",
            "gender": "F",
            "date_of_birth": "2001-02-03",
            "relation": 1
        }
        ],
        "products": [
        {
            "product": 3,
            "plan_id": pytest.life_plan_id
        }
        ]
    },
    {
        "first_name": "Demo",
        "last_name": "Employee",
        "cnic": cnic_two,
        "gender": "M",
        "date_of_birth": "2000-02-03",
        "corporate": pytest.corp_id,
        "is_hr": True,
        "phone1": "232",
        "dependents": [
        {
            "first_name": "Demo",
            "last_name": "Son",
            "cnic": "",
            "gender": "M",
            "date_of_birth": "2012-02-03",
            "relation": 1
        },
        {
            "first_name": "Demo",
            "last_name": "Mother",
            "cnic": "",
            "gender": "F",
            "date_of_birth": "1993-02-03",
            "relation": 1
        }
        ],
        "products": [
        {
            "product": 2,
            "plan_id": pytest.health_plan_id
        },
        {
            "product": 3,
            "plan_id": pytest.life_plan_id
        }
        ]
    }
    ])
    return create_bulk_employee_payload

def create_corporate_payload():
    name = f'DEMO-{str(uuid4())}'
    create_corporate = dumps({
        "name": name,
        "domain_name": name,
        "bussiness_type": 1,
        "account_manager": config.AGENT,
        "params": {
            "key": "some value"
        }
    })
    return create_corporate

def create_bulk_corporate_payload():
    name = f'DEMO-{str(uuid4())}'
    name_two = f'DEMO-{str(uuid4())}'
    create_bulk_corporate_payload = dumps([
    {
        "name": name,
        "domain_name": name,
    },
    {
        "name": name_two,
        "domain_name": name_two,
        "account_manager": config.AGENT,
    }
    ])
    return create_bulk_corporate_payload

def create_health_plan_payload():
    plan_id = helpers_functions.generate_random_plan_id()
    create_health_plan = dumps(
    {
        "name": f'HEALTH-Plan-{plan_id}',
        "category": "A",
        "product_id": 2,
        "insurer_id": 1,
        "hospitalization_limit": 200,
        "daily_room_limit": 0,
        "before_after_hospitalization_days": 0,
        "medical_emergencies": "Covered",
        "medical_emergencies_amount": 34,
        "accidental_emergencies": "Not Covered",
        "accidental_limit_enhancement": None,
        "pre_existing_conditions": 3,
        "congenital_disease_coverage": 0,
        "with_maternity": True,
        "normal_maternity_limit": 2,
        "complicated_maternity_limit": 3,
        "miscarriage_legal_abortion": 4,
        "maternity_pre_existing": "Covered",
        "maternity_pre_existing_note": "test"
    })
    return create_health_plan

def update_health_plan_payload():
    update_health_plan = dumps({
        "hospitalization_limit": 200,
        "daily_room_limit": 1000
    })
    return update_health_plan

def create_life_plan_payload():
    plan_id = helpers_functions.generate_random_plan_id()
    create_life_plan = dumps(
    {
        "name": f'LIFE-Plan-{plan_id}',
        "category": "A",
        "product_id": 3,
        "insurer_id": 1,
        "death_amount": 100,
        "accidental_death_amount": 100,
        "accidental_disability_amount": 100,
        "permanent_accidental_disability_amount": 100,
        "partial_accidental_disability_amount": 100,
        "temporary_accidental_disability_amount": 100
    })
    return create_life_plan

def update_life_plan_payload():
    update_life_plan = dumps({
    "accidental_death_amount": 1000
})
    return update_life_plan

def add_health_plan_in_corporate_payload():

    add_health_plan_in_corporate = dumps({
        "corporate": pytest.corp_id,
        "product": 2,
        "plan_id": pytest.health_plan_id,
        "policy_start": "2021-10-01",
        "policy_end": "2022-10-01",
        "policy_number": "HEALTH-PLAN-DEMO"
    })
    return add_health_plan_in_corporate

def add_life_plan_in_corporate_payload():
    add_life_plan_in_corporate = dumps({
        "corporate": pytest.corp_id,
        "product": 3,
        "plan_id": pytest.life_plan_id,
        "policy_start": "2021-10-01",
        "policy_end": "2022-10-01",
        "policy_number": "LIFE-PLAN-DEMO"
    })
    return add_life_plan_in_corporate

def create_insurer_poc_payload():
    insurer_poc = dumps({
    "product": 2,
    "insurer": 1,
    "claims_poc_emails": "abc@gmail.com,xyz@gmail.com",
    "fluctuation_poc_emails": "abc@gmail.com,xyz@gmail.com",
    "mailing_address_physical_documents": "abc@gmail.com,xyz@gmail.com"
    })
    return insurer_poc

def update_insurer_poc_payload():
    insurer_poc = dumps({
    "claims_poc_emails": "xyz@gmail.com,abc@gmail.com",
    "fluctuation_poc_emails": "xyz@gmail.com,abc@gmail.com",
    "mailing_address_physical_documents": "xyz@gmail.com,abc@gmail.com"
    })
    return insurer_poc

def register_step_one_payload():
    register_step_one = dumps({
        "corporate_code": pytest.corp_code,
        "cnic": pytest.emp_cnic
    })
    return register_step_one

def register_step_two_payload():
    helpers_functions.truncate_otp_table()
    pytest.phone_no = f'0300{helpers_functions.generate_random_phone_no()}'
    register_step_two = dumps({
        "corporate_code": pytest.corp_code,
        "cnic": pytest.emp_cnic,
        "phone": pytest.phone_no,
        "password": pytest.password
    })
    return register_step_two

def verify_otp_payload():
    otp = helpers_functions.get_otp_from_db()
    verify_otp = dumps({
        "phone": pytest.phone_no,
        "otp": otp
    })
    return verify_otp

def login_payload():
    login = dumps({
        "username": pytest.phone_no,
        "password": pytest.password
    })
    return login

def generate_otp_payload():
    generate_otp = dumps({
        "phone": pytest.phone_no
    })
    return generate_otp

def reset_password_payload():
    otp = helpers_functions.get_otp_from_db()
    pytest.password = "secret22"
    reset_password = dumps({
        "phone": pytest.phone_no,
        "otp": otp,
        "password": pytest.password
    })
    return reset_password

def update_profile():
    update_profile = dumps({
        "bank_name": "MCB",
        "iban": "AD1400080001001234567116"
    })
    return update_profile
