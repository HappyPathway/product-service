from flask import Flask
from flask import jsonify
from pymongo import MongoClient

import os

DB_ADDR = 'DB_ADDR'
DB_PORT = 'DB_PORT'
DB_USER = 'DB_USER'
DB_PW = 'DB_PW'

#DB_NAME = 'bbthe90s'
#COL_NAME = 'products'
DB_NAME = 'DB_NAME'
COL_NAME = 'COL_NAME'

PRODUCT_PORT = 'PRODUCT_PORT'

def connect_to_db():
    db_addr = os.environ.get(DB_ADDR)
    db_port = int(os.environ.get(DB_PORT))
    db_username = os.environ.get(DB_USER)
    db_pw = os.environ.get(DB_PW)
    db_name = os.environ.get(DB_NAME)
    col_name = os.environ.get(COL_NAME)


    if not db_addr or not db_port:
        # try default connection settings
        client = MongoClient()
    else:
        client = MongoClient(db_addr, db_port)
    return client

db_client = connect_to_db()

app = Flask(__name__)

# these can be seeded into the DB for testing if necessary
prods = [{ 'inv_id': 1, 'name':'jncos', 'cost':35.57, 'img':None},
         { 'inv_id': 2, 'name':'denim vest', 'cost':22.50, 'img':None},
         { 'inv_id': 3, 'name':'pooka shell necklace', 'cost':12.37, 'img':None},
         { 'inv_id': 4, 'name':'shiny shirt', 'cost':17.95, 'img':None}]

@app.route("/product", methods=['GET'])
def get_products():
    res = get_products_from_db()
    return jsonify(res)

def get_products_from_db():
    return [rec for rec in db_client[DB_NAME][COL_NAME].find({}, {'_id': False})]

if __name__ == '__main__':
    PORT = os.environ.get(PRODUCT_PORT)
    app.run(host='127.0.0.1', port=PORT)