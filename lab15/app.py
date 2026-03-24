"""
Muhammad Zhaoor
March 24, 2026
lab 15: RESTful API and unit test in a flask app
"""
from flask import Flask, request,jsonify, render_template

app = Flask(__name__)

# in-memory database (dictionary)
items ={}

@app.route('/')
def home():
    return render_template('index.html')

#CReate an item
@app.route('/items', methods = ['POST'])
def create_item():
    # get_json method is used to read JSON data sent by the client in a  http request
    data = request.get_json()

    # generate a new unique id for thge new item
    item_id = str(len(items)+1)

    # add the data collected for the new item
    items[item_id] = data

    #jsonify converts a python dictionary into a json response
    return jsonify({'id':item_id,'item': data}), 201

# READ ALL ITEMS
@app.route('/items', methods =['GET'])
def get_items():
    return jsonify(items)

    #READ single item
    @app.route('/items/<items_id>', method=['GET'])
    def get_oneitem(item_id):
        item = items.get(item_id)
        if not item:
            # 404 = server is reacheable but the item you asked for doesnt exist
            return jsonify({'Error':"Item not found"}), 404

            return jsonify(item)

if __name__ == '__main__':
    app.run(debug=True)