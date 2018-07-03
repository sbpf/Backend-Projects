from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/catalogs')
def showCatalogs():
    return "This page will show all my catalogs"

@app.route('/catalog/new')
def newCatalog():
    return "This page will make a new catalog"

@app.route('/catalog/<int:catalog_id>/edit')
def editCatalog(catalog_id):
    return "This page will edit the catalog %s" %catalog_id

@app.route('/catalog/<int:catalog_id>/delete')
def deleteCatalog(catalog_id):
    return "This page will delete the catalog %s" %catalog_id

@app.route('/catalog/<int:catalog_id>')
@app.route('/catalog/<int:catalog_id>/items')
def showItems(catalog_id):
    return "This page will show items of catalog %s" %catalog_id

@app.route('/catalog/<int:catalog_id>/items/new')
def newItem(catalog_id):
    return "This page will create a new item for catalog %s" %catalog_id

@app.route('/catalog/<int:catalog_id>/items/<int:item_id>/edit')
def editItem(item_id,catalog_id):
    return "This page will edit the item %s of catalog %s" %(item_id,catalog_id)

@app.route('/catalog/<int:catalog_id>/items/<int:item_id>/delete')
def deleteItem(catalog_id,item_id):
    return "This page will delete the item %s of catalog %s" %(item_id,catalog_id)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
