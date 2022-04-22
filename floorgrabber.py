from win10toast import ToastNotifier
from selenium import webdriver

d = webdriver.Firefox(executable_path=r"c:\webdriver\geckodriver.exe")
url = input("url =")
TrashHold = input('Floor TrashHold =')
xpath_name = "/html/body/div[1]/div/main/div/div/div[1]/div[2]/div[3]/h1"
xpath_floor = "/html/body/div[1]/div/main/div/div/div[1]/div[2]/div[5]/div/div[3]/a/div/div[1]/div/span/div"

while True:
    d.get(url)
    floor = float(d.find_element_by_xpath(xpath_floor).text)
    pname = str(d.find_element_by_xpath(xpath_name).text)
    print(floor)
    if floor >= float(TrashHold):
        ToastNotifier().show_toast(f"Alert, Floor is {floor}", f"{pname}")
    d.implicitly_wait(5)