import requests
import os.path
import time
from bs4 import BeautifulSoup
from plyer.utils import platform
from plyer import notification
from datetime import datetime

appdataPath = os.path.join(os.getenv('APPDATA'), "is-there-upd8")
if not os.path.exists(appdataPath):
    os.makedirs(appdataPath)

filePath = os.path.join(appdataPath, "previous_update.txt")
if not os.path.isfile(filePath):
    open (filePath, "a").close()

while(True):
    request = requests.get("https://beyondcanon.com/story/feed")

    soup = BeautifulSoup(request.text, "xml")
    mostRecentUpdate = soup.find_all("updated")[1].text
    #print(mostRecentUpdate)


    with open (filePath, "r+") as file:
        previousUpdate = file.read()
        file.seek(0)
        file.write(mostRecentUpdate)
    #with open ("previous_update.txt", "w") as file:
        

    print(previousUpdate)
    print(mostRecentUpdate)

    if previousUpdate != mostRecentUpdate:
        mostRecentUpdateTime = datetime.fromisoformat(mostRecentUpdate)
        updateMessage = mostRecentUpdateTime.strftime('Homestuck Beyond Canon has updated!\nMost recent update was on %d/%m/%y, at %H:%M')
        print(updateMessage)


        notification.notify(
            title='Is There An Upd8?',
            message=updateMessage,
            app_name='Is There an Upd8?'
        )
    else: print("no upd8 :(")
    time.sleep(600)