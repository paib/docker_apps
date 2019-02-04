import os
from flask import Flask, render_template
import logging
import urllib.request
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.debug = True

color = '#262626' #Black
#color = '#4286f4' #Blue
#color = '#33cc33' #Green


cwd = os.getcwd()
hostname = os.getenv('HOSTNAME', '')
image = os.getenv('IMAGE', 'mario')
my_ip = os.getenv('MY_IP', '0.0.0.0')
site = os.getenv('SITE', '')
vault_host = os.getenv('VAULT_HOST', None)

@app.route('/')
def index():

  if vault_host:
    f = open('static/img/%s.png' % image,'wb')
    f.write(urllib.request.urlopen('http://%s/static/img/%s.png' % (vault_host, image)).read())
    f.close()
    return render_template('index.html', image=image, hostname=hostname, my_ip=my_ip, site=site, color=color) 
  return "Image vault not specified"

if __name__ == '__main__':
  # Log http requests
  logging.basicConfig(filename= cwd + '/logs/webapp.log', level=logging.DEBUG)

  # Run the webserver
  app.run(host='0.0.0.0', port=8080, debug=True)
