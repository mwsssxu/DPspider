#coding:utf-8
import requests
from settings import *
from settings import *
from config import STR_SVG_PATH,NUM_SVG_PATH,COMMENT_SVG_PATH
from decorator.decrypt import checkSVG
from util.http import send_http
from bs4 import BeautifulSoup as bs

def _clean(res_list):
    _ = []
    for i in res_list:
        if isinstance(i,str):
            _.append(i.strip('\n'))
    return ''.join(_).strip()

@checkSVG(NUM_SVG_PATH)
def _get_num_svg(url,svg=None):
    if svg is None:
        resp = send_http( requests.Session(),
                          'get',
                          url,
                          retries=-1,
                          headers=CSS_HEADERS
                          )
        svg = resp[0].text
    if svg:   
        text = bs(svg, 'lxml')
        texts = text('text')
        if not texts:
            res = {}
            text_path = text('textpath')
            path = text('path')
            for _, i in enumerate(path):
                d = i['d']
                num = int(d.split(' ')[1].strip())
                string = text_path[_].text.strip()
                res[num] = string
            return res,svg
        else:
            ys = {i['y']:i.text for i in texts if i}
            return ys,svg

@checkSVG(STR_SVG_PATH)
def _get_str_svg(url,svg=None):
    if svg is None:
        resp = send_http( requests.Session(),
                          'get',
                          url,
                          retries=-1,
                          headers=CSS_HEADERS
                          )
        svg = resp[0].text
    if svg:
        res = {}
        text = bs(svg,'lxml')
        text_path = text('textpath')
        if not text_path:
            texts = text('text')
            ys = {i['y']: i.text for i in texts if i}
            return ys,svg
        else:
            path = text('path')
            for _,i in enumerate(path):
                d = i['d']
                num = int(d.split(' ')[1].strip())
                string = text_path[_].text.strip()
                res[num]=string
            return res,svg

@checkSVG(COMMENT_SVG_PATH)
def _get_comment_svg(url,svg=None):
    if svg is None:
        resp = send_http( requests.Session(),
                          'get',
                          url,
                          retries=-1,
                          headers=CSS_HEADERS
                          )
        svg = resp[0].text
    if svg:
        res = {}
        text = bs(svg,'lxml')
        text_path = text('textpath')
        if not text_path:
            texts = text('text')
            ys = {i['y']: i.text for i in texts if i}
            return ys,svg
        else:
            path = text('path')
            for _,i in enumerate(path):
                d = i['d']
                num = int(d.split(' ')[1].strip())
                string = text_path[_].text.strip()
                res[num]=string
            return res,svg

def _find_head(cls,tag_dict):
    for tag,_list in tag_dict.items():
        if cls.startswith(tag):
            return _list

def _find_css(cls,css_dict):
    if cls in css_dict:
        return css_dict[cls]