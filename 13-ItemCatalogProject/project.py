#from flask import Flask, render_template, request, redirect, jsonify, url_for, flask
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

"""
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Travelogue Application"
"""

# Connect to Database and create database session
engine = create_engine('sqlite:///travelogueapp.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

"""
# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)
"""

@app.route('/')
@app.route('/categories')
def showCategories():
    categories = session.query(Category).all()
    return render_template('categories.html',categories = categories)
    
@app.route('/category/new')
def newCategory():
    return "This page will make a new category"

@app.route('/catalog/<int:catalog_id>/edit')
def editCategory(catalog_id):
    return "This page will edit the catalog %s" %catalog_id

@app.route('/catalog/<int:catalog_id>/delete')
def deleteCategory(catalog_id):
    return "This page will delete the catalog %s" %catalog_id

@app.route('/catalog/<int:catalog_id>')
@app.route('/catalog/<int:catalog_id>/items')
def showItems(catalog_id):
    return "This page will show items of catalog %s" %catalog_id

@app.route('/catalog/<int:catalog_id>/items/new')
def newItem(catalog_id):
    return "This page will create a new item for catalog %s" %catalog_id

@app.route('/catalog/<int:catalog_id>/items/<int:item_id>')
def displayItem(catalog_id,item_id):
    return "This page will diplay item %s of catalog %s" %(item_id,catalog_id)

@app.route('/catalog/<int:catalog_id>/items/<int:item_id>/edit')
def editItem(item_id,catalog_id):
    return "This page will edit the item %s of catalog %s" %(item_id,catalog_id)

@app.route('/catalog/<int:catalog_id>/items/<int:item_id>/delete')
def deleteItem(catalog_id,item_id):
    return "This page will delete the item %s of catalog %s" %(item_id,catalog_id)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
