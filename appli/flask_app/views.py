import os
import sys
import json
import requests
from flask import Flask, render_template, request

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from scripts.controller.car_bean import Car_bean
from scripts.controller.user_bean import User_bean


app = Flask(__name__)


car_bean    = Car_bean()
user_bean   = User_bean()


@app.route('/')
def login():    
    return render_template('login.html')


@app.route('/', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    if user_bean.connect(username, password) :
        return render_template('predict_lite.html')
    else :
        return render_template('login.html')
    
@app.route('/logout')
def logout():
    user_bean.destruct_user()
    return render_template('login.html')


@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')


@app.route('/subscribe', methods=['POST'])
def subscribe_post():
    username = request.form['username']
    password = request.form['password']
    if not user_bean.is_exist(username=username) :
        user_bean.set_user(username=username, password=password)        
        user_bean.create_user()
        return render_template('predict_lite.html', username=username)
    else :
        return render_template('subscribe.html', error='Error username already exist !')


@app.route('/predict_all')
def predict_all():
    if user_bean.user.username == '' :
        return login()
    else :
        return render_template('predict_all.html')


@app.route('/predict_all', methods=['POST'])
def predict_all_post():
    name                = request.form['Name']
    location            = request.form['Location']
    year                = request.form['Year']
    kilometers_driven   = request.form['Kilometers_Driven']
    owner_type          = request.form['Owner_Type']
    fuel_type           = request.form['Fuel_Type']
    transmission        = request.form['Transmission']
    mileage             = request.form['Mileage']
    engine              = request.form['Engine']
    power               = request.form['Power']
    seats               = request.form['Seats']
    new_price           = request.form['New_Price']
    
    car_bean.set_car(name=name, location=location, year=year, kilometers_driven=kilometers_driven, owner_type=owner_type,
                     fuel_type=fuel_type, transmission=transmission, mileage=mileage, engine=engine, power=power, seats=seats, new_price=new_price, user_id=user_bean.user.id)
    data = car_bean.form_predict_all()
    
    
    y_pred = requests.post('http://127.0.0.1:5000/car/predict/all', data=json.dumps(data), headers={ 'Content-type': 'application/json', 'Accept' : 'application/json'}).json()
    
    car_bean.car.price = y_pred['prediction']
    car_bean.create_car()
    
    return render_template('result.html', predict=y_pred['prediction'])


@app.route('/predict_lite')
def predict_lite():
    if user_bean.user.username == '' :
        return login()
    else :        
        return render_template('predict_lite.html')


@app.route('/predict_lite', methods=['POST'])
def predict_lite_post():
    year        = request.form['Year']
    engine      = request.form['Engine']
    power       = request.form['Power']
    new_price   = request.form['New_Price']
    
    car_bean.set_car(year=year, engine=engine, power=power, new_price=new_price)
    data = car_bean.form_predict_lite()
    
    
    y_pred = requests.post('http://127.0.0.1:5000/car/predict/lite', data=json.dumps(data), headers={ 'Content-type': 'application/json', 'Accept' : 'application/json'}).json()
    
    return render_template('result.html', predict=y_pred['prediction'])


@app.route('/analysis')
def analysis():
    return render_template('analysis.html')


if __name__ == '__main__':
	app.run(debug = True, port=8000)