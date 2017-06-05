# project/config.py

class BaseConfig:
    """Configuração Base"""
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Configuração de Desenvolvimento"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Configuração de Teste"""
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """Configuração de Produção"""
    DEBUG = False
