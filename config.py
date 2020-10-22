import os
from dotenv import load_dotenv
load_dotenv()


class Config(object):
    RECIPE_URL = os.getenv('RECIPE_URL')
    RECIPE_KEY = os.getenv('RECIPE_KEY')
    IMAGE_URL = os.getenv('IMAGE_KEY')
    IMAGE_CONSTRUCT = os.getenv('IMAGE_CONSTRUCT')
    IMAGE_KEY = os.getenv('IMAGE_KEY')
