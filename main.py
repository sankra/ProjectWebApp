from website import create_app

app = create_app()

if __name__ == '__main__': #this will restrict the main.py run as module imported into another program.
#if main.py run as a script the condition will pass and block will be executed. 
#but if this main.py imported into another program this will not work
    app.run(debug=True) #this line will run our flask application