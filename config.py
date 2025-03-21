import os

class Config:
    DEBUG = os.getenv("DEBUG", True)

class ProductionConfig(Config):
    DEBUG = False