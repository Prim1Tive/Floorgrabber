from win10toast import ToastNotifier
import argparse
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import *
import warnings

def args_handler():
    parser = argparse.ArgumentParser(prog="FloorGrabber.py", formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description="This project was built so that one may follow a desired floor of an NFT at any moment by giving a Opensea URL")

    parser.add_argument("-u", "--url", help='URL of the OpenSea NFT you want to track', required=True)
    parser.add_argument("-t", "--trash-hold", default='store_false' , help='Floor TrashHold [0.1, 3.4, 5]', required=True)
    parser.add_argument("-s", "--sleep", default='1' , help='how much time to sleep between each request')

    return parser.parse_args()


class FloorGrabber:


    def __init__(self):
        self.args = args_handler()
        self.warnings = warnings
        self.url = self.args.url
        self.set_floor = self.args.trash_hold
        self.sleeptime = int(self.args.sleep)

        # selenium
        self.driver = webdriver.Firefox(executable_path=r"c:\webdriver\geckodriver.exe")
        self.xpath_name = "/html/body/div[1]/div/main/div/div/div/div[3]/div/div/div[1]/div/div[2]/h1"
        self.xpath_floor = "/html/body/div[1]/div/main/div/div/div/div[5]/div/div[2]/div/div[2]/div[3]/div/div[" \
                           "6]/a/div/span[1]/div "

        self.current_floor = None

    def windows_popup_message(self, _floor, _pname):
        return ToastNotifier().show_toast(f"Alert, Floor is {self.current_floor}", f"{self.pname}")

    def get_to_opensea_url(self):
        return self.driver.get(self.url)

    def get_data_from_page(self):
        self.current_floor = self.driver.find_element_by_xpath(self.xpath_floor).text.split('\n')[0]
        self.pname = str(self.driver.find_element_by_xpath(self.xpath_name).text)

    def calculation(self):
        if self.set_floor >= self.current_floor:
            self.get_data_from_page()
            self.driver.implicitly_wait(5)
            self.sleep_time()

    def print_floor(self):
        print("Floor: ", self.current_floor)

    def sleep_time(self):
        return sleep(self.sleeptime)

    def main(self):
        while True:
            self.get_to_opensea_url()
            self.get_data_from_page()
            self.windows_popup_message(self.current_floor, self.pname)
            self.print_floor()
            self.sleep_time()


if __name__ == '__main__':
    FloorGrabber().main()
