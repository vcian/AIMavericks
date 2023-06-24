from flask import Flask, request

app = Flask(__name__)

from aimavericks.api.module import send
