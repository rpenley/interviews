#!/usr/bin/python3

from dotenv import load_dotenv
from flask import Flask
import os
import requests

load_dotenv()

GITHUB_KEY = os.getenv('GITHUB_KEY')
GITHUB_ENDPOINT = 'https://api.github.com'

app = Flask(__name__)

@app.route('/')
def get():
	return 'GitHub Wrapper API'

@app.route('/zen')
def get_zen():
	response = requests.get(GITHUB_ENDPOINT + '/zen')
	response.close
	return response.text

@app.route('/users/<user>')
def get_user(user):
	response = requests.get(GITHUB_ENDPOINT + '/users/' + user)
	response.close()
	return response.json()

@app.route('/users/<user>/orgs')
def get_user_org(user):
	response = requests.get(GITHUB_ENDPOINT + '/users/' + user + '/orgs')
	response.close()
	return response

if __name__ == '__main__':
	app.run()
