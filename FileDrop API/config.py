import os

class Config:
    SECRET_PASS= os.environ.get('SECRET_PASS') or '123basab#' #theoretically, any secret key should work here
    UPLOAD_FOLDER= 'uploads'    #uploads here is the folder i am storing the uploaded files
    
    #i prefer using SQLite for my homeserver. so now we define a config for the app & type of database
    SQLALCHEMY_DATABASE_URI= 'sqlite:///site.db' 
    #note: 'sqlite:///site.db' is a relative path btw for the db that'll be instantiated in the same diretry as this api

    