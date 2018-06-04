import urllib.request
from bs4 import BeautifulSoup

html = '''
<html>
<head>
    <title>1111</title>
</head>
<body>
<div id='sidebar'>
    <a class='aa' href='www.baidu.com'>测试1</a>
    <a class='aa' href='www.baidu.com'>测试2</a>
    <a class='aa' href='www.baidu.com'>测试3</a>
    <a class='aa' href='www.baidu.com'>测试4</a>
</div>
<div id='sidebar'>
    <a class='aa' href='www.baidu.com'>开发2</a>
    <a class='aa' href='www.baidu.com'>开发2</a>
    <a class='aa' href='www.baidu.com'>开发2</a>
    <a class='aa' href='www.baidu.com'>开发3</a>
</div>
<div id='sidebar'>
</div>
</body>
'''
soup = BeautifulSoup(html, 'html.parser')
# print(soup.title.string)
# print(soup.find_all(id='sidebar'))
for item in soup.find_all(id='sidebar'):
    for a in item.find_all(name='a'):
        print(a.attrs['href'], a.string)