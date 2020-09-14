import os


class Config:
    """Common configurations for the project modules."""

    DEBUG = True
    TEST = False


class LocalConfig:
    """Configuration for debugging purposes."""

    DEBUG = True
    TEST = False

    POSTGRESQL_DB_NAME = "irithm"
    POSTGRESQL_DB_HOST = "127.0.0.1"
    POSTGRESQL_DB_PORT = "5432"
    POSTGRESQL_DB_USERNAME = "postgres"
    POSTGRESQL_DB_PASSWORD = "password"

    API_SECRET_KEY = "API_SECRET_KEY"


class TestConfig(LocalConfig):
    """Configuration for unit testing purposes"""

    TEST = True


class DevelopmentConfig(Config):
    """Development configurations"""

    DEBUG = True


class StagingConfig(Config):
    """Staging configurations"""

    DEBUG = False


class ProductionConfig(Config):
    """Production ready configurations"""

    DEBUG = False


def get_config(config_name=None):
    if not config_name:
        config_name = os.getenv("APP_ENV", "default")

    return {
        "local": LocalConfig,
        "test": TestConfig,
        "development": DevelopmentConfig,
        "staging": StagingConfig,
        "production": ProductionConfig,
        "default": LocalConfig,
    }.get(config_name)
