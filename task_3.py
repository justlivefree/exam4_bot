from threading import Thread
import httpx


def my_func(url_json: str) -> None:
    req = httpx.get(url_json)
    data = req.text
    print(data, '\n')


links = ['https://api.chucknorris.io/jokes/random',
         'https://restcountries.com/v3.1/all',
         'https://dummyjson.com/products/1',
         'https://www.geonames.org/datasources/',
         'https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata']
oqimlar = {}

for i in range(len(links)):
    oqimlar.update({f'oqim{i + 1}': Thread(target=my_func, args=(links[i],))})

for oqim in oqimlar:
    oqimlar[oqim].start()
for oqim in oqimlar:
    oqimlar[oqim].join()

# oqim1 = Thread(target=my_func, args=('https://api.chucknorris.io/jokes/random',))
# oqim2 = Thread(target=my_func, args=('https://restcountries.com/v3.1/all',))
# oqim3 = Thread(target=my_func, args=('https://dummyjson.com/products/1',))
# oqim4 = Thread(target=my_func, args=('https://www.geonames.org/datasources/',))
# oqim5 = Thread(target=my_func, args=('https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata',))

# oqim1.start()
# oqim2.start()
# oqim3.start()
# oqim4.start()
# oqim5.start()
# oqim1.join()
# oqim2.join()
# oqim3.join()
# oqim4.join()
# oqim5.join()
