from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Function to get the latest message
def get_latest_message():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("SELECT text FROM messages ORDER BY created_at DESC LIMIT 1")
    message = cursor.fetchone()
    conn.close()
    return message[0] if message else "No message yet! Upload one."

# Homepage route
@app.route("/")
def home():
    message = get_latest_message()
    return render_template("index.html", message=message)

# Upload page route
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        message = request.form.get("message")
        if message:
            conn = sqlite3.connect("messages.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO messages (text) VALUES (?)", (message,))
            conn.commit()
            conn.close()
        return redirect("/")
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
