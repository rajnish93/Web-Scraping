import requests
from bs4 import BeautifulSoup
_author_ = 'Rajnish singh'
request = requests.get("https://www.flipkart.com/mobiles/~cs-6sluk2u18k/pr?sid=tyy%2C4io&collection-tab-name=OPPO+Reno+10X+Zoom&sort=price_asc&param=4567&otracker=clp_banner_1_9.bannerX3.BANNER_big-saving-days-mobiles-939ws-929q9sj-store_WL9R6SO84SCA&fm=neo%2Fmerchandising&iid=M_4fe78bb7-d492-4f33-a16d-9eb0e37b01a0_9.WL9R6SO84SCA&ppt=clp&ppn=big-saving-days-mobiles-939ws-929q9sj-store&ssid=m62szo9wlkscuxa81600523749667")
content = request.content
soup = BeautifulSoup(content, "html.parser")
# <div class="_1vC4OE _2rQ-NK">₹41,990</div>
element = soup.find("div", {"class": "_1vC4OE _2rQ-NK"})
print(element.text)
# print(soup.find_all('a'))
# List all url from the page
# for link in soup.find_all('a'):
#     print(link.get('href'))
# extracting all the text
print(soup.get_text())