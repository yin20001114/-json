import requests
from lxml import etree
import re
from fontTools.ttLib import TTFont
import json
if __name__ == '__main__':
    url_ = "https://www.qidian.com/rank/yuepiao/"
    headers_ = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
        "Cookie":"e1=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A4%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_P_rank%22%2C%22eid%22%3A%22qd_C19%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A4%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_P_rank%22%2C%22eid%22%3A%22qd_C19%22%7D; newstatisticUUID=1778133756_1131627410; traffic_utm_referer=https%3A//www.baidu.com/link; fu=372233468; supportwebp=true; _csrfToken=CT8IxgymFbfflx3ydJ3opOmLVtPejxeuxjYOrGOC; Hm_lvt_f00f67093ce2f38f215010b699629083=1778133787,1778146173,1778146424; HMACCOUNT=9FC561839E7615F8; ywguid=2335916524; ywkey=ywPMIilZbmQd; ywopenid=5BF20B141827EC0543D589A819F29187; e1=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A3%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A16%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A3%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A1001%22%7D; Hm_lpvt_f00f67093ce2f38f215010b699629083=1778146759; w_tsfp=ltvuV0MF2utBvS0Q7qLokE2pEDwidzg4h0wpEaR0f5thQLErU5mC2Yd+uMzxNXTZ4cxnvd7DsZoyJTLYCJI3dwNBEZmSJo5HiguYlNcn3ItBBkIyEc3bCwVLcu537mIULnhCNxS00jA8eIUd379yilkMsyN1zap3TO14fstJ019E6KDQmI5uDW3HlFWQRzaLbjcMcuqPr6g18L5a5W3bsQiuKw4lBr1FgUXHgykYWCog6Ue4drgMNBWsIZ2sSqA="
    }
    response_ = requests.get(url_,headers=headers_)
    data_ = response_.text
    data_obg = etree.HTML(data_)
    name = data_obg.xpath('//div/h2/a/text()')
    #获取成功，报错原因故就是没有用原始的cookie
    #value_ =data_obg.xpath()
    #用xpath提取不到，用正则提取，获取的密文的数据
    mon_list = re.findall(r'</style><span class=".*?">(.*?)</span></span>月票</p>',data_)
    #进行密文文件的地址获取
    str_ = data_obg.xpath('//span/style/text()')[0]
    woff_url = re.findall(r"format\('eot'\); src: url\('(.*?)'\) format\('woff'\)", str_)[0]
    response_woff = requests.get(woff_url,headers=headers_)
    with open('qidian.woff','wb') as f:
        f.write(response_woff.content)
        # 解析字体加密文件
        font_obj = TTFont('qidian.woff')
        # 转成明文格式的xml文件
        font_obj.saveXML('qidian.xml')

        # 直接获取到加密关系映射表
        cmap_dict = font_obj.getBestCmap()
        print('字体加密映射表:', cmap_dict)
        # 定义一个英文数字:阿拉伯数字的字典
        dict_b = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                  'eight': '8',
                  'nine': '9', 'zero': '0'}

        # 进行替换
        for i in cmap_dict:  # i:a的健名
            for j in dict_b:  # j:b的健名
                if cmap_dict[i] == j:
                    cmap_dict[i] = dict_b[j]
        print('转换之后的字体加密映射表:', cmap_dict)

        # 去除月票密文列表里面的特殊符号: &#
        new_mon_list = []
        for i in mon_list:  # i:'&#100074;&#100069;&#100070;&#100076;&#100075;'
            list_ = re.findall(r'\d+', i)
            new_mon_list.append(list_)
        print('去除特殊符号之后的月票列表:', new_mon_list)

        # 解析月票数据
        for i in new_mon_list:  # i:['100063', '100065', '100067', '100065', '100059']
            for j in enumerate(i):  # j:100065 还要得到他的索引 (0, '100063')
                for k in cmap_dict:  # k对应的是每个健名
                    if j[1] == str(k):  # 完成替换
                        i[j[0]] = cmap_dict[k]
        print('解析之后的月票数据列表:', new_mon_list)

        # 月票数据的拼接
        new_list = []
        for i in new_mon_list:  # i:['5', '1', '3', '3', '5']
            str_ = ''.join(i)
            new_list.append(str_)
        print('最终获取到的月票数据:', new_list)

        # 保存
        with open('qidian.json', 'w', encoding='utf-8') as f:
            for i in range(len(new_list)):
                dict_ = {}
                dict_[name[i]] = new_list[i]
                json_data = json.dumps(dict_, ensure_ascii=False) + ',\n'
                f.write(json_data)






