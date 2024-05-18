import jwt, datatime, os
from flask import Flask, request
from flask_mysqldb import MySQL
server = Flask(__name__)
mysql = MySQL(server)


#config

sever.config["MYSQL_HOTS"] = os.environ.get("MYSQL_HOTS")
sever.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
sever.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
sever.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
sever.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")


@server.route("/login", methods=["POST"])
def login():
    auth= request.authorization
    if not auth:
        return"missing credentials",401
    
    #check db for username and password 