# MyBlog-WebApp

A small effort by me to create my own blogging application.I would recommend you to view this on PC/Laptop/Desktop for a beautiful experience.


Hosted on pythonanywhere.com . Check this link: 
```
https://debanjan2001.pythonanywhere.com/
```

![Demo](https://user-images.githubusercontent.com/56274058/115596567-dfc74d80-a2f5-11eb-8fc1-9975d00bb1c1.gif)


Clone This Project (Make Sure You Have Git Installed)
```
git clone https://github.com/Debanjan2001/MyBlog-WebApp.git
```

Change your directory to the cloned repo

```
cd <<Your Download Location Here>>/MyBlog-Webapp
```

Install Dependencies 

```
pip install -r requirements.txt
```

Set Database (Make Sure you are in directory same as manage.py)
```
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations
```

Create SuperUser to get admin login features
```
python manage.py createsuperuser
```

After all these steps , you can start enjoying this project. 

#### P.S. - It is not perfectly optimised for mobile version, but you won't face any major trouble while using the hosted website through mobile .
