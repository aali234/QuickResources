import firebase_admin
from firebase_admin import credentials,auth
import requests
import userRepository 
import os
from dotenv import load_dotenv
import json

current_dir = os.getcwd()
auth_file = os.path.join(current_dir, 'userAuth.json')

load_dotenv()
firebase_api_key = os.getenv("FIREBASE_API_KEY")

cred = credentials.Certificate(auth_file)
firebase_admin.initialize_app(cred)

def register_user(email, password, name, username,dob=""):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        print(f"Successfully registered user with UID: {user.uid}")
        m_user = userRepository.userRepo(user.uid,email,name,username,dob)
        print("created m_user", m_user.get_name())
        return (user,m_user)
    
    except Exception as e:
        print(f"Error: {e}")
        return None

def login_user(email,password):
    url = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={firebase_api_key}'
    headers = {'Content-Type': 'application/json'}

    # Prepare the payload with user credentials
    payload = {
        'email': email,
        'password': password,
        'returnSecureToken': True
    }

    # Make the API request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Parse and print the response
    if response.status_code == 200:
        response_data = response.json()
        user_uid = response_data.get('localId')
        print(f"Successfully authenticated. User UID: {user_uid}")
        return user_uid
    else:
        print(f"Authentication failed. Status code: {response.status_code}")
        print(response.text)
        return None

    
def log_out(uid):
    try:
        auth.revoke_refresh_tokens(uid)
        print(f"Successfully logged out user with UID: {uid}")
    except Exception as e:
        print(f"Error: {e}")
    

if __name__ == '__main__':
    testing = True
    if testing:
        dummy_email = 'testFunc2@test.com'
        dummy_password = '12345678'
        dummy_name = 'test'
        dummy_username = 'tester'
        testfunc2_pass = 'twDl5fsTp0dZJj23BxbZxqpgPYI2'
        #u1 = register_user(dummy_email, dummy_password,dummy_name,dummy_username)
        #m1 = u1[1]
        # login_user(m1.get_email(), '12345678')
        # log_out(m1.get_uid())
        print('logging in ', dummy_email)
        login_user(dummy_email,dummy_password)
        print('logging out')
        log_out(testfunc2_pass)
        print('attempt re log in with wrong password')
        login_user(dummy_email,dummy_password+'1')
