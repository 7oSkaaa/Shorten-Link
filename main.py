from Services.link_shorten import shortenLink
from Helpers.colors import colors
from Services.link_shorten import change_directory


def saveToFile(fileName, mode, data, message):
    change_directory()
    with open(f"{fileName}", mode) as file:
        file.write(message + ": " + data + "\n")


def main():

    # Make Shorten Link
    shorten_url_response = shortenLink()

    # Get the shorten url
    shorten_url = shorten_url_response["shortLink"]

    # Get the original url
    original_url = shorten_url_response["fullLink"]

    # title of the link
    title = shorten_url_response["title"]

    # Save the links to the file
    saveToFile("URLs.txt", "w", shorten_url, "Shorten URL")
    saveToFile("URLs.txt", "a", original_url, "Original URL")
    saveToFile("URLs.txt", "a", title, "URL Title")

    # check the URLs.txt
    print(f"\n{colors.brown}Check the URLs.txt file for the shorten url, the original url and URL Title{colors.reset}")


if __name__ == "__main__":
    main()
