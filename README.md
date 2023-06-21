# how to start project

# open project go to manage.py location as - 
cd srcafe                # ex- in my case  Directory: C:\Users\HP\Desktop\iph\srCafe_django\srcafe
ls
# show manage.py file
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        05-06-2023     12:10                meal_images
d-----        05-06-2023     15:14                media
d-----        31-05-2023     18:42                myapp
d-----        31-05-2023     16:19                srcafe
-a----        16-06-2023     12:29         155648 db.sqlite3
-a----        05-06-2023     12:10            684 manage.py
-a----        21-06-2023     10:40              0 README.md

# python manage.py makemigrations
# python manage.py migrate

for database - 
# python manage.py createsuperuser
name, email,passowrd      note - password is not visual 


start project - 
# python manage.py runserver

# open admin dash bord 
http://127.0.0.1:8000/admin/

give email and passowrd   ( note - superuser email and password)


# open website ( HOME PAGE WEBSITE )
http://127.0.0.1:8000