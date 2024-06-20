from flask_restful import Resource

from models import Product
from schemas import ProductSchema

class ProductResources(Resource):
    
    product_schema = ProductSchema()
    product_list_schema = ProductSchema(many=True)
    
    def get(self, product_id=None):
        if product_id:
            product = Product.query.get_or_404(product_id)
            return self.product_schema.dump(product)
        else:
            all_products = Product.query.all()  
            return self.product_list_schema.dump(all_products)
     