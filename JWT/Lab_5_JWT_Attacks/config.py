# ==========================================
# Configuration File for JWT Exploit
# INSTRUCTIONS: Replace ALL placeholder values below with your own lab details.
# ==========================================

# 1. File Path
PRIVATE_KEY_PATH ="/path/to/your/private_key.pem"

# 2. JWT Custom Header
JKU_URL = "https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/exploit"
KID = "YOUR-GENERATED-KEY-ID"

# 3. URLs
BASE_URL = "https://YOUR-LAB-ID.web-security-academy.net/"
LOGIN_URL = BASE_URL + "login"
ADMIN_URL = BASE_URL + "admin"


# 4. Credentials
Credentials = {
    'csrf' :'/CSRF-VALUE', # Todo: Fetch it dynamically
    'username' :'wiener',
    'password' :'peter'
}