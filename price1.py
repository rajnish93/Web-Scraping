import requests
from bs4 import BeautifulSoup
_author_ = 'Rajnish singh'
request = requests.get("https://www.flipkart.com/mobiles/~cs-6sluk2u18k/pr?sid=tyy%2C4io&collection-tab-name=OPPO+Reno+10X+Zoom&sort=price_asc&param=4567&otracker=clp_banner_1_9.bannerX3.BANNER_big-saving-days-mobiles-939ws-929q9sj-store_WL9R6SO84SCA&fm=neo%2Fmerchandising&iid=M_4fe78bb7-d492-4f33-a16d-9eb0e37b01a0_9.WL9R6SO84SCA&ppt=clp&ppn=big-saving-days-mobiles-939ws-929q9sj-store&ssid=m62szo9wlkscuxa81600523749667")
content = request.content
soup = BeautifulSoup(content, "html.parser")
'''
Gives all information about all products on a page
'''
# for x, y in zip(soup.findAll("div", attrs={"class": "_1-2Iqu row"}),
#                 soup.findAll("div", attrs={"class": "_1vC4OE _2rQ-NK"})):
#     print(x.text, "-", y.text)
'''
All products with their price
'''
for x, y in zip(soup.findAll("div", attrs={"class": "_3wU53n"}),
                soup.findAll("div", attrs={"class": "_1vC4OE _2rQ-NK"})):
    print(x.text, "-", y.text)