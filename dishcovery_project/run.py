# Starts the Flask application.
# This file is kept small so most of the project logic stays inside the app folder.

from app import create_app
app=create_app()
if __name__=="__main__": app.run(debug=True)
