import params as params
import requests
s_city = 'Khakasiya Republic, RU'
appid = '62886c6662acea5756eabe22c6874ae1'
'''res = requests.get('https://api.openweathermap.org/data/2.5/weather',
                  params= {'q':s_city, 'units':'metric', 'lang':'ru','APPID':appid})
data=res.json()

print('город:', s_city)
print('Погодные условия:', data['weather'][0]['description'])
print('Температура:', data['main']['temp'])
print('Мин температура:', data['main']['temp_min'])
print('Макс температура:', data['main']['temp_max']) '''

res = requests.get('https://api.openweathermap.org/data/2.5/forecast',
                   params= {'q':s_city, 'units':'metric', 'lang':'ru','APPID':appid})
data=res.json()

print('Прогноз погоды на неделю:')
for i in data ['list']:
    print('Дата<', i['dt_txt'], '>\r\nТемпература<',
    '{0:+3.0f}'.format(i['main']['temp']), '> \r\nПогодные условия<',
    i['weather'][0]['description'],'>')
    print('----------------------------')