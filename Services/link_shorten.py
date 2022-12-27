import os
import sys

import requests
from dotenv import load_dotenv

from Helpers.colors import colors


def change_directory():
    # Get the directory of current folder
    directory = os.path.dirname(os.path.realpath(__file__))
    os.chdir(directory)


def Load_env():
    # Change the directory and load the environment variables
    change_directory()

    # Load the environment variables
    load_dotenv()


def getResponseMessage(status):
    switcher = [
        "Unknown error"
        f"\n{colors.WARNING}the shortened link comes from the domain that shortens the link, i.e. the link has already been shortened\n{colors.ENDC}",
        f"\n{colors.WARNING}the entered link is not a link\n{colors.ENDC}",
        "Unknown error{colors.ENDC}",
        f"\n{colors.WARNING}Invalid API key\n{colors.ENDC}",
        f"\n{colors.WARNING}the link has not passed the validation. Includes invalid characters\n{colors.ENDC}",
        f"\n{colors.WARNING}The link provided is from a blocked domain\n{colors.ENDC}",
        "Uknown error{colors.ENDC}",
        f"\n{colors.WARNING}You have reached your monthly link limit. You can upgrade your subscription plan to add more links.",
    ]
    return switcher[status]


def shortenLink():

    # Change the directory and load the environment variables
    Load_env()

    # Get API Key of the user
    if "API_KEY" not in os.environ or os.getenv("API_KEY") == '':
        print(f"\n{colors.red}Missing Environemnts Variables\n{colors.reset}")
        exit(0)

    # Get API Key from environment variables
    Api_Key = os.getenv("API_KEY")

    print(f"{colors.magenta}Generating short url...\n{colors.reset}")

    url = input(f"{colors.cyan}Enter url: {colors.reset}")

    while True:

        slashtag = input(f"\n{colors.cyan}Enter url's slashtag: {colors.reset}")

        key = Api_Key
        name = slashtag

        try:
            r = requests.get(
                "http://cutt.ly/api/api.php?key={}&short={}&name={}".format(
                    key, url, name
                )
            )

        except Exception as e:
            sys.exit(f"\nSomething went wrong with Cuttly api!\n {e}")

        json_response = r.json()["url"]
        response_status = json_response["status"]
        if response_status == 7:
            print(f"\n{colors.green}ACCEPTED! ✅{colors.reset}")
            break
        elif response_status != 3:
            sys.exit(getResponseMessage(response_status))

        print(f"{colors.red}Sorry, this slashtag is used!{colors.reset}")

    print(
        f"{colors.gold}\nShorten url successfully generated with the following link:\n{colors.reset}"
    )
    print(f"{colors.blue}{json_response['shortLink']}{colors.reset}")
    return json_response
