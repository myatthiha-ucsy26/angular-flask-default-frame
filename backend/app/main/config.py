import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']
# change (prod) in production mode, develop mode in (develop)
db_config = 'develop'
generated_img_path = 'dev/generated_images/'
bg_img_path = 'api-images/'
# page size retrieve page size for mentionlists page and lotterylists page
page_size = 3000


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'xyz')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
