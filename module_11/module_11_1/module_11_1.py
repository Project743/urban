import requests
from PIL import Image

URL = 'https://openweathermap.org/'
URL_API = 'https://api.openweathermap.org/data/2.5/weather'
name = 'москва'  # название города в кавычках

params = {'q': name, 'appid': '5796abbde9106b7da4febfae8c44c232', 'units': 'metric',
          'lang': 'zh_cn'}
with requests.Session() as session:
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})

    session.get(URL)

    r = session.get(URL_API, params=params)
    print(session.cookies)
    if r:
        js = r.json()
        location = js['name']
        coord = f'долгота: {js['coord']['lon']} / широта: {js['coord']['lat']}'
        speed_wind = js['wind']['speed']
        temp = js['main']['temp']
        print(f'город: {location} \n'
              f'координаты: {coord} \n'
              f'температура воздуха: {temp} \n'
              f'скорость ветра: {speed_wind}')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
url_ = 'https://httpbin.org/user-agent'
request = requests.get(url_, headers=headers)
print(request.text)
url_ = 'https://httpbin.org/response-headers'
params = {'freeform': 'hello'}
request = requests.post(url_, headers=headers, params=params)
print(request.text)
url_ = 'https://httpbin.org/post'
data = {
    "comments": "asd",
    "custemail": "3@c.s",
    "custname": "1",
    "custtel": "2",
    "delivery": "11:20",
    "size": "medium",
    "topping": "bacon"
}
request = requests.post(url_, headers=headers, data=data)
print(request.text)


def mirror(img):  # отзеркаливание изображения, принимает путь к файлу
    # загружаем изображение с жесткого диска
    original = Image.open(img)
    original = original.transpose(Image.FLIP_LEFT_RIGHT).convert(
        'L')  # отзеркаливание по горизонтали и конвертация в чб
    # im = original.transpose(Image.FLIP_TOP_BOTTOM) #отзеркаливанеи по вертикали
    original.save("mirror_" + img)
    original.close()


mirror('1.jpg')


def watermark(img, water):  # наложение одного изображения на другое
    original = Image.open(img)  # основное изображение
    watermark = Image.open(water).convert("RGBA")  # вспомогательное изображение

    width = original.size[0]  # ширина изображения
    height = original.size[1]  # высота изображения
    if width > height:  # в зависимости от пропорций основного изображения расчитываем размер накладываемого
        percent_w_h = watermark.size[0] / watermark.size[1]
        new_size_watermark = (int(width / 3), int(width / 3 / percent_w_h))
        if new_size_watermark[1] > height:
            new_size_watermark_height = height
            new_size_watermark_width = height * percent_w_h
            new_size_watermark = (int(new_size_watermark_width), int(new_size_watermark_height))
    else:
        percent_h_w = watermark.size[1] / watermark.size[0]
        new_size_watermark = (int(height / 3 / percent_h_w), int(height / 3))
        if new_size_watermark[0] > width:
            new_size_watermark_width = width
            new_size_watermark_height = width * percent_h_w
            new_size_watermark = (int(new_size_watermark_width), int(new_size_watermark_height))
    mark = watermark.resize((new_size_watermark))  # задаем новый размер вспомогательному изображению
    loc = [int(width) - int(new_size_watermark[0]),
                0 + height - new_size_watermark[1]]  # определяем место наложения изображения

    original.paste(mark, loc, mark)  # накладываем изображение
    original.save("watermark" + img)
    original.close()
    watermark.close()


watermark('1.jpg', '2.png')
