import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.car import Car
from db.car_db import Car_db

class Car_bean :
        
    
    def __init__(self, id=id, name:str=None, location:str=None, year:int=None, kilometers_driven:int=None, 
                 fuel_type:str=None, transmission:str=None, owner_type:str=None, mileage:int=None, 
                 engine:int=None, power:int=None, seats:int=None, new_price:int=None, price:int=None, user_id:int=-1) :
        self.car_db = Car_db()
        self.car    = Car(id=id, name=name, location=location, year=year, kilometers_driven=kilometers_driven, 
                        fuel_type=fuel_type, transmission=transmission, owner_type=owner_type, mileage=mileage, 
                        engine=engine, power=power, seats=seats, new_price=new_price, price=price, user_id=user_id)
        
        
        
        
    def set_car(self, id=id, name:str=None, location:str=None, year:int=None, kilometers_driven:int=None, 
                 fuel_type:str=None, transmission:str=None, owner_type:str=None, mileage:int=None, 
                 engine:int=None, power:int=None, seats:int=None, new_price:int=None, price:int=None, user_id:int=-1) :
        self.car    = Car(id=id, name=name, location=location, year=year, kilometers_driven=kilometers_driven, 
                        fuel_type=fuel_type, transmission=transmission, owner_type=owner_type, mileage=mileage, 
                        engine=engine, power=power, seats=seats, new_price=new_price, price=price, user_id=user_id)
        
        
        
    def form_car(self, car_list) :
        self.car    = Car(id=car_list[0], name=car_list[1], location=car_list[2], year=car_list[3], kilometers_driven=car_list[4], 
                        fuel_type=car_list[5], transmission=car_list[6], owner_type=car_list[7], mileage=car_list[8], 
                        engine=car_list[9], power=car_list[10], seats=car_list[11], new_price=car_list[12], price=car_list[13], user_id=car_list[14])
        
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CRUD car~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
    
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Read One car~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
    
    def select_car_by_id(self, id) :
        car = self.car_db.select_car_by_id(id)
        return self.form_car(car)
    
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Read All car for one user ~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
    
    def select_cars(self, user_id:int='') :
        user_id = user_id if user_id != '' else self.car.user_id
        
        final_cars  = []
        cars        = self.car_db.select_cars(user_id)
        
        for car in cars :
            final_cars.append(self.form_car(car))
        return final_cars
    
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Read All car ~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        
    def select_all(self) :
        return self.car_db.select_all()

    
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Create One car ~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        
    def create_car(self) :
        self.car_db.create_car(self.car)
        
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Update One car ~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        
    def update_car(self) :
        self.car_db.update_car(self.car)
        
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Delete One car ~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        
    def delete_car(self) :
        self.car_db.delete_car(self.car)
        
        
        
    def form_predict_all(self, car='') :
        car = car if car != '' else self.car
        data = {key: car.__dict__[key] for key in ['name', 'location', 'year', 'kilometers_driven', 'owner_type', 'fuel_type',
                                                    'transmission', 'mileage', 'engine', 'power', 'seats', 'new_price']}
        return data


    def form_predict_lite(self, car='') :   
        car = car if car != '' else self.car     
        data = {key: car.__dict__[key] for key in ['year', 'engine', 'power', 'new_price']}        
        return data