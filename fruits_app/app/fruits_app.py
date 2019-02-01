import os
from flask import Flask, render_template
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.debug = True


cwd = os.getcwd()
hostname = os.getenv('HOSTNAME', '')
fruit = os.getenv('FRUIT', 'green-apple')
my_ip = os.getenv('MY_IP', '0.0.0.0')
site = os.getenv('SITE', '')
vault_host = os.getenv('VAULT_URL', None)

@app.route('/')
def index():
  return render_template('index.html', fruit=fruit, hostname=hostname, my_ip=my_ip) 

if __name__ == '__main__':
  # Log http requests
  logging.basicConfig(filename= cwd + '/logs/webapp.log', level=logging.DEBUG)

  if vault_host:
    f = open('static/img/%s.png' % fruit,'wb')
    f.write(urllib.urlopen('http://%s/static/img/%s.png' % (vault_host, fruit)).read())
    f.close()
  # Run the webserver
  app.run(host='0.0.0.0', port=8080, debug=True)
