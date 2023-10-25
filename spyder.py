from pprint import pprint
from bs4 import BeautifulSoup
import requests as res, bs4, time, re

my_dict = {}


def get_link(URL):
    my_header = {'cookie': 'over18=1;'}

    response = res.get(URL, headers=my_header)

    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("div", "title", )

    for check in titles:
        my_dict.update({check.text.strip().split("\n")[0]: "https://www.ptt.cc/"+re.search(r'href="([^"]+)"', str(check)).group(1)})

    pprint(my_dict)


start = 3990
end = 3995

for i in range(start, end):
    link = "https://www.ptt.cc/bbs/sex/index" + str(i) + ".html"

    get_link(link)
    time.sleep(1)

print("total :", len(my_dict))