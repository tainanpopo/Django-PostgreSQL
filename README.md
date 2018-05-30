# Django-PostgreSQL
練習Django並搭配Heroku PostgreSQL，測試資料庫操作。

## 關於此專案
* 左邊的表格是網頁顯示出來的結果
* 右邊的表格是在[pgadmin3](https://www.postgresql.org/ftp/pgadmin/pgadmin3/v1.22.2/win32/)顯示
![alt tag](https://i.imgur.com/NSVtJ5v.png)

## 注意事項
* 靜態網站設置利用[whitenoise](http://whitenoise.evans.io/en/stable/django.html)
* 查看資料庫利用[pgadmin3](https://www.postgresql.org/ftp/pgadmin/pgadmin3/v1.22.2/win32/)
會利用[pgadmin3](https://www.postgresql.org/ftp/pgadmin/pgadmin3/v1.22.2/win32/)的原因是
直接利用[Heroku](https://dashboard.heroku.com/)的dashboard無法看出tabel內的資料。

## Push to Heroku
* 確認專案設置完整之後，先在本地migrate後，再開始push。
heroku login
heroku git:remote yourapp
git add .
git commit -m "django-postgresql" 
git push heroku master
* 推上去之後會failed，輸入以下指令:
heroku config:set DISABLE_COLLECTSTATIC=1
* 給予[Heroku](https://dashboard.heroku.com/)APP一個乾淨空白的資料庫跟超級使用者。
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser

## 參考資料
* 熱於分享的高人
[twtrubiks](https://github.com/twtrubiks/Deploying_Django_To_Heroku_Tutorial)
[Python Django Book](http://www.books.com.tw/products/0010762818)
[Connecting with Django](https://devcenter.heroku.com/articles/heroku-postgresql#connecting-with-django)