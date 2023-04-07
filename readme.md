# OpenSea Floor RealTime Notifications.

This project was built so that one may follow a desired floor of an NFT at any moment by giving the "OpenSea NTF Profile URL."

<p align="center">
<img src="demo.png"/>
</p>


## Requierments:

- Selenium - that is compatible with your Firefox  version
- win10toast - pip install win10toast
- Firefox lastest version
- gekodriver - Install this file in c:\webdrivers\gekodriver.exe
- Currently supports Windows only.

## Installation:

- python3 - https://www.microsoft.com/store/productId/9PJPW5LDXLZ5
- Selenium - open cmd and type pip install selenium OR python -m pip install selenium
- win10toast - open cmd and type pip install win10toast OR python -m pip install win10toast
- ### Download the project And save it somewhere https://github.com/Prim1Tive/Floorgrabber/releases/download/untagged-ea92eb196d54158ab008/floorgrabber.py
- gekodriver - https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-win64.zip | please save the file at c:\webdrivers\gekodriver.exe


## Usage:

```
usage: Opensea NFT FloorGrabber [-h] -u URL -t TRASH_HOLD [-s SLEEP]

This project was built so that one may follow a desired floor of an NFT at any moment by giving a Opensea URL

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL of the OpenSea NFT you want to track
  -t TRASH_HOLD, --trash-hold TRASH_HOLD
                        Floor TrashHold [0.1, 3.4, 5]
  -s SLEEP, --sleep SLEEP
                        how much time to sleep between each request
```
