class Config():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://<root>:pass@localhost/database_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False