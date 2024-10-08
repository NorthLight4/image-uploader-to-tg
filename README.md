# Космический Телеграм

Данный проект содержит набор скриптов, часть из которых совершает запрос к различным API (SpaceX, NASA) для скачивания изображений космоса, а другая публикует данные в телеграм канал через бота.

### Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

#### Настройка окружения

1) Вам нужно получить сервисный токен NASA. [Сервисный токен](https://api.nasa.gov/)
2) Создайте Телеграм бота и получите его токен. [Создание бота](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)
3) Узнайте ID чата, куда должны отправляться изображения. [Узнать ID](https://pikabu.ru/story/kak_uznat_identifikator_telegram_kanalachatagruppyi_kak_uznat_chat_id_telegram_bez_botov_i_koda_11099278)

Создайте файл .env в корневом каталоге проекта и запишите значения из предыдущих пунктов в переменные NASA_API_KEY, TG_BOT_TOKEN, CHAT_ID соответственно.

### Примеры запуска скриптов

Далее приведём примеры работы программ.

#### 1) Загрузить фотографии запуска ракет SpaceX
По умолчанию скачивает фотографии последнего запуска (при их наличии). В качестве параметра launch_id указываем ID нужного нам запуска.
```
python fetch_spacex_images.py
python fetch_spacex_images.py -launch_id 5eb87d2dffd86e000604b376
```

#### 2) Загрузить NASA APOD (Astronomy Picture of the Day)
По умолчанию скачивается одно изображение. В качестве параметра count указываем количество нужных для скачивания изображений.
```
python fetch_nasa_apod.py
python fetch_nasa_apod.py -count 5
```

#### 3) Загрузить NASA EPIC (Earth Polychromatic Imaging Camera)
По умолчанию скачивается одно изображение. В качестве параметра count указываем количество нужных для скачивания изображений.
```
python fetch_nasa_epic.py
python fetch_nasa_epic.py -count 5
```

#### 4) Выгрузить фотографию в Телеграмм канал
ТГ бот публикует указанное в качестве параметра фото. При отсутствии параметра image_name публикует случайное фото. Укажите имя фото вместе с __расширением__!
```
python post_image_to_channel.py
python post_image_to_channel.py -image_name nasa_apod_0.jpg
```

#### 5) Выгрузить директорию в Телеграмм канал
ТГ бот публикует всю директорию изображений с указанным в качестве параметра интервалом (указывается в секундах). По умолчанию интервал равен 4 часам. При отправке конечного изображения скрипт перемешает фотографии в случайном порядке и начнет отправку снова.
```
python post_images_constantly.py
python post_images_constantly.py -interval 120
```

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).