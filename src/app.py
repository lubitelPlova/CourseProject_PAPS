from flask import Flask, request, jsonify, send_file
from SingletonDB import SingletonDB
import pandas as pd

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    login = request.json["login"]
    password = request.json["password"]
    
    print(request.json)

    db = SingletonDB()

    row = db.execute("SELECT * FROM users where login=?", (login,))
    print(row)
    db.close()
    
    if row and row[0][2] == password and row[0][1] != "admin":
        return jsonify({"success": True, "message": "Авторизация успешна", "admin": False})
    elif row and row[0][2] == password and row[0][1] == "admin":
        print("admin log")
        return jsonify({"success": True, "message": "Авторизация успешна", "admin": True})
    else:
        return jsonify({"success": False, "message": "Неправильный пароль", "admin": False})

@app.route("/notifications", methods=["POST"])
def create_notification():
    user_id = request.json["user_id"]
    title = request.json["title"]
    message = request.json["message"]

    print( user_id, title, message)

    db = SingletonDB()
    db.execute("INSERT INTO messages (user_id, title, message) VALUES (?,?,?)", (user_id, title, message))
    db.commit()
    db.close()

    return jsonify({"success": True, "message": "Уведомление создано"}), 201

@app.route("/notifications", methods=["GET"])
def get_notifications():
    user_id = request.args.get("user_id")

    db = SingletonDB()
    rows = db.execute("SELECT * FROM messages WHERE user_id=? ORDER BY created_at DESC", (user_id,))
    notifications = [{"id": row[0], "title": row[2], "message": row[3], "read": row[5]} for row in rows]
    db.close()

    return jsonify({"success": True, "notifications": notifications})

@app.route("/notifications/<int:notification_id>", methods=["GET"])
def get_notification(notification_id):
    db = SingletonDB()
    row = db.execute("SELECT * FROM messages WHERE id=?", (notification_id,))
    if row:
        notification = {"id": row[0], "title": row[2], "message": row[3], "read": row[5]}
        db.close()
        return jsonify({"success": True, "notification": notification})
    else:
        db.close()
        return jsonify({"success": False, "message": "Уведомление не найдено"})

@app.route("/notifications/<int:notification_id>", methods=["PUT"])
def update_notification(notification_id):
    title = request.json.get("title")
    message = request.json.get("message")
    read = request.json.get("read")

    db = SingletonDB()
    if title:
        db.execute("UPDATE messages SET title=? WHERE id=?", (title, notification_id))
    if message:
        db.execute("UPDATE messages SET message=? WHERE id=?", (message, notification_id))
    if read is not None:
        db.execute("UPDATE messages SET read=? WHERE id=?", (read, notification_id))
    db.close()

    return jsonify({"success": True, "message": "Уведомление обновлено"})

@app.route("/notifications/<int:notification_id>", methods=["DELETE"])
def delete_notification(notification_id):
    db = SingletonDB()
    db.execute("DELETE FROM messages WHERE id=?", (notification_id,))
    db.close()

    return jsonify({"success": True, "message": "Уведомление удалено"})

@app.route('/data', methods=['GET'])
def get_data():
    # Получение имени файла из параметра запроса
    filename = request.args.get('filename')
    print(filename)

    # Проверка, что имя файла было передано
    if filename is None:
        return 'Имя файла не было передано', 400

    # Загрузка данных из CSV файла
    try:
        df = pd.read_csv("./data/" + filename)
    except FileNotFoundError:
        return f'Файл {filename} не найден', 404

    PathTo = "data\\" + filename
    # Преобразование данных в формат CSV
    # csv_data = df.to_csv(index=False)

    # Отправка данных в формате CSV
    return send_file(PathTo, mimetype='text/csv', as_attachment=True, download_name=filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)