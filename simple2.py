
from bs4 import BeautifulSoup
import textwrap

soup = BeautifulSoup(open("/home/shani/RnD/github_conv/Adding-an-API-State-Change-Workflow_97563610.html"), "html.parser")

for divInfo1 in soup.find_all("span", {'class':'aui-icon aui-icon-small aui-iconfont-approve confluence-information-macro-icon'}): 
	divInfo1.unwrap()

for divInfo2 in soup.find_all("span", {'class':'aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon'}): 
	divInfo2.unwrap()

for divInfo2 in soup.find_all("span", {'class':'aui-icon aui-icon-small aui-iconfont-error confluence-information-macro-icon'}): 
	divInfo2.unwrap()


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

html =soup.contents
html = soup.prettify("utf-8")

with open("converted.html", "wb") as file:
    file.write(html)
    file.close()

print ('Hello, world!')

