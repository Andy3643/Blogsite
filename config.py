import os
class Config:

    SECRET_KEY = 'secretkey1'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:pass123@localhost/personalblog'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
   
    
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