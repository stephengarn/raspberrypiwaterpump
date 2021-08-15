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
    <h2> Web Application to Control Pump</h2>
        <a href="/test">Turn pump on</a>
    </body>
</html>
'''

# which URL should call the associated function.
@app.route("/")
def home():
    return render_template_string(TPL)

@app.route("/test")
def test():
    returnPage = ''' 
<html>
<h1>motor is running</h1>
<a href="/turnoff">turn pump off</a>
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
<h1>motor is off</h1>
<a href="/">return to turn on</a>
</html>
'''

    return returnPage1


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
