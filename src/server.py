from flask import Flask
import requests
import json 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloworld():
  return 'Hello, World!'


@app.route('/ai', methods=['POST'])
def ai():
  try:
    name = requests.get(url = "https://test1235.azurewebsites.net", params = {'name': 'Maurice'})
    print(name)
    return 'Success'
  except:
    print("an exception occurred")

if __name__ == '__main__':
  app.run(debug=True, port= 3001)