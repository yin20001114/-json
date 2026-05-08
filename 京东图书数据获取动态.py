from selenium.webdriver import Chrome
from selenium.common.exceptions import TimeoutException
from lxml import etree
import json
import time
if __name__ == '__main__':
    page_ = int(input('请输入要保存的页数：'))
    chrom_obj = Chrome()
    chrom_obj.set_page_load_timeout(5)
    try:
        chrom_obj.get(
            'https://re.jd.com/search?keyword=%E5%B0%8F%E8%AF%B4&ad_od=3&traffic_source=1004&re_dcp=202m0QjIIg%3D%3D&bd_vid=nHDLPWb1PjmdP1nknjDdPj0dn19xnWcdg17xnH0s&cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=9603741117_0_101907452951397441778227791188')
        chrom_obj.maximize_window()
    except TimeoutException:
        print('主页渲染超时了.......')
    time.sleep(2)
    for page_1 in range(page_):
        for i in range(5):
            time.sleep(0.5)
            j = (i+1) * 640
            js_ = f'document.documentElement.scrollTop={j}'
            chrom_obj.execute_script(js_)

        html = chrom_obj.page_source
        html_obj = etree.HTML(html)
        value = html_obj.xpath('//div/img/@data-item')
        name_list = []
        price_list = []
        for i in value:
            new_data = ''.join(i)
            new_data2 = json.loads(new_data)
            name = new_data2['title']
            price = new_data2['price']
            name_list.append(name)
            price_list.append(price)
        name_list2 = name_list[:48]
        price_list2 = price_list[:48]
        with open(f'京东{page_1}.json', 'a', encoding='utf-8') as f:
            for i in range(len(name_list2)):
                dict_ = {}
                dict_[name_list2[i]] = price_list2[i]
                json_data = json.dumps(dict_, ensure_ascii=False) + ',\n'
                f.write(json_data)
        print("*"*200)

        try:
            click = chrom_obj.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div/div/div/div[4]/div/div[10]')
            click.click()
        except:
            continue






