

class Car():
    

    def __init__(self, id:int=None, name:str=None, location:str=None, year:int=None, kilometers_driven:int=None, 
                 fuel_type:str=None, transmission:str=None, owner_type:str=None, mileage:int=None, 
                 engine:int=None, power:int=None, seats:int=None, new_price:int=None, price:int=None, user_id:int=-1) :
        
        self.id                    = id     
        self.name                  = name
        self.location              = location
        self.year                  = year
        self.kilometers_driven     = kilometers_driven
        self.owner_type            = owner_type
        self.fuel_type             = fuel_type
        self.transmission          = transmission
        self.mileage               = mileage
        self.engine                = engine
        self.power                 = power
        self.seats                 = seats
        self.new_price             = new_price
        self.price                 = price       
        self.user_id               = user_id