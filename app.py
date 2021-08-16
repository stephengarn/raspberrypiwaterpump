# import all necessary libraries 
from flask import Flask, render_template_string, request
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
# BCM GPIO vs BOARD GPIO. We are using BCM here. 
GPIO.setmode(GPIO.BCM)      
# Pin where the relay is connected to
GPIO.setup(2, GPIO.OUT)

# flask constructer 
app = Flask(__name__)
# Enable debug mode (this is optional, but useful if your application is having problems)
app.config['DEBUG'] = True

# let's create a variable to store the HTML
TPL = '''
<html>
    <head><title>Web Application to control air conditioner water relief pump</title></head>
    <body>
    <h1 style='text-align:center;font-family:arial;'> Web Application to Control Pump</h1>
        <div style='text-align:center;'>
        <a href="/run" style='font-size:20px; font-family: arial;'>Turn pump on</a></div>
    </body>
</html>
'''

# Flask uses routing to navigate where the HTTP requests shall go
@app.route("/")
def home():
    return render_template_string(TPL)

@app.route("/run")
def run():
    returnPage = ''' 
<html>
<h1 style='text-align:center;font-family:arial;'>motor is running</h1>
<div style='text-align:center;'>
<a href="/turnoff" style='font-size:20px; font-family: arial;'>turn pump off</a></div>
</html>
'''
    # turns water pump on
    GPIO.output(2, GPIO.HIGH)

    return returnPage

@app.route("/turnoff")
def turnoff():
    #turns pump off
    GPIO.output(2, GPIO.LOW)
    returnPage1 = '''
<html>
<h1 style='text-align:center;font-family: arial;'>motor is off</h1>
<div style='text-align:center;'>
<a href="/" style='font-size:20px; font-family: arial;'>return to turn on</a></div>
</html>
'''

    return returnPage1

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')