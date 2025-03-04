from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# MySQL configuration - replace with your Render credentials
app.config['MYSQL_HOST'] = '193.39.187.202'  # Your host
app.config['MYSQL_USER'] = 'u236_tQbKjxlgPq'  # Your username
app.config['MYSQL_PASSWORD'] = 'FFiKOh^w7h7x7s9c.z=Pj0JC'  # Your password
app.config['MYSQL_DB'] = 's236_DONOTTOUCH'  # Your database name

mysql = MySQL(app)

# Route to display the latest message
@app.route("/")
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM messages ORDER BY created_at DESC LIMIT 1")
    message = cur.fetchone()
    return render_template("index.html", message=message[1] if message else "No message yet!")

# Route to upload a new message
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        message_text = request.form.get("message")
        if message_text:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO messages (text) VALUES (%s)", [message_text])
            mysql.connection.commit()
            cur.close()
        return redirect("/")
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
