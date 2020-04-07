#!/usr/bin/env python3
import requests
def download(url,filename):
    '''
    从指定的url中下载文件并存储到当前目录
    url：要下载页面内容的网址
    '''
#检查url是否存在
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Invalid Url "{}"'.format(url))
        return
#检查是否成功访问了该网站
    if req.status_code == 403:
        print("You do not have the authority to access this page.")
        return
    #filename = str(input("请输入保存文件的名称："))
    with open(filename, 'w') as fobj:
        fobj.write(req.content.decode('utf-8'))
    print("Download over.")

if __name__ == '__main__':
    url = input('Enter a url: ')
    filename = str(input("请输入保存文件的名称："))
    download(url,filename)
