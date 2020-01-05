from urllib.request import urlopen as uReq
from bs4 import  BeautifulSoup as soup
my_url = 'https://www.sastodeal.com/sastodeal/cta-mobiles-28?flag='


print(1)
# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# # html parsing
# page_soup = soup(page_html, "html.parser")

# # grabs each product
# # containers = page_soup.find_all("div",{"class":"c1_t2i"})
# containers = page_soup.find_all("div",{"class":['sku', '-gallery']})
# len(containers)

