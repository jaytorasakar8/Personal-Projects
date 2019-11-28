# Amazon product price tracker using Python

# importing libraries
import bs4 as bs
import sys
import schedule
import time
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

import winsound

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()


def exact_url(url):
    print("Checking url....")
    index = url.find("B0")
    index = index + 10
    current_url = ""
    current_url = url[:index]
    print("URL Returned : ", current_url)
    return current_url


def mainprogram():
    url = "https://www.amazon.com/Lambs-Ivy-578043S-Snoopy-Plush/dp/B018FIQLME/ref=sr_1_2?keywords=snoopy+dog&qid=1574916068&sr=8-2"
    exacturl = exact_url(url)  # main url to extract data
    page = Page(exacturl)
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    js_test = soup.find('span', id='priceblock_ourprice')
    if js_test is None:
        js_test = soup.find('span', id='priceblock_dealprice')
    str = ""
    for line in js_test.stripped_strings:
        str = line

    # convert to integer
    print("Price is: ", str)
    str = str.replace("$", "")
    current_price = int(float(str))
    your_price = 600
    if current_price < your_price:
        print("Price decreased book now")
        #winsound.Beep(frequency, duration)
    else:
        print("Price is high please wait for the best deal")


def job():
    print("Tracking....")
    mainprogram()


# main code
print("Starting tracking")
schedule.every(60).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
