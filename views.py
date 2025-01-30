from flask import Blueprint

views= Blueprint('views',__name__)

@views.route('/')
def home():
    return " <h1> Home Page hello</h1>"
	
def kompa():
	retrun "adhirindhi"