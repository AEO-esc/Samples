from logging import exception
from urllib import response
import urllib.request as urllib

class SiteChecker():
    def checkSiteStatus(self, url):
        # set our response up w
        try:
            response = urllib.urlopen(url)
            print("Connected to", url, "successfully")
            print("Response code was:", response.getcode())
        except Exception as e:
            print("Failed to open URL:", e)
        finally:
            print("Program completed.")

def main() -> None:
    mySiteClass = SiteChecker()
    print("Site Checker")
    inputUrl = input("Input the URL of the website you would like to check: ")
    mySiteClass.checkSiteStatus(inputUrl)

if __name__ == "__main__":
    main()