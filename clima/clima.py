import requests
import json
from conf import API_KEY

# , -68.157175

lat = '35'
lon = '139'
        # 'https://samples.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=439d4b804bc8187953eb36d2a8c26a02'
url = f'https://samples.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
# print(url)
r = requests.get(url)

print(f'status code: {r.status_code}')
# print(f'text: {r.text}')

i = r.text.find('temp')
temp_str = r.text[i+6:i + 6 +7]
# print(temp_str)
temp_obj = json.loads(r.text)
# print(type(temp_obj))
# print(temp_obj)
temp = temp_obj['main']['temp']
print(f'temperatura actual: {temp}, tipo: {type(temp)}')

# 
if temp < 10:
    print('tapar plantita')
else:
    print('destapar')

# sockets TCP   ==> socket (standar)
# GUI           ==> tkinter (standar)
# servidor web  ==> flask (externo)
