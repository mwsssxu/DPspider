# coding:utf-8
import codecs
from util.shop import parse_shop_css
from decrypt import Decrypter
from bs4 import BeautifulSoup as bs

# 解密步骤1：获取当前页面的html内容
with codecs.open('txt/fake.html', 'r', encoding='utf-8') as f:
    html = f.read()
# 解密步骤2：获取当前页面的加密用css文件内容，具体获取可以用正则匹配等
with codecs.open('txt/fake.css', 'r', encoding='utf-8') as f:
    css = f.read()
# 解密步骤3：整个html进行解析后，获取要解密内容所在的标签，例如，店铺地址所在的标签,店铺点评评论
soup = bs(html, 'lxml')
address_tag = soup('div', class_='expand-info address')[0]
comment_tag = soup('p', class_='desc J-desc')[0]
print(f'未解密地址标签：{address_tag}\n')
print(f'为解密店铺点评评论：{comment_tag}\n')
# 解密步骤4：直接解析获取到的CSS文件，具体规则看函数parse_shop_css
# 此步骤获取到解密映射字典
cls_dict, css_dict = parse_shop_css(css)
# 解密步骤5：使用Decrypter对象解密标签获得解密文本
# 其中，Decrypter的decrypt函数增加了参数说明
# 下面解析地址标签的内容
decrypter = Decrypter()
text = decrypter.decrypt(address_tag, cls_dict, css_dict)
dp = decrypter.decrypt(comment_tag, cls_dict, css_dict, comment=True)
print(f'解密后地址文本：{text}\n')
print(f'解密后店铺点评评论：{dp}\n')
# 其他的加密标签解密也是类似的:)
