from flask import Flask
from models import db, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

db.init_app(app)

with app.app_context():
    
    try:
        db.drop_all()
        db.create_all()
        
        chaussure = Product(name='chaussure', description='chaussures de sport', price=145.85)
        jogging = Product(name='jogging', description='jogging de sport', price=54.99)
        
        db.session.add(chaussure)
        db.session.add(jogging)
        db.session.commit()
        
        chaussure_db = db.session.query(Product).filter(Product.name == 'chaussure').first()
        jogging_db = db.session.query(Product).filter(Product.name == 'jogging').first()
        print(f"{chaussure_db.id}: {chaussure_db.name} - {chaussure_db.description} seulement {chaussure_db.price}€")
        print(f"{jogging_db.id}: {jogging_db.name} - {jogging_db.description} seulement {jogging_db.price}€")
        
        app.run()
    except Exception as e:
        print(e)
        db.session.rollback()
    
    