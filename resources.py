from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from models import Product, db
from schemas import ProductSchema

class ProductResources(Resource):
    
    product_schema = ProductSchema()
    product_list_schema = ProductSchema(many=True)
    product_patch_schema = ProductSchema(partial=True)
    
    def get(self, product_id=None):
        if product_id:
            product = Product.query.get_or_404(product_id)
            return self.product_schema.dump(product)
        else:
            all_products = Product.query.all()  
            return self.product_list_schema.dump(all_products)
    def post(self):
        try:
           new_product_data =  self.product_schema.load(request.json)
        except ValidationError as err:
            return {"message":"ValidationError", "errors": err.messages}, 400
        
        new_product = Product(
            name=new_product_data['name'],
            description=new_product_data['description'],
            price=new_product_data['price']
            
        )
        db.session.add(new_product)
        db.session.commit()
        return self.product_schema.dump(new_product), 201
    
    def put(self, product_id):
        try:
            product_data = self.product_schema.load(request.json)
        except ValidationError as err:
            return {"message":"ValidationError", "errors": err.messages}, 400
        
        product = Product.query.get_or_404(product_id)
        for key, value in product_data.items():
            if value is not None:
                setattr(product, key, value)
        
        db.session.commit()
        return self.product_schema.dump(product)
    
    def patch(self, product_id):
        try:
            product_data = self.product_patch_schema.load(request.json)
        except ValidationError as err:
            return {"message":"ValidationError", "errors": err.messages}, 400
        
        product = Product.query.get_or_404(product_id)
        for key, value in product_data.items():
            if value is not None:
                setattr(product, key, value)
        
        db.session.commit()
        return self.product_schema.dump(product)
    
    def delete(self, product_id):
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return '', 204