

class ApplicationConfig(object):
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'rorring'
    PYMODM_HOST = 'mongodb://localhost:27017/rorring'
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6378


class DevelopmentConfig(ApplicationConfig):
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'rorring'
    PYMODM_HOST = 'mongodb://localhost:27017/rorring'
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6378



class ProductionConfig(ApplicationConfig):
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'rorring'
    PYMODM_HOST = 'mongodb://localhost:27017/rorring'
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6378



class TestConfig(ApplicationConfig):
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'rorring_test'
    PYMODM_HOST = 'mongodb://localhost:27017/rorring_test'
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6378


