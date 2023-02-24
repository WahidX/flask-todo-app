from flask import Flask, request, abort
from todos import todoStorage
from Todo import Todo


app = Flask(__name__)

count = 0

@app.route("/")
def get_todos():
    out = []
    for t in todoStorage:
        out.append(t.__dict__)
    
    return out


@app.route("/create", methods=["POST"])
def create_todo():
    data = request.json
    content = data.get('content')
    if not content:     # returning 400 if the content is blank
        abort(400)

    t = Todo(content)
    todoStorage.append(t)
    
    return {
        "created": t.__dict__
    }


@app.route("/update", methods=["PUT"])
def update_todo():
    data = request.json
    upd_id = data.get('id')

    if not upd_id:  # returning 400 if the id not present
        abort(400)

    for i in range(len(todoStorage)):
        if todoStorage[i].id == upd_id:
            if data.get('content'):
                todoStorage[i].content = data.get('content')

            if data.get('done'):
                todoStorage[i].done = data.get('done')

            return {
                "updated": todoStorage[i].__dict__
            }

    return {
        "error": "invalid id"
    }


@app.route("/delete", methods=["DELETE"])
def delete_todo():
    id = request.args.to_dict().get("id")
    if not id:  # returning 400 if the id not present
        abort(400)

    for i in range(len(todoStorage)):
        if str(todoStorage[i].id) == id:
            todoStorage.pop(i)

            return {
                "message":"deleted successfully"
            }
    
    return {
        "message": "invalid id"
    }