import os
# bad imports
import sys
from typing import List
from typing import Tuple

from flask import Flask, request
app = Flask(__name__)

non_used_list = []
always_none = non_used_list.append("1")

non_used_list = []
always_none = [].append("2")

try:
  1/0
except:
  print("meaningless try/catch")

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/badcode1')
def bad_code_one(param=None):
    if param:
        return os.system('ls -l ' + param)
    else:
        return os.system('ls -l')

@app.route('/badcode2')
def bad_code_two():
    cmd = request.args.get('cmd', 'echo "blah"')
    return os.system(cmd)

@app.route('/badcode3')
def bad_code_three():
    cmd = request.args.get('cmd', 'echo "blah"')
    return os.system(cmd)

def duplicated_name():
  pass

def duplicated_name():
  print('duplicated name')

if __name__ == '__main__':
    app.run()
