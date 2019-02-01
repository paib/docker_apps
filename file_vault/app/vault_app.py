import os
from flask import Flask, render_template
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.debug = True


cwd = os.getcwd()



@app.route('/')
def index():
  return 'Simple vault app for files and images'

if __name__ == '__main__':
  # Log http requests
  logging.basicConfig(filename= cwd + '/logs/webapp.log', level=logging.DEBUG)

  # Run the webserver
  app.run(host='0.0.0.0', port=8080, debug=True)
