import pprint as pp

import re
import string
import requests as req
from distutils.dir_util import copy_tree
from bs4 import BeautifulSoup as bs
# import xml.etree.cElementTree as ET


import tools_.tools as tools
import tools_.bs_tools as bs_tools

#входные данные --------------------------------------------------------
page_adresse = 'https://habr.com/ru/company/leader-id/blog/527492/'

#входные данные end-----------------------------------------------------


pic_folder = './images'
pdf_folder = './pdf'


tools.clean_dir(pic_folder)
tools.clean_dir(pdf_folder)

r = req.get(page_adresse)


# pp.pprint(r.text)
soup = bs(r.text, 'html5lib')

post_title = soup.find('h1').text.strip()
post_body = soup.find('div', class_="post__body_full")



a = 1



















# post_body_ = list(filter(lambda x: str(x).strip(), post_body.contents))

# for child in post_body_[0].children:
#     pp.pprint(str(child) + "\n")

# pp.pprint(f'Найдено {len(all_images)} изображений')


# for pic in all_images:
    
#     resp_img = req.get(pic["src"], stream=True)
#     pic_name = pic["src"].rsplit('/')[-1]

#     a = resp_img.content

#     with open('./images/' + pic_name + '.png', 'wb') as file:
#         file.write(resp_img.content)

#     img_tag = post_body.find('img', src=re.compile(pic_name))

#     # img_tag['src'] = "{% static './images/' + pic_name + '.png' %}"
#     img_tag['src'] = "./images/" + pic_name + ".png"

# pp.pprint(post_body)


