from pharmtool import create_app

app = create_app()

# Runs the app in debug mode to allow changes in real time
# __name__ = __main__ if the script is run directly with Python
# If imported from elsewhere, __name__ is the name of the module
if __name__ == '__main__':
    app.run()