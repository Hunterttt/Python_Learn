from contextlib import nullcontext
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

iheader = {"User-Agent": UserAgent().random}
session1 = requests.session()

page1 = session1.get('https://yoyaku.city.kita.tokyo.jp/shisetsu/reserve/gin_menu',headers=iheader)
page1_bs = BeautifulSoup(page1.text, 'lxml')

#print(page1.text)
sessiont1 = page1_bs.find(attrs={'name':'RiyosyaForm'})
sessiont2 = sessiont1.find(attrs={'name':'g_sessionid'})
sessionid1 = sessiont2.attrs.get('value')

print(sessionid1)


page2 = session1.post(
    url = 'https://yoyaku.city.kita.tokyo.jp/shisetsu/reserve/gin_init',
    data = {
        'g_sessionid': sessionid1,
        'x': 77,
        'y': 44,
        'u_genzai_idx': 0,
        'g_kinonaiyo': 35
    },
    headers=iheader
)
#print(page2.text)


page3 = session1.post(
    url = 'https://yoyaku.city.kita.tokyo.jp/shisetsu/reserve/gin_id_input',
    data = {
        'g_sessionid': sessionid1,
        'x': 337,
        'y': 63,
        'u_genzai_idx': 0,
        'g_kinonaiyo': 35
    },
    headers=iheader
)
#print(page3.text)



page4 = session1.post(
    url = 'https://yoyaku.city.kita.tokyo.jp/shisetsu/reserve/gin_login1',
    data = {
        'g_sessionid': sessionid1,
        'u_genzai_idx': 1,
        'g_kinonaiyo': 14,
        'g_riyoushabangou': 3100019255,
        'ansyono': 3385,
        'x': 79,
        'y': 42
    },
    headers=iheader
)

page4_bs = BeautifulSoup(page4.text, 'lxml')
sessiont3 = page4_bs.find(attrs={'name':'YykForm'})
sessiont4 = sessiont3.find(attrs={'name':'g_sessionid'})
sessionid2 = sessiont4.attrs.get('value')

print(sessionid2)


page5 = session1.post(
    url = 'https://yoyaku.city.kita.tokyo.jp/shisetsu/reserve/gin_z_group_sel_1',
    data = {
        'g_sessionid': sessionid2,
        'x': 107,
        'y': 73,
        'u_genzai_idx': 0,
        'g_kinonaiyo': 17
    },
    headers=iheader
)
#print(page5.text)



page6 = session1.post(
    url = 'https://yoyaku.city.kita.tokyo.jp/shisetsu/reserve/gin_z_group_sel_2',
    data = {
        'g_sessionid': sessionid2,
        'checkedAll': 'false',
        'g_bunruicd': 5001,
        'bunruicd': 5001,
        'u_genzai_idx': 1,
        'g_kinonaiyo': 17,
        'pageflg': 1
    },
    headers=iheader
)
#print(page6.text)


page7 = session1.post(
    url = 'https://yoyaku.city.kita.tokyo.jp/shisetsu/reserve/gin_z_dest_sel',
    data = {
        'g_sessionid': sessionid2,
        'checkedAll': 'false',
        'g_bunruicd': 5101,
        'bunruicd': 5101,
        'u_genzai_idx': 2,
        'g_kinonaiyo': 17,
        'pageflg': 2
    },
    headers=iheader
)
#print(page7.text)


page_courts = session1.post(
    url = 'https://yoyaku.city.kita.tokyo.jp/shisetsu/reserve/gin_z_amenity_sel',
    data = {
        'g_sessionid': sessionid2,
        'riyosmk': 5000,
        'u_genzai_idx': 3,
        'g_kinonaiyo': 17,
    },
    headers=iheader
)
#print(page_courts.text)


