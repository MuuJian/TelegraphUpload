#!usr/bin/python3

from telegraph import Telegraph
import requests
import os
from config import FileName
from config import AuthorLink
from config import AuthorName
from config import ShortName

telegraph = Telegraph()

telegraph.create_account(short_name = ShortName, author_name = AuthorName, author_url = AuthorLink)

path = list()

dir_list = os.listdir('file')
file = list()
for cur_file in dir_list:
    # 获取文件的绝对路径
    filepath = os.path.join('file', cur_file)
    if os.path.isfile(filepath): # 判断是否是文件还是目录需要用绝对路径
        file.append(filepath)
file.sort()

def upload():
    for it in file:
        with open(it, 'rb') as f:
            print(it)
            path.append(requests.post(
                            'https://telegra.ph/upload', files={'file': 
                                                                ('file', f, 
                                                                'image/jpeg')}).json()[0]['src'])
            
                    

upload()
html = "<img src='{}'>" * len(file)

response = telegraph.create_page(
    title = FileName,
    author_name = AuthorName,
    author_url = AuthorLink,
    html_content = html.format(*path),
)


print('https://telegra.ph/{}'.format(response['path']))