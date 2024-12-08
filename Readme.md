### Model Explainability and Interpretability  

##### Introduction:    


This project uses [Flask](https://flask.palletsprojects.com/en/stable/) to create the web application and 
[bootstrap](https://getbootstrap.com/) for styling. Flask in turn uses [Jinja Templates](https://jinja.palletsprojects.com/en/stable/) 
to dynamically build HTML pages using python constructs. [SQLite](https://www.sqlite.org/) is used as a database 
and [DB Browser for SQLite](https://sqlitebrowser.org/) is used as SQL Client.

##### Set up environment    
$ Go to project web API root (e.g. cd ~/workspace/projects/nishkarsh/src/webUI)    
$ Activate virtual environment. (e.g. workon nishkarsh)     
$ pip install -r requirements.txt

##### Set up database. 
Open a new tab and go to project root.     
Run the queries in src/webUI/sqlite/schema.sql using DB Browser for SQLite.    
$ cd src/webUI/sqlite/       
$ python init_db.py     

##### Run the application
Open a new tab and go to project root.    
$ cd ~/workspace/projects/nishkarsh/src/webUI 
$ export FLASK_APP=app     
$ export FLASK_ENV=development    
$ flask run     
Open the URL at http://127.0.0.1:5000/    
To hot deploy     
$ flask --debug run      
To run another server    
$ flask run -p 5001      

##### References
1.[Bootstrap framework for html/CSS/Java Script](https://getbootstrap.com/)     
2.[Flask tutorial](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)   
3.[Sqlite Database](https://www.sqlite.org/)    
4.[Bootstrap w3School Docs](https://www.w3schools.com/bootstrap4/default.asp)    
5.[Bootstrap Example](https://getbootstrap.com/2.0.4/examples/hero.html)
6.[Setting up Blueprints](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications#1-flask-the-minimalist-application-development-framework)