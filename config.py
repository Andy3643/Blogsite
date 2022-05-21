import os
class Config:

    SECRET_KEY = 'secretkey1'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:pass123@localhost/personalblog'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
    #mail cconfiguration
    MAIL_SERVER= 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS=True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD= os.environ.get("MAIL_PASSWORD")
   
    
class ProdConfig(Config):
    DEBUG = False
    
class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    
    
class TestingConfig(Config):
    TESTING = True


config_options = {
'test':TestingConfig,
'development':DevConfig,
'production':ProdConfig
}