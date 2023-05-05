"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa14ak728r8860n02g-a.oregon-postgres.render.com",
        database="todo_x37f",
        user="todo_x37f_user",
        password="9vRbvS0BWlyEF3aNnQWrneSsrgQZxeeT")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
