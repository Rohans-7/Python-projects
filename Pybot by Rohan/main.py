import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from src.pythonREPL import execute_python, install_package
import src.services as services
app=Flask(__name__)
@app.route('/bot',methods=['POST'])

def bot():
    incoming_msg=request.values.get('Body','').strip()
    print(incoming_msg)
    resp=MessagingResponse()
    msg=resp.message()
    isPythonCode=False

    if incoming_msg.startswith('#!python3'):
        code=incoming_msg.strip('#!python3')
        output=execute_python(code)
        msg.body(output)
        isPythonCode=True
    elif incoming_msg.startswith('!pip install'):
        package=incoming_msg.split()[-1]
        output=install_package(package)
        msg.body(output)
        isPythonCode=True
    if isPythonCode:
        return str(resp)
    incoming_msg=incoming_msg.lower()
    if 'your name' in incoming_msg:
        output='Hi I am Pybot created by Rohan'
    elif 'your age' in incoming_msg:
        output='My age is less than a year'
    elif 'joke' in incoming_msg:
        output=services.get_joke()
    msg.body(output)
    return str(resp)


if __name__=='__main__':
    app.run()
