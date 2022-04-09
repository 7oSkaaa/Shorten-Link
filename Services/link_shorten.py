import json
import os
import sys
import requests
from Helpers.colors import bcolors

def getResponseMessage(status):
    switcher = [
        "Unknown error"
        f"\n{bcolors.WARNING}the shortened link comes from the domain that shortens the link, i.e. the link has already been shortened\n{bcolors.ENDC}",
        f"\n{bcolors.WARNING}the entered link is not a link\n{bcolors.ENDC}",
        "Unknown error{bcolors.ENDC}",
        f"\n{bcolors.WARNING}Invalid API key\n{bcolors.ENDC}",
        f"\n{bcolors.WARNING}the link has not passed the validation. Includes invalid characters\n{bcolors.ENDC}",
        f"\n{bcolors.WARNING}The link provided is from a blocked domain\n{bcolors.ENDC}",
    ]
    return switcher[status]


def shortenLink(api_key):
    
    print(f"{bcolors.HEADER}Generating short url...\n{bcolors.ENDC}")

    while True:

        slashtag = input(f"{bcolors.OKCYAN}Enter url's slashtag: {bcolors.ENDC}")

        key = api_key
        url = os.getenv('URL')
        name = slashtag

        try:
            r = requests.get(
                'http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(key, url, name))
        except Exception as e:
            sys.exit(f"\nSomething went wrong with rebrandly api!\n {e}")

        json_response = r.json()['url']
        response_status = json_response['status']
        if response_status == 7:
            print(f"\n{bcolors.OKGREEN}ACCEPTED! ✅{bcolors.ENDC}")
            break
        elif response_status != 3:
            sys.exit(getResponseMessage(response_status))

        print(
            f"{bcolors.WARNING}Sorry, this slashtag is used!{bcolors.ENDC}")

    print(f"{bcolors.OKYELLOW}\nShorten url successfully generated with the following link:\n{bcolors.ENDC}")
    print(f"{bcolors.OKRED}{json_response['shortLink']}{bcolors.ENDC}")
    return json_response['shortLink']
