from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/config', methods=['GET', 'POST'])
def config():
  return render_template('config.html',  data = read_Sensors())
  
@app.route('/download/<string:table>', methods = ['POST'])
def download(table):
  with open("Docker_Servidor\config\RaspConfig.json", "w") as fo:
    fo.write(table)
    fo.close()
  return ('/')

@app.route('/remove', methods = ['GET'])
def remove():
  with open("Docker_Servidor\config\RaspConfig.json", "w") as fo:
    fo.write("[]")
    fo.close()
  return ('/')

def read_Sensors():
    f = open("Docker_Servidor\config\RaspConfig.json","r")
    return  json.load(f)


if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug=True)
