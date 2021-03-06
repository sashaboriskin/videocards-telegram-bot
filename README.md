Инструкция по использованию “Heroku”

Выполнили студенты группы БИВТ-21-8
Борискин Александр, Павел Фетисов, Павел Кошкин

Установка PyCharm и Python
Чтобы пользоваться нашим ботом и вносить изменения в проект нужно установить среду разработки. Мы советуем PyCharm.
Ссылка на скачивание: https://www.jetbrains.com/ru-ru/pycharm/download/#section=windows
Ссылка на скачивание Python: https://www.python.org/downloads/

Импорт проекта
 
Нажимаем на open и открываем проект, который мы вам скинули. 
Далее нажимаем на settings и выбираем кодировку windows-1251 и устанавливаем все библиотеки из списка.

 
Далее в строку Python packages вбиваем вот эти библиотеки в строку поиска и нажимаем на install.
1)	Pandas
2)	Requests
3)	Bs4
4)	Aiogram
5)	Pycoingecko
6)	Openpyxl

Содержание проекта

На картинке вы можете наблюдать все файлы в нашем проекте. Для ясности картины хочу вкратце рассказать о каждом файле. 
Главный файл – main.py (Он исполняется на удаленном сервере, в нем прописана логика работы телеграмм бота). 
Markup.py и Spisok.py созданы для анимации кнопок в боте.
 parse.py используется для автономного обновления базы данных с видеокартами. Он сканирует сайты и заносит данные в текстовые документы, а после заносит в csv таблицы. Его можно запускать, например, раз в полгода для обновления цен. Также можно вручную изменять базы данных, просто открывая их в экселе или гугл документах. Чтобы изменения в базе данных появились в телеграм боте, нужно заново проделать операции по отправке проекта на удаленный сервер (Смотрите следующие страницы).
Отзывы.txt и bool отзыв.txt созданы для хранения отзывов пользователей.
Список пользователей.txt создан для хранения данных о пользователей, которые использовали наш бот.
В Список возникших ошибок.txt вносятся все ошибки, которые возникают при работе бота для дальнейшего дебагинга и усовершенствования бота. 
Procfile и requirements – служебные файлы для работы с удаленным сервером.
Все другие файлы – базы данных. Может показаться, что базы данных повторяются, но это не так. Один файл имеет расширение csv, а другой xlms. Это нужно для хорошей работы бота. 

Heroku (для работы с удаленным сервером)

Сначала зайдем на сайт Heroku
Ссылка: https://id.heroku.com/login
Нам надо зарегистрироваться:
 
Далее создаем проект

Теперь нам нужно установить на компьютер GIT для создания локального репозитория. Переходим на официальный сайт https://git-scm.com/downloads и скачиваем сам GIT с настройками по умолчанию.
 
Далее заходим обратно на Heroku, переходим в раздел Deploy и устанавливаем Heroku CLI. Путь установки выбираем нашу папку с проектом – это важно!
Далее на Heroku заходим в раздел Settings и добавляем Buildpack:
После открываем в нашей папке проекта файл main.py с помощью Pycharm. Заходим в terminal и прописываем следующие команды:
~ heroku login

Переходим в браузер и нажимаем log in
Далее:
~ git init
~ git add .
~ git commit -am "Start"
~ heroku git:remote -a hyperbot115(hyperbot115 - название приложения в Heroku, которое мы задали при создании Рис. 3, если у вас не такой, то вместо его введите свое)
~ git push heroku master

 
После того, как всё установится на Heroku нужно ввести в терминале следующую команду:
~ heroku ps:scale worker=1
Эта команда активирует бота на сервере. Чтобы приостановить самого бота нужно ввести команду: 
~ heroku ps:scale worker=0


Обновление данных на Heroku

Для начала нужно приостановить нашего бота 
~ heroku ps:scale worker=0
После этого надо закрыть проект main.py и открыть с помощью Pycharm файл parse.py
Далее запускаем сам парсинг и ждем пока он всё запарсит:
 
После этого приостанавливаем сам парсер и закрываем проект. Потом снова открываем файл в Pycharm’е main.py, заходим в терминал и прописываем следующие команды:
~ git add .
~ git commit -m "updated the header and footer"
~ git push heroku master
Теперь все файлы на сервере обновлены)))



