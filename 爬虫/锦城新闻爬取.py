from lxml import etree
import requests
import csv
from urllib.parse import urljoin


def getHTMLText(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
        }
        r = requests.get(url, headers=headers)  # 请求超时时间为30秒
        r.raise_for_status()  # 如果状态不是200，则引发异常
        r.encoding = r.apparent_encoding  # 配置编码
        return r.text
    except:
        return r.status_code


for i in range(162, 0, -1):
    if i == 162:
        url = "http://www.scujcc.edu.cn/zhxw/zhxw.htm"
    else:
        url = "http://www.scujcc.edu.cn/zhxw/zhxw/" + str(i) + ".htm"
    text = getHTMLText(url)
    html = etree.HTML(text)
    # html树状目录结构
    title = html.xpath(
        '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/ul//a/@title')
    href = html.xpath(
        '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/ul//a/@href')
    hreflist = []
    for url in href:
        full_url = urljoin("http://www.scujcc.edu.cn/", url)
        hreflist.append(full_url)
    # / html / body / div[3] / div / div[2] / div[2] / div[1] / div / ul
    time = html.xpath(
        '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/ul//div[@class="time"]/text()')
    with open("work/2.csv", "a", newline='', encoding='UTF-8-SIG')as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(title)):
            print("正在写入", title[i])
            writer.writerow([title[i], hreflist[i], time[i]])
