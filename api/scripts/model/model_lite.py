from flask_restx import fields


model_lite = {
				"year"                 : fields.Integer(required = True, 
													description="Year of release of the car", 
													help="Year cannot be blank."),
				"engine"               : fields.Integer(required = True, 
													description="Engine of the car", 
													help="Engine cannot be blank."),
				"power"                : fields.Float(required = True, 
													description="Power of the car", 
													help="Power cannot be blank."),
				"new_price"            : fields.Float(required = True, 
													description="Price of a new car", 
													help="Price cannot be blank."),
            }