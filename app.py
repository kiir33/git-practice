from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.json.get('todo')
    if todo:
        todos.append(todo)
        return jsonify({'message': 'Todo added successfully!'}), 201
    return jsonify({'message': 'Todo is required!'}), 400

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        deleted_todo = todos.pop(todo_id)
        return jsonify({'message': 'Todo deleted successfully!', 'todo': deleted_todo}), 200
    return jsonify({'message': 'Todo not found!'}), 404

if __name__ == '__main__':
    app.run(debug=True)
