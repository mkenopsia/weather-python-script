#!/usr/bin/env python3
import requests
import argparse

parser = argparse.ArgumentParser(description="Пример скрипта с аргументами")

parser.add_argument('cityName', type=str, help='Первый параметр')

args = parser.parse_args()

currCity = args.cityName.lower()
appId = ":)" #your key
city_id = 0


def getWeather(id):
    currRes = requests.get("http://api.openweathermap.org/data/2.5/weather",
                                params={'id': id, 'units': 'metric', 'lang': 'ru', 'APPID': appId})
    currData = currRes.json()

    print("\n")
    print(currData['name'])
    print("Общее: ", currData['weather'][0]['description'])
    print("Температура: ", currData['main']['temp'])
    print("Ветер: ", currData['wind']['speed'])
    print("\n")

if (currCity == 'tomsk'): 
    getWeather(1489425)

elif (currCity == 'zelenogorsk'):
    getWeather(1488253)

else: 
    try: 
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                            params = {'q': currCity, 'type': 'like',
                                    'units': 'metric', 'APPID': appId})
        
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                for d in data['list']]
        choose = 0
        if(len(cities) > 1):
            print("choose your city (type '0' for print all): \n")
            index = 1
            for i in cities: 
                print(f"{i} {index}\n")
                index += 1
            choose = int(input())

        if(choose != 0):
            city_id = data['list'][choose-1]['id']
            getWeather(city_id)

        else:
            listCities = [data['list'][i]['id'] for i in range(len(data['list']))]

            for i in listCities:
                getWeather(i)

    except Exception as e:
        print("Exception (find):", e)
        pass
