import os



##------------------------------------Connection DB------------------------------------##

##-----------------MySQL-----------------##

host                        = "localhost"
user                        = "admin"
password                    = "root"
database                    = "price_project"

connect_db_mysql            = "mysql://{}:{}@{}/{}".format(user, password, host, database)

user_table_name            = "users"
car_table_name             = "cars"

##------------------------------------Config Model------------------------------------##

##-----------------Path to the model-----------------##

model_path                  = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), 'data')

model_all_path              = os.path.join(model_path, 'dt_smote.pkl')

model_simple_path           = os.path.join(model_path, 'dt_simple.pkl')




url_api             = 'http://127.0.0.1:5000/car'

url_predict_lite    = url_api + '/predict/lite'

url_predict_all     = url_api + '/predict/all'


columns_model_all   =  ['name', 'location', 'year', 'kilometers_driven', 'owner_type', 'fuel_type',
                      'transmission', 'mileage', 'engine', 'power', 'seats', 'new_price']


columns_model_lite  =  ['year', 'engine', 'power', 'new_price']


post_headers = { 'Content-type': 'application/json', 'Accept' : 'application/json'}
