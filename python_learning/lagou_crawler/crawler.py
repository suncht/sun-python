import urllib.request
from bs4 import BeautifulSoup

class LagouCrawler(object):
    def __init__(self):
        pass

    def query_job_catagory(self):
        """
        从拉钩网中获取职位大类和职位列表
        :return: [catagory, {job, url}]
        """
        url = "https://www.lagou.com/"
        html = urllib.request.urlopen(url).read()
        html = html.decode('UTF-8')

        soup = BeautifulSoup(html, 'html.parser')

        sidebar = soup.find(name='div', attrs={'id': 'sidebar'})
        category_list = sidebar.find_all(name='div', attrs={'class': 'category-list'})

        # 获取职位大类
        type_job_map = []

        for category in category_list:
            type_job = category.find(name='h2')
            jobs = category.find_all(name='a')

            str_type = type_job.string.strip()
            # 获取职位+url
            job_map = {}

            if str_type != '':
                for job in jobs:
                    job_map[job.string] = job.attrs['href']

            type_job_map.append((str_type, job_map))

        return type_job_map
