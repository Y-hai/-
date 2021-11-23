from lxml import etree
import requests
from urllib.parse import urljoin


def baidu_W(text, name):
    html = etree.HTML(text)
    title = html.xpath('/html/body/div[3]/div[2]/div/div[1]//div/text()')
    s = ''
    for i in title:
        s = s+str(i)
    with open(name, "w", encoding='UTF-8-SIG') as f:
        f.write(s)


def getHTMLText(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
        r = requests.get(url, headers=headers)
        r.raise_for_status()  # 如果状态不是200，则引发异常
        r.encoding = r.apparent_encoding  # 设置编码
        return r.text
    except:
        return r.status_code


url_al = r"https://baike.baidu.com/item/%E9%98%BF%E9%87%8C%E4%BA%91/297128?fr=aladdin"
url_tx = r"https://baike.baidu.com/item/%E8%85%BE%E8%AE%AF%E4%BA%91"
url_hw = r"https://baike.baidu.com/item/%E5%8D%8E%E4%B8%BA%E4%BA%91/4572949?fr=aladdin"

# 百度百科爬取
baidu_W(getHTMLText(url_al), "./work/阿里云百度百科.txt")
baidu_W(getHTMLText(url_tx), "./work/腾讯云百度百科.txt")
baidu_W(getHTMLText(url_hw), "./work/华为云百度百科.txt")
