# Horoscopes
<h1>Описание</h1>
<p>Этот проект являктся заданием по дисциплине Python в МФТИ.
<br>Он представляет собой скрапер гороскопов с  <a href="https://astroscope.ru/horoskop/ejednevniy_goroskop" target="_blank">сайта</a>
и отображение гороскопов на сайте, вся информация сохраняется в PostgreSQL</p>

<h1>Запуск с помощью скрипта</h1>
<p>Для запуска проекта с помощью скрипта вам необходим <a href="https://www.docker.com/products/docker-desktop/" target="_blank">Docker</a> 
</p>
<ol>
<li>Cклонируйте репозиторий с <a href="https://www.docker.com/products/docker-desktop/" target="_blank">Github</a></li>

```
git clone https://github.com/Entriqa/Horoscopes
```

<li>Перейдите в репозиторий с проектом
</li>

```
cd Horoscopes
```

<li>Запустите скрипт</li>

```
./run.sh
```

<li>Перейдите по <a href="http://172.19.0.5:3000/" target="_blank">ссылке</a></li>

</ol>

  
> Если скрипт не заупскается, попробуйте запустить его от имени администратора или выполните команду 
> ```sudo chmod +x run.sh```

<h1>Запуск с помощью Docker-compose</h1>
<p>Для этого вам необходимо установить Docker и docker-compose.
Как это сделать вы можете посмотреть <a href="https://www.docker.com/products/docker-desktop/" target="_blank">здесь</a>. </p>
<ol>
<li>Cклонируйте репозиторий с <a href="https://www.docker.com/products/docker-desktop/" target="_blank">Github</a></li>

```
git clone https://github.com/Entriqa/Horoscopes
```

<li>Перейдите в репозиторий с проектом
</li>

```
cd Horoscopes
```

<li>Запустите docker-compose</li>

```
docker-compose up
```

<li>Перейдите по <a href="http://172.19.0.5:3000/" target="_blank">ссылке</a></li>

</ol>

