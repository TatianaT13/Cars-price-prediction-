import os
import sys
import mysql.connector

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common import conf


class Car_db :
        
    def __init__(self) :
        self.db = mysql.connector.connect(
            host      = conf.host,
            user      = conf.user,
            password  = conf.password,
            database  = conf.database
        )
            
        self.cursor = self.db.cursor(buffered=True)
        
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CRUD car~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
    
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Read One car~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
    
    def select_car_by_id(self, id) :
        request = "SELECT * FROM {} WHERE car_id = '{}'".format(conf.car_table_name, id)
        self.cursor.execute(request)
        return self.cursor.fetchone()
    
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Read All car for one user ~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
    
    def select_cars(self, user_id) :
        request = "SELECT * FROM {} WHERE user_id = '{}'".format(conf.car_table_name, user_id)
        self.cursor.execute(request)
        return self.cursor.fetchall()    
   
    
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Read All car~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
    
    def select_all(self) :
        request = "SELECT * FROM {}".format(conf.user_table_name)        
        self.cursor.execute(request)
        return self.cursor.fetchall()
    
    
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Create One car~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
    
    def create_car(self, car) :
        request = """INSERT INTO {} (name, location, year, kilometers_driven, owner_type, fuel_type, transmission, 
                        mileage, engine, power, seats, new_price, price, user_id) 
                        VALUES ('{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', 
                        '{}', '{}', '{}', '{}', '{}')""".format(conf.user_table_name, car.name, car.location, 
                                                                        car.year, car.kilometers_driven, car.owner_type, car.fuel_type, 
                                                                        car.transmission, car.mileage, car.engine, car.power, car.seats, 
                                                                        car.new_price, car.price, car.user_id)        
        self.cursor.execute(request)    
        self.db.commit()
        
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Update One car~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        
    def update_car(self, car) :
        request = """UPDATE {} SET name = '{}', location = '{}', year = '{}', kilometers_driven = '{}', owner_type = '{}', 
                                    fuel_type = '{}', transmission = '{}', mileage = '{}', engine = '{}', power = '{}', seats = '{}', 
                                    new_price = '{}', price = '{}', user_id = '{}' WHERE car_id = '{}'""".format(conf.user_table_name, car.name, car.location, 
                                                                                                                car.year, car.kilometers_driven, car.owner_type, car.fuel_type, 
                                                                                                                car.transmission, car.mileage, car.engine, car.power, car.seats, 
                                                                                                                car.new_price, car.price, car.user_id, car.car_id)
        self.cursor.execute(request)
        self.db.commit()
        
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Delete One car~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        
    def delete_car(self, car) :
        request = "DELETE FROM {} WHERE id = '{}'".format(conf.user_table_name, car.id)

        self.cursor.execute(request)
        self.db.commit()
