
from config import *
import requests
import json
import hashlib
import sys, time
from speak import speak
session = requests.Session()
session.headers = headers


def generateOTP():
    for i in range(0,4):
        data = {"secret":"U2FsdGVkX1+z/4Nr9nta+2DrVJSv7KS6VoQUSQ1ZXYDx/CJUkWxFYG6P3iM/VW+6jLQ9RDQVzp/RcZ8kbT41xw==","mobile": REGISTERED_MOBILE_NUMBER}
        resp = session.post('https://cdn-api.co-vin.in/api/v2/auth/generateMobileOTP', data=json.dumps(data))
        if resp.status_code == 200:
            print("OTP SENT SUCCESSFULLY")
            out_json = resp.json()
            print(f"Transaction ID: {out_json['txnId']}")
            break
            
            
        elif resp.status_code == 429:
            print("excceding limit trying after 5 secon")
            time.sleep(5)
        
        else:
            print(f"Generate otp Status code: {resp.status_code}\n{resp.text}")
            return False
    return out_json

def validateOTP(txnId=None):
    for i in range(0,4):
        speak("Enter OTP")
        speak("Recived On you Phone Number")
        data = input("Enter You OTP\n")
        otp = data
        pin = hashlib.sha256(bytes(otp, 'utf-8')).hexdigest()
        validate = {}
        validate["otp"] = pin
        validate["txnId"] = txnId  
        resp = session.post('https://cdn-api.co-vin.in/api/v2/auth/validateMobileOtp', data=json.dumps(validate))
        
        if resp.status_code == 200:
            print("OTP SUCCESSFULLY VERIFIED")
            # out_json = resp.json()
            break
            
        
        
        elif resp.status_code == 429:
            speak("otp limit exceeded")
            speak("trying after 20 seconds")
            print("excceding limit trying after 5 secon")
            time.sleep(20)
            
        
        else:
            speak("Error IN OTP Validation Probalbly you entered wrong otp")
            print(f"Validate otp Status code: {resp.status_code}")
            # sys.exit('Terminated')

    return resp.json()

def get_authenticated_session():
    # session = requests.Session()
    txn = generateOTP()
    if txn != False:
        token_json = validateOTP(txnId=txn['txnId'])
        if token_json != False: 
            speak("login Succesfully")
            token = token_json['token']
            return token
            # print(token)
        else:
            speak("Login fail")
            print("Login Failed")
    else:
        speak("Login fail")
        print("LOGIN Failed")
        
        
if __name__ == '__main__':
    session = get_authenticated_session()