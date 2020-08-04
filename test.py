from dianping import DianPing
from city import City

dp = DianPing()
provinces = dp.provinces
# print(provinces)

"""
{'北京': {'areaId': 1, 'provinceId': '1'}, '天津': {'areaId': 1, 'provinceId': '2'}, '河北': {'areaId': 1, 'provinceId': '3'},
 '山西': {'areaId': 1, 'provinceId': '4'}, '内蒙古': {'areaId': 1, 'provinceId': '5'},
 '辽宁': {'areaId': 2, 'provinceId': '6'}, '吉林': {'areaId': 2, 'provinceId': '7'},
 '黑龙江': {'areaId': 2, 'provinceId': '8'}, '上海': {'areaId': 3, 'provinceId': '9'},
 '江苏': {'areaId': 3, 'provinceId': '10'}, '浙江': {'areaId': 3, 'provinceId': '11'},
 '安徽': {'areaId': 3, 'provinceId': '12'}, '福建': {'areaId': 3, 'provinceId': '13'},
 '江西': {'areaId': 3, 'provinceId': '14'}, '山东': {'areaId': 3, 'provinceId': '15'},
 '河南': {'areaId': 4, 'provinceId': '16'}, '湖北': {'areaId': 4, 'provinceId': '17'},
 '湖南': {'areaId': 4, 'provinceId': '18'}, '广东': {'areaId': 4, 'provinceId': '19'},
 '广西': {'areaId': 4, 'provinceId': '20'}, '海南': {'areaId': 4, 'provinceId': '21'},
 '重庆': {'areaId': 5, 'provinceId': '22'}, '四川': {'areaId': 5, 'provinceId': '23'},
 '贵州': {'areaId': 5, 'provinceId': '24'}, '云南': {'areaId': 5, 'provinceId': '25'},
 '西藏': {'areaId': 5, 'provinceId': '26'}, '陕西': {'areaId': 6, 'provinceId': '27'},
 '甘肃': {'areaId': 6, 'provinceId': '28'}, '青海': {'areaId': 6, 'provinceId': '29'},
 '宁夏': {'areaId': 6, 'provinceId': '30'}, '新疆': {'areaId': 6, 'provinceId': '31'},
 '香港': {'areaId': 7, 'provinceId': '32'}, '澳门': {'areaId': 7, 'provinceId': '33'},
 '台湾': {'areaId': 7, 'provinceId': '34'}}
"""

sh = City('上海')
# url = sh.url

sh.get()
# locations = sh.locations

results = sh.search('咖啡', category='咖啡厅', location='嘉定区', save=False, details=True)
print(results)
