
from bs4 import BeautifulSoup
import textwrap

soup = BeautifulSoup(open("/home/shani/RnD/Adding-a-New-API-Store-Theme_97563622.html"), "html.parser")

for divInfo1 in soup.find_all("span", {'class':'aui-icon aui-icon-small aui-iconfont-approve confluence-information-macro-icon'}): 
	divInfo1.unwrap()

for divInfo2 in soup.find_all("span", {'class':'aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon'}): 
	divInfo2.unwrap()

for divInfo2 in soup.find_all("span", {'class':'aui-icon aui-icon-small aui-iconfont-error confluence-information-macro-icon'}): 
	divInfo2.unwrap()

for divNote2 in soup.find_all("span", {'class':'aui-icon aui-icon-small aui-iconfont-warning confluence-information-macro-icon'}): 
	divNote2.unwrap()

for divBody in soup.find_all("div", {'class':'confluence-information-macro-body'}):
        divBody.unwrap()

for divTip0 in soup.find_all("div", {'class':'confluence-information-macro-tip'}):
        divTip0.insert_before('!!! tip')
        divTip0.insert_after("TEST")
        divTip0.unwrap()

for divInfo in soup.find_all("div", {'class':' confluence-information-macro-information'}): 
        divInfo.insert_before('!!! info')
        divInfo.insert_after("TEST")
        divInfo.unwrap()

for divWarning in soup.find_all("div", {'class':'confluence-information-macro-warning'}): 
        divWarning.insert_before('!!! warning')
        divWarning.insert_after("TEST")
        divWarning.unwrap()


for divNote in soup.find_all("div", {'class':'confluence-information-macro-note'}): 
        divNote.insert_before('!!! note')
        divNote.insert_after("TEST")
        divNote.unwrap()

html =soup.contents
html = soup.prettify("utf-8")

with open("converted.html", "wb") as file:
    file.write(html)
    file.close()

print ('Hello, world!')


