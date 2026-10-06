import requests

# СЮДА ВСТАВЬ СВОЙ API-КЛЮЧ (в кавычках)
API_KEY = ""

city = "Moscow"

url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY + "&lang=ru&units=metric"

print("Ссылка:", url)
print("")

response = requests.get(url)

print("Код ответа:", response.status_code)
print("")

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print("Погода в Москве:")
    print("Температура:", temp, "°C")
    print("Описание:", description)
else:
    print("ОШИБКА!")
    print("Текст ошибки:", response.text)