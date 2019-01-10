from flask import Flask

#This creates a Flask application, which we name ‘application’. 
# This is an important requirement — Amazon Elastic Beanstalk will look for 
# an object named ‘application’ in the file ‘application.py’.
application = Flask(__name__)

#set debug to True, so if there is an error, the error will be displayed in the browser. 
# We wouldn’t want to do this in production, as it could enable a hacker to discover
#  the internal workings of our application. However, during development it’s 
# useful to see the error messages.
application.debug = True

#Flask decorator. It says, if the user goes to the “/” URL of your website 
# (in other words the homepage) then run the next 2 lines
@application.route('/', methods=['GET'])
def hello():
 return '<p>Hello world</p>'

# initialise the Flask application.
if __name__ == "__main__":
 application.run()