import json
import os
import sys
import requests
import urllib
import json
from Helpers.colors import bcolors

def getResponseMessage(status):
    switcher = [
        "Unknown error"
        f"\n{bcolors.WARNING}the shortened link comes from the domain that shortens the link, i.e. the link has already been shortened\n",
        f"\n{bcolors.WARNING}the entered link is not a link\n",
        "Unknown error",
        f"\n{bcolors.WARNING}Invalid API key\n",
        f"\n{bcolors.WARNING}the link has not passed the validation. Includes invalid characters\n",
        f"\n{bcolors.WARNING}The link provided is from a blocked domain\n",
    ]
    return switcher[status]


def shortenLink(Link, api_key):
    
    print(f"{bcolors.HEADER}\nGenerating short url..\n")

    while True:

        slashtag = input(f"{bcolors.OKCYAN}Enter url's slashtag: ")

        key = api_key
        url = urllib.parse.quote(Link)
        name = slashtag

        try:
            r = requests.get(
                'http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(key, url, name))
        except Exception as e:
            sys.exit(f"\nSomething went wrong with rebrandly api!\n {e}")

        json_response = r.json()['url']
        response_status = json_response['status']
        if response_status == 7:
            print(f"{bcolors.OKGREEN}ACCEPTED!{bcolors.ENDC}")
            break
        elif response_status != 3:
            sys.exit(getResponseMessage(response_status))

        print(
            f"{bcolors.WARNING}Sorry, this slashtag is used!{bcolors.ENDC}")

    print(f"{bcolors.OKYELLOW}\nShorten url successfully generated with the following link:")
    print(f"{bcolors.OKRED}{json_response['shortLink']}")
    return json_response['shortLink']
