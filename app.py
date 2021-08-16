from flask import Flask, render_template_string, request   # Importing the Flask modules required for this project
import RPi.GPIO as GPIO     # Importing the GPIO library to control GPIO pins of Raspberry Pi
from time import sleep      # Import sleep module from time library to add delays
GPIO.setwarnings(False)
# Pins where we have connected servos
GPIO.setmode(GPIO.BCM)      # We are using the BCM pin numbering
# Declaring Servo Pins as output pins
GPIO.setup(2, GPIO.OUT)

# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)
# Enable debug mode
app.config['DEBUG'] = True

# Store HTML code
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

# which URL should call the associated function.
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
    # Get slider Values
    GPIO.output(2, GPIO.HIGH)

    return returnPage

@app.route("/turnoff")
def turnoff():
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