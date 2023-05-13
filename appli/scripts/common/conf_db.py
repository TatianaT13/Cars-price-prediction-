import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from flask_app.views import app



##------------------------------------Connection DB------------------------------------##

##-----------------MySQL-----------------##

host                        = "localhost"
user                        = "admin"
password                    = "root"
database                    = "price_project"

connect_db_mysql            = "mysql://{}:{}@{}/{}".format(user, password, host, database)


app.config["SQLALCHEMY_DATABASE_URI"] = connect_db_mysql

app.app_context().push()