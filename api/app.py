import os
import sys
from flask import Flask, request
from flask_restx import Api, Resource

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts'))

from model.model_all import model_all
from model.model_lite import model_lite
from main import data_predict_all, data_predict_lite

flask_app = Flask(__name__)
app = Api(app = flask_app, 
		  version = '1.0', 
		  title = 'Predict car price', 
		  description = 'Predict the price of a car', 
)

name_space 	= app.namespace('car')

model_all 	= app.model('Car All Model', model_all)
model_lite 	= app.model('Car Lite Model', model_lite)


@name_space.route('/predict/all')
class Predict_all(Resource):

	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }) 
	@app.expect(model_all)		
	def post(self):
		try:
			predict = data_predict_all(request.json['name'], request.json['location'], request.json['year'], request.json['kilometers_driven'], 
                              			request.json['owner_type'], request.json['fuel_type'], request.json['transmission'], request.json['mileage'], 
                                 		request.json['engine'], request.json['power'], request.json['seats'], request.json['new_price'])
			return {
				'status'		: 'True',
				'prediction'	: predict
			}
 
		except KeyError as e:
			name_space.abort(500, e.__doc__, status = 'Could not save information', statusCode = '500')
		except Exception as e:
			name_space.abort(400, e.__doc__, status = 'Could not save information', statusCode = '400')
   
   
@name_space.route('/predict/lite')
class Predict_lite(Resource):

	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' } ) 
	@app.expect(model_lite)		
	def post(self):
  
		try:  
			predict = data_predict_lite(request.json['year'], request.json['engine'], request.json['power'], request.json['new_price'])
			return {
				'status'		: 'True',
				'prediction'	: predict
			}
   
		except KeyError as e:
			name_space.abort(500, e.__doc__, status = 'Could not save information', statusCode = '500')
		except Exception as e:
			name_space.abort(400, e.__doc__, status = 'Could not save information', statusCode = '400')
   
   
if __name__ == '__main__':
	flask_app.run(debug = True, port=5000)