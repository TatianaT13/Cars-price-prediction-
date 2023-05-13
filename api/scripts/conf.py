import os

path_data           = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

path_dataset        = os.path.join(path_data, 'dataset.csv')

path_target         = os.path.join(path_data, 'com/target.pkl')


path_data_all       = os.path.join(path_data, 'all')

path_data_lite      = os.path.join(path_data, 'lite')

columns_model_all   =  ['Name', 'Location', 'Year', 'Kilometers_Driven', 'Owner_Type', 'Fuel_Type',
                      'Transmission', 'Mileage', 'Engine', 'Power', 'Seats', 'New_Price']


columns_model_lite  =  ['Year', 'Engine', 'Power', 'New_Price']