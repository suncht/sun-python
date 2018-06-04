import urllib.request
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument('-headless')  # 无头参数
driver = Firefox(executable_path='geckodriver', firefox_options=options)  # 配了环境变量第一个参数就可以省了，不然传绝对路径
wait = WebDriverWait(driver, timeout=10)

url = "https://www.lagou.com/zhaopin/Java/1/?filterOption=1"
driver.get(url)
wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys('headless firefox' + Keys.ENTER)
wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
html = driver.page_source
driver.quit()

# html = urllib.request.urlopen(url).read()
html = html.decode('UTF-8')

"""
从拉勾网中获取java职位的翻页列表
"""
soup = BeautifulSoup(html, 'html.parser')

file = open('d:/a.txt', 'w')
file.write(html)
file.close()

s_position_list = soup.find(name='div', attrs={'id': 's_position_list'})

pages = s_position_list.find(name='div', attrs={'class': 'pager_container'})

max_page_num = 0
for page in pages.find_all(name='a'):
    page_index = page.attrs['data-index']
    if page_index != '':
        max_page_num = max(max_page_num, int(page_index))

print(max_page_num)