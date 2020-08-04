# coding:utf-8

from settings import *
from config import TAG_CHANGED, COMMENT_TAGS
from bs4.element import Tag
from util.tools import from_pattern
from util.decrypt import _clean, _find_css, \
    _find_head, _get_str_svg, _get_num_svg, _get_comment_svg


class Decrypter(object):

    def __init__(self, shopId=None):
        self.shopId = shopId
        self.svg = None
        self._str_svg = None
        self._num_svg = None

    def decrypt(self, soup, cls_dict, css_dict, pattern='.*', comment=False):
        '''
        soup:加密的标签
        cls_dict,css_dict:解析css文件得到的解密字典。
        pattern:解密后的正则匹配模式，会匹配解密后的文本，将符合正则的内容返回
        comment:当前标签是否属于点评评论标签。有些不是属于评论内容的标签不用置True
        '''
        _contents = soup.contents
        _ = []
        while _contents:
            i = _contents.pop(0)
            if isinstance(i, Tag):
                if i.name in DECRYPT_TAGS:
                    if i['class'][0] in IGNORED_SPAN_CLASS:
                        continue
                    if i['class'][0] == 'item':
                        i_contents = i.contents
                        for j in reversed(i_contents):
                            _contents.insert(0, j)
                        continue
                    i = self._get_decrypted(i, cls_dict, css_dict, comment)
            elif not isinstance(i, str):
                continue
            _.append(i)
        text = _clean(_)
        return from_pattern(pattern, text)

    def _get_decrypted(self, element, tag_dict, css_dict, comment=False):
        cls = element['class'][0]
        f, url = _find_head(cls, tag_dict)
        _css = _find_css(cls, css_dict)
        if f and _css:
            if not comment:
                svg = {
                    TAG_CHANGED['string']: self._str_svg,
                    TAG_CHANGED['number']: self._num_svg,
                }[element.name]
                if svg is None:
                    svg = eval(DECRYPT_TAGS[element.name.strip()])(url)
                    {
                        TAG_CHANGED['string']: self._str_svg,
                        TAG_CHANGED['number']: self._num_svg,
                    }[element.name] = svg
            else:
                svg = {
                    COMMENT_TAGS['string']: self._str_svg,
                    COMMENT_TAGS['number']: self._num_svg,
                }.get(element.name)
                if svg is None:
                    svg = eval(DECRYPT_TAGS[element.name.strip()])(url)
                    {
                        COMMENT_TAGS['string']: self._str_svg,
                        COMMENT_TAGS['number']: self._num_svg,
                    }[element.name] = svg
                if self.svg is None:
                    self.svg = _get_str_svg(url) if not comment else _get_comment_svg(url)
                svg = self.svg
            for y, _str in svg.items():
                if _css['y'] > int(y):
                    continue
                x = int(_css['x'] / f)
                return _str[x]