akabane_kiri = session1.post(
    url = 'https://yoyaku.city.kita.tokyo.jp/shisetsu/reserve/gin_z_room_sel',
    data = {
        'g_sessionid': sessionid2,
        'u_genzai_idx': 4,
        'g_kinonaiyo': 17,
        'g_basyocd': 63,
        'g_jitubasyocd': 521,
        'shisetugroup': 50,
        'g_systemcd': 1,
        'g_mkkbn': 2
    },
    headers=iheader
)
#print(akabane_kiri.text)



akabane_kiri_data = session1.post(
    url = 'https://yoyaku.city.kita.tokyo.jp/shisetsu/reserve/gin_z_dsp_sel',
    data = {
        'g_sessionid': sessionid2,
        'u_genzai_idx': 5,
        'g_kinonaiyo': 17,
        'g_kinomkkbn': 2,
        'g_basyocd': 63,
        'g_stgroup': 50,
        'g_sisetucd': 5056100
    },
    headers=iheader
)
#print(akabane_kiri_data.text)


'''
写爬虫时会遇到提交表单的问题，一般先构造data，然后利用post方式进行提交表单。
一般data的数据类型为字典，但当遇到多个数据项的属性名字重复时，则不能够使用字典了，因为字典中的键是不能够重复的。
对于这个问题的解决可以使用，列表+元组的形式进行data数据的构造。如下：
data=[('data_name','value'),('data_name','value'),('data_name','value')...]
'''
akabane_kiri_xo0 = session1.post(
    url = 'https://yoyaku.city.kita.tokyo.jp/shisetsu/reserve/gin_z_datetime_sel_1',
    data = [   
        ('g_sessionid', sessionid2),            
        ('chkbox', 'on'),
        ('u_yobi', 0),
        ('chkbox', 'on'),
        ('u_yobi', 1),
        ('chkbox', 'on'),
        ('u_yobi', 2),
        ('chkbox', 'on'),
        ('u_yobi', 3),
        ('chkbox', 'on'),
        ('u_yobi', 4),
        ('chkbox', 'on'),
        ('u_yobi', 5),
        ('chkbox', 'on'),
        ('u_yobi', 6),
        ('chkbox', 'on'),
        ('u_yobi', 10),
        ('ymd', 20210629),
        ('u_genzai_idx', 6),
        ('g_kinonaiyo', 17)
    ],
    headers=iheader
)
#print(akabane_kiri_xo0.text)



akabane_kiri_ox1 = session1.post(
    url = 'https://yoyaku.city.kita.tokyo.jp/shisetsu/reserve/gin_z_amenitytime_sel_1',
    data = {
        'g_sessionid': sessionid2,
        'flg_sstkoma': 0,
        'u_genzai_idx': 7,
        'g_kinonaiyo': 17,
        'showStartKoma': 1,
        'showEndKoma': 7
    }
)
#print(akabane_kiri_ox1.text)


dates0 = session1.post(
    url = 'https://yoyaku.city.kita.tokyo.jp/shisetsu/reserve/gin_z_amenitytime_sel_1',
    data = {
        'g_sessionid': sessionid2,
        'u_genzai_idx': 7,
        'flg_ikou': 1,
        'hiduke_sousa_flg': 0,
        'u_hyojibi': 20210706,
        'yoyakuinfo': None,        #空的时候用None
        'g_kinonaiyo': 17,
        'showStartKoma': 1,
        'showEndKoma': 7
    }
)
#print(dates0.text)

dates0_bs = BeautifulSoup(dates0.text, 'lxml')
dates_temp1 = []
dates_temp1 = dates0_bs.find_all('tr')
#print(dates_temp1)
days = []
days.append(dates_temp1[1].find('strong'))
print(days)




'''
page_akabane_kawa = session1.post(
    url = 'https://yoyaku.city.kita.tokyo.jp/shisetsu/reserve/gin_z_room_sel',
    data = {
        'g_sessionid': sessionid2,
        'u_genzai_idx': 4,
        'g_kinonaiyo': 17,
        'g_basyocd': 66,
        'g_jitubasyocd': 532,
        'shisetugroup': 50,
        'g_systemcd': 1,
        'g_mkkbn': 2
    }
)
print(page_akabane_kawa.text)
'''