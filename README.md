
<h1 align="center">
  <br>
  <a href="https://github.com/xdearboy/HidakiNuke/"><img src="https://github.com/xdearboy/HidakiNuke/blob/main/assets/bomb.png?raw=true" alt="HidakiNuke" width="400"></a>
  
  <br>
  HidakiNuke
  <br>
</h1>

<h4 align="center">HidakiNuke - это утилита для быстрого краша дискорд серверов.</h4>

<p align="center">
  <a href="https://badge.fury.io/py/discord.py">
    <img src="https://badge.fury.io/py/discord.py.svg"
         alt="Gitter">
  </a>
  <a href="https://saythanks.io/to/xdearboy">
      <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
  </a>
  <a href="https://t.me/send?start=IVTISEyPdXCn">
    <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>

<p align="center">
  <a href="#Functions">Функции</a> •
  <a href="#how-to-use">Как использовать</a> •
  <a href="#config">Настройка</a> •
  <a href="#credits">Использованные библиотеки, авторы.</a> •
  <a href="#License">Лицензия</a>
</p>

![gif](https://github.com/xdearboy/HidakiNuke/raw/main/assets/slowed.gif)

<p align="center">
  <a href="https://youtu.be/_mOsrgssFAE" style="font-size: smaller">(Замедленная гифка), нажмите чтобы увидеть в нормальном качестве</a>
</p>

## <a name="Functions">Функции</a>
* Краш сервера
  - Создание каналов, ролей и событий
  - Спам в каналы
  - Антирейтлимитер, грамотное ограничение запросов.
* Пинг
  - Пинг до Discord
* Статистика
  - Реализованна система статистики (кол-во атак, среднее время краша)
* Доп-функции
  - Пока-что give_admin. В скором времени, будет пополняться.

* <i>Важно!</i> Скорость краша зависит от пинга до Discord. Поэтому винить создателей в якобы медленной скорости не нужно. При пинге 150, время атаки занимает 11 секунд, при меньшем пинге будет быстрее

## <a name="how-to-use">Как использовать</a>

Что бы запустить HidakiNuke, вам нужно иметь [Git](https://git-scm.com) и [Python](https://www.python.org/) на своём компьютере. После этого, вы можете прописать команды для установки HidakiNuke:

```bash
# Склонировуйте репозиторий
$ git clone https://github.com/xdearboy/HidakiNuke.git

# Перейдите в директорию
$ cd HidakiNuke

# Установите зависимости
$ pip3 install -r requirements.txt

# Запустите приложение
$ python3 main.py
```

## <a name="config">Настройка</a>

После, настройте файлы `config.py` и `token.py` в директории `src/config`. Это нужно, что бы бот корректно работал.

> **Заметка**
> Если у вас Windows, то используйте pip заместо pip3.

## <a name="credits">Использованные библиотеки, авторы</a>

- [disnake](https://disnake.dev/)
- [aiohttp](https://docs.aiohttp.org/en/stable/)
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [aiolimiter](https://github.com/mjpieters/aiolimiter)
- [Алекс Quite](https://discord.gg/GSABGHKg)
- [xdearboy](https://github.com/xdearboy)

## <a name="License">Лицензия</a>

MIT

---

> [garticrashers.ru](https://garticrashers.ru) &nbsp;&middot;&nbsp;
> GitHub [@xdearboy](https://github.com/xdearboy) &nbsp;&middot;&nbsp;
> Telegram канал [@vroffteam](https://t.me/vroffteam)

