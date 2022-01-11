House-of-Bake is the name of the application where customer can come and register their credantials.

The Frontend consist two part, an intro part with a button name Register and an svg img.
And the footer part comes with a tagline, address div, contact us div, and few card pics.

The file name index.html is created and link to a stylesheet name style.css.
When a customer can visit the site, if he/she click to register button then it will redirect to register.html where
they can enter their credentials. if it is true, then the page will redirect to success.html. If without any field they register, a message will pop up on the screen. To display how many attendees attend in the site,
visit http://localhost:5000/users

Technology used:
HTML, CSS, JS. - Frontend
Python - Backend
Postgres - Database

In the Application, filename - app.py five routes are used, named.

1. For Homepage (/). http://127.0.0.1:5000/
2. For Registration (/register) route. http://127.0.0.1:5000/register
3. For Submission (/submit). http://127.0.0.1:5000/submit
4. For API route (/attendees). Here, all the users from the database is fetch. http://localhost:5000/attendees
5. To Display the users in html page (/users) route is created. To visit: http://localhost:5000/users

To run the application, go to root folder, type- python app.py

In app.py, if you change the URI you can connect your own postgres account.
To connect to the database from terminal type:
step 1 : python
step 2 : from app import db
step 3 : db.create_all()
