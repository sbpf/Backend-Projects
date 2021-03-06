from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def displayRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)

    output = ''
    output += 'Restaurant: ' + restaurant.name + '</br></br>'
    for i in items:
        output += i.name + '</br>'
        output += i.price + '</br>'
        output += i.description + '</br>'
        output += '</br>'
    return output    

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port = 5000)
