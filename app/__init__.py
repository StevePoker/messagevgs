# урок по статье
# https://habr.com/ru/post/346306/
from flask import Flask
# from config import Config

app = Flask(__name__)
# app.config.from_object(Config)

from app import routes
