"""
第十三个是的月票
&#100152;&#100152;&#100146;&#100153;&#100148;&#100155
1        1       5         0        7         6

</style><span class="RZRqbBZe">&#100157;&#100152;&#100146;&#100155;&#100153;</span></span>


"""
"""
import re
str_ = '</style><span class="RZRqbBZe">&#100157;&#100152;&#100146;&#100155;&#100153;</span></span>月票</p>'
res_ = re.findall(r'</style><span class="RZRqbBZe">(.*?)</span></span>月票</p>',str_)
print(res_)

class属性不能写实，用贪恋来替代
https://gitcode.com/open-source-toolkit/6d2177/?utm_source=tools_gitcode&index=top&type=card&uuid_tt_dd=10_30727864350-1775039500172-614769&from_id=143129855&from_link=61bb68d88c1649e883f28379606bfbcb
去下载字体编辑器免费版本，如果好用可以去赞助一下创作者
进行字体匹配
找到之后使用fontget
找到字体加密文件的位置所在，在全局搜索里面查找
最后发现在url中的文本里面包含了这个加密文件的地址
<p><span><style>@font-face { font-family: AojEsnyw; src: url('https://qdfepccdn.qidian.com/gtimg/qd_anti_spider/AojEsnyw.eot?') format('eot')
"""
"""
from fontTools.ttLib import TTFont
font_obg = TTFont('MUpIszvv.woff')
font_obg.saveXML('font1.xml')
res_ = font_obg.getBestCmap()
print(res_)
<p><span><style>@font-face { font-family: NqiwIOEN; src: url('https://qdfepccdn.qidian.com/gtimg/qd_anti_spider/NqiwIOEN.eot?') format('eot'); src: ur
"""
import re
str_ = " format('eot'); src: url('https://qdfepccdn.qidian.com/gtimg/qd_anti_spider/NqiwIOEN.woff') format('woff')"
res_ = re.findall(r"format\('eot'\); src: url\('(.*?)'\) format\('woff'\)",str_)[0]
print(res_)