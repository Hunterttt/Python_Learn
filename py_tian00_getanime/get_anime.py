import requests
import re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_link_list(xwords):
    header = {"User-Agent": UserAgent().random}    #伪造head的User-Agent字段，假装是从浏览器发出的请求
    i = 0
    link_list = []

    while True:       
        i += 1
        print('第%d页'%i)
        sourse_html = 'https://share.dmhy.org/topics/list/page/{}?keyword={}'      #根据网站不同链接不同
        sourse_html = sourse_html.format(i, xwords)    #参数ip来代替sourse_html里面的大括号
        response = requests.get(sourse_html, headers = header)     #headers这个参数有些教程里没有
        #print(response.text)
        homepage = BeautifulSoup(response.text, 'lxml')

        homepage1 = homepage.find('div',attrs={'class':'table clear'}).find('tbody')
        
        
        if homepage1 == None:
            link_list.append('第%d页'%i)
            link_list.append('这页没有')
            print('这页没有')
            break
        else:
            list1 = homepage1.find_all('tr')
            link_list.append('第%d页'%i)

            for item in list1:
                # t1 = item.find('a',target = '_blank')
                # title = t1.get_text().strip()
                # print(title)

                
                t2 = item.find('a',attrs={'class':'download-arrow arrow-magnet'})
                p = re.compile('^magnet.*?&dn=')
                str = p.findall(t2['href'])[0]
                print(str[:-4])
                link_list.append(str[:-4])
    return(link_list)

def list_to_txt(xlist):
    temp_file = open('Link.txt','w')
    for line in xlist:
        temp_file.write(line+'\n')
    temp_file.close()


def main():
    while True:
        print('请输入关键字，然后回车，多个关键字用+进行连接，如“辉夜大小姐+极影”')
        key_words = input(':')
        if len(key_words) > 0:        
            temp_list = []
            temp_list = get_link_list(key_words)
            list_to_txt(temp_list)
            break
        else:
            print('您的输入有误，请重新输入')

if __name__ == '__main__':
    main()