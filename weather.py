# coding=utf-8

import requests
import json
import jsonpath

session = requests.session()
response = session.get('https://api.caiyunapp.com/v2/aJkb6gTZrkEqnAQh/121.6544,25.1552/realtime?unit=metric:v2')
# print response.text
js = json.loads(response.text)
print js['result']
tmp = str(jsonpath.jsonpath(js, '$.result.temperature')[0])
pm10 = str(jsonpath.jsonpath(js, '$.result.pm10')[0])
pm25 = str(jsonpath.jsonpath(js, '$.result.pm25')[0])
skycon = jsonpath.jsonpath(js, '$.result.skycon')
if str(skycon[0]).find('CLEAR') != -1:
    sky = u'晴'
elif str(skycon[0]).find('PARTLY_CLOUDY') != -1:
    sky = u'多云'
elif str(skycon[0]).find('CLOUDY') != -1:
    sky = u'阴'
elif str(skycon[0]).find('RAIN') != -1:
    sky = u'雨'
elif str(skycon[0]).find('SNOW') != -1:
    sky = u'雪'
elif str(skycon[0]).find('WIND') != -1:
    sky = u'风'
elif str(skycon[0]).find('HAZE') != -1:
    sky = u'雾霾沙尘'
rain = str(jsonpath.jsonpath(js, '$.result.precipitation.local.intensity')[0])
wind_direct = float(jsonpath.jsonpath(js, '$.result.wind.direction')[0])
if (wind_direct >= 337.5) or (wind_direct < 22.5):
    wd = u'北'
elif (wind_direct >= 22.5) and (wind_direct < 67.5):
    wd = u'东北'
elif (wind_direct >= 67.5) and (wind_direct < 112.5):
    wd = u'东'
elif (wind_direct >= 112.5) and (wind_direct < 157.5):
    wd = u'东南'
elif (wind_direct >= 157.5) and (wind_direct < 202.5):
    wd = u'南'
elif (wind_direct >= 202.5) and (wind_direct < 247.5):
    wd = u'西南'
elif (wind_direct >= 247.5) and (wind_direct < 292.5):
    wd = u'西'
elif (wind_direct >= 292.5) and (wind_direct < 337.5):
    wd = u'西北'
wind_speed = str(jsonpath.jsonpath(js, '$.result.wind.speed')[0])
humidity = float(jsonpath.jsonpath(js, '$.result.humidity')[0])*100


print u'温度: ' + tmp
print u'湿度: ' + str(humidity) + '%'
print 'pm2.5: ' + pm25
print 'pm10: ' + pm10
print u'天气: ' + sky
print u'降水: ' + rain + ' mm'
print u'风向: ' + wd
print u'风速: ' + wind_speed + ' km/h'


