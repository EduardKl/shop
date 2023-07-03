# Shop
Стек проекта:
- Python 3.11, Pipenv;
- Django, PostgreSQL, Celery, RabbitMQ;
- HTML, SCSS, JS.

Простой интернет-магазин на django с возможностью сложить товары в корзину и оформить заказ на них.
После оформления заказа на указанную клиентом почту отправляется письмо с подтверждением удачного оформления.

Запуск:
1. Для начала нужно клонировать репозиторий: git clone https://github.com/EduardKl/shop.git;
2. После установить виртуальное окружение и зависимости: pipenv sync;
3. Настроить переменные окружения в .env по шаблону .env.dist;
4. Запустить приложение: django ./manage.py runserver;
5. Во втором окне терминала запустить docker-контейнер брокера RabbitMQ: docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management;
6. В третьем окне терминала запустить работника Celery: celery -A shop_site worker -l info.
