from flask import Flask
from public import public
from admin import admin
from police import police
from user import user
app=Flask(__name__)

app.secret_key='key'
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(police,url_prefix="/police")
app.register_blueprint(user,url_prefix="/user")


app.run(debug=True,port=5675)