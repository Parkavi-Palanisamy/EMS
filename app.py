from flask import Flask, render_template, psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

    conn = psycopg2.connect(
        host="your-host",
        database="postgres",
        user="postgres",
        password="your-password"
    )


    @app.route("/")
    def home():
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees")
        data = cur.fetchall()
        return str(data)

    app.run()

    conn = psycopg2.connect(
        host="YOUR_HOST",
        database="postgres",
        user="postgres",
        password="YOUR_PASSWORD",
        port="5432"
    )


    @app.route("/")
    def home():
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees")
        data = cur.fetchall()
        cur.close()
        return render_template("index.html", employees=data)


    if __name__ == "__main__":
        app.run(debug=True)

from db import conn, cursor

cursor.execute("SELECT * FROM users")
data = cursor.fetchall()

print(data)
