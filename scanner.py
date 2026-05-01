import requests
import time
from pyfiglet import Figlet

def SubdomainFinder():
    TargetName = input("Enter the target domain name: ")
    WordlistType = input("For default wordlist type '0' | For custom wordlist type '1': ")
    if WordlistType == "0":
        filename = "defwordlistsub.txt"
        with open(filename, "r") as file:
            for line in file:
                sub = line.strip()
                url = f"http://{sub}.{TargetName}"
                try:
                    response = requests.get(url, timeout=2)
                    print(f"|{url} ---------------- {response.status_code}|")
                except requests.RequestException:
                    print(f"|{url} ---------------- Connection Error|")

    elif WordlistType == "1":
        filename = input("Enter the path to your custom wordlist: ")
        with open(filename, "r") as file:
            for line in file:
                sub = line.strip()
                url = f"http://{sub}.{TargetName}"
                try:
                    response = requests.get(url, timeout=2)
                    print(f"|{url} ---------------- {response.status_code}|")
                except requests.RequestException:
                    print(f"|{url} ---------------- Connection Error|")
#                
##################
##################
##################
##################
#
def DirectoryBruteForce():
    TargetName = input("Enter the target domain name: ")
    WordlistType = input("For default wordlist type '0' | For custom wordlist type '1': ")
    if WordlistType == "0":
        filename = "defwordlistdir.txt"
        with open(filename, "r") as file:
            for line in file:
                sub = line.strip()
                url = f"http://{TargetName}/{sub}"
                try:
                    response = requests.get(url, timeout=2)
                    print(f"|{url} ---------------- {response.status_code}|")
                except requests.RequestException:
                    print(f"|{url} ---------------- Connection Error|")

    elif WordlistType == "1":
        filename = input("Enter the path to your custom wordlist: ")
        with open(filename, "r") as file:
            for line in file:
                sub = line.strip()
                url = f"http://{TargetName}/{sub}"
                try:
                    response = requests.get(url, timeout=2)
                    print(f"|{url} ---------------- {response.status_code}|")
                except requests.RequestException:
                    print(f"|{url} ---------------- Connection Error|")
#################################################################################################################



ScannerType = input("Subdomain finder or directory brute-force? (for subdomains type 1 for directory brute-force type 2): ")
if ScannerType == "1":
    print("Starting subdomain finder...")
    time.sleep(0.5)
    f = Figlet(font='slant')   # you can change font
    print(f.renderText('SUBDOMAIN FINDER'))
    SubdomainFinder()

elif ScannerType == "2":
    print("Starting directory brute-forcer...")
    time.sleep(0.5)
    f = Figlet(font='slant')   # you can change font
    print(f.renderText('DIRECTORY BRUTE-FORCER'))
    DirectoryBruteForce()

else :
    print("Invalid input. Please enter 1 or 2.")



#####################################################################################################################
