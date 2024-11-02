from flask import Flask, request, jsonify
from SingletonDB import SingletonDB

app = Flask(__name__)



@app.route("/login", methods=["POST"])
def login():
    login = request.json["login"]
    password = request.json["password"]
    
    print(request.json)

    db = SingletonDB()

   

    row = db.execute("SELECT * FROM users where login=?", (login,))
    print(row)
    
    if row and row[2] == password:
        return jsonify({"success": True, "message": "Авторизация успешна"})
    else:
        return jsonify({"success": False, "message": "Неправильный логин или пароль"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)