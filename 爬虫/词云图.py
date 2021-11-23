import numpy as np
from wordcloud import WordCloud, ImageColorGenerator  # , STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import jieba  # cutting Chinese sentences into words
from collections import Counter  # 词频统计

if __name__ == '__main__':
    # 设置所需文件路径
    al = 'work/阿里云百度百科.txt'
    tx = 'work/腾讯云百度百科.txt'
    hw = 'work/华为云百度百科.txt'
    aly = 'data/aly.png'
    txy = 'data/txy.png'
    hwy = 'data/hwy.png'
    fname_text = tx    # 待解析文本
    fname_stop = 'data/cn_stopwords.txt'  # 停用词文本（非必须）
    fname_mask = txy    # 预备生成的图案图片
    fname_font = 'data/simhei.ttf'      # 词云中所使用的字体
    fname_reserve = 'data/reserve.txt'  # 保留指定词不被分隔

    # 读取需要分词的文本内容
    text = open(fname_text, encoding='utf8').read()
    # 读取停用词文本内容
    STOPWORDS_CH = open(fname_stop, encoding='utf8').read().split()

    # 对文本进行分词处理并剔除停用词
    jieba.load_userdict(fname_reserve)
    wordlist = jieba.cut(text, cut_all=False)  # 精确模式
    # wordlist = jieba.cut_for_search(text) # 搜索引擎模式
    toplist = list()
    for i in wordlist:
        if (i not in STOPWORDS_CH) & (i != '\n'):
            toplist.append(i)

    # 提取出现频率最高的100个关键词
    top = Counter(toplist).most_common(100)
    toplist = list()
    for i in top:
        toplist.append(i[0])
    # print(toplist)

    # 读取图片数组
    im_mask = np.array(Image.open(fname_mask))

    # 绘制词云
    wcd = WordCloud(width=800,
                    height=1200,
                    scale=15,
                    font_path=fname_font,  # 指定字体路径
                    background_color='white',  # 指定背景颜色
                    mode="RGBA",  # 指定图片模式
                    mask=im_mask,  # 指定mask图片
                    )
    # 根据词频生成词云
    wcd.generate_from_frequencies(dict(top))
    # wcd.generate(text)

    # 直接提取原图颜色进行着色
    im_colors = ImageColorGenerator(im_mask)
    wcd.recolor(color_func=im_colors)

    plt.axis('off')  # 关闭坐标轴
    plt.imshow(wcd)  # 图片可视化

    # 保存词云图片
    wcd.to_file('work/txy.png')
