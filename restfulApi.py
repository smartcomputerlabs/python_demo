from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (replace with database interaction in real applications)
items = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'}
]


# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/compound', methods=['POST'])
def compound():
    data = request.get_json()
    ci = data['principal']*data['rate']*data['intrest']
    new_item = {'r': data['principal'], 'p': data['principal']}
    items.append(new_item)
    return jsonify(new_item), 201

# GET a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404


# POST a new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = {'id': len(items) + 1, 'name': data['name']}
    items.append(new_item)
    return jsonify(new_item), 201


# PUT (update) an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        data = request.get_json()
        item['name'] = data['name']
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404


# DELETE an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'})


if __name__ == '__main__':
    app.run(debug=True)