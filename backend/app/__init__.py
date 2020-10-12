import os
import requests
import random

from flask import Flask
from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)

@app.route('/')
def default():
    return 'aaaaaWelcome to the blockchain world!!!!'

@app.route('/blockchain')
def route_blockchain():
    return 'this is the datas of the blockchain.'

app.run()












