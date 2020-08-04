#  -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from scrapy import Selector
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.dianping.com/shanghai/ch10/g132')
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "J-img-pop"))
)

# 定位到要悬停的元素
# above = driver.find_element_by_link_text("静安寺")
# 对定位到的元素执行鼠标悬停操作
# ActionChains(driver).move_to_element(above).perform()

shops = []
for i in range(1, 50):
    time.sleep(3)
    try:
        driver.execute_script('document.getElementsByClassName("J-bonus-close")[0].click();')
    except:
        print('错误', flush=True)

    selector = Selector(text=driver.page_source)
    items = selector.css('.shop-list.J_shop-list.shop-all-list ul li')
    for item in items:
        # print(item.xpath('.//div[@class="tit"]/a/@title').extract_first())
        # 构造一个存放商户信息的字典
        shop = {
            # 通过xpaht获取店名
            'shop': item.xpath('.//div[@class="tit"]/a/@title').extract_first(),
            # 通过css选择器获取地址
            'location': item.css('.addr::text').extract_first(),
            'location_raw': str(item.xpath('.//div[@class="tag-addr"]/span//text()').extract()),
            # 通过xpaht获取商圈区域、商户等级、评价数、人均消费水平
            'region': item.xpath(
                './/div[@class="tag-addr"]//a[2]//span/text()').extract_first(),
            'level': item.xpath(
                '//div[@class="comment"]//span/@title').extract_first(),
            'comment': ''.join(
                item.xpath('.//a[@class="review-num"]//text()').extract()).strip(
            ).replace('\n', ''),
            'consume': ''.join(
                item.xpath('.//a[@class="mean-price"]//text()').extract()).replace(
                '\n', '').replace(' ', ''),
            'comment-list': str(item.xpath('.//span[@class="comment-list"]/span//text()').extract()).replace(
                '\n', '').replace(' ', ''),
        }

        shops.append(shop)
    print(shops)

    try:
        driver.execute_script('document.getElementsByClassName("next")[0].click();')
    except:
        print('错误', flush=True)
