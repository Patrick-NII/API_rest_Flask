from flask_marshmallow import Marshmallow

from models import Product

ma = Marshmallow()

class ProductSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = Product