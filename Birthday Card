from flask import Flask, render_template_string, request, redirect, session
import secrets
import os

app = Flask(Bortday_Card.py)
app.secret_key = secrets.token_hex(16)

# Set the PORT dynamically for Render deployment
PORT = int(os.environ.get("PORT", 10000))

initial_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome!</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Montserrat', 'Times New Roman', serif;
            text-align: center;
            background: linear-gradient(45deg, #004d4d, #008080);
            padding: 20px;
            margin: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .form {
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            max-width: 400px;
            width: 90%;
        }
        input {
            width: 80%;
            padding: 10px;
            margin: 10px 0;
            border: 2px solid #90EE90;
            border-radius: 5px;
            font-size: 16px;
        }
        .btn {
            background-color: #90EE90;
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 15px;
        }
        .btn:hover {
            background-color: #32CD32;
        }
    </style>
</head>
<body>
    <div class="form">
        <h2>✨ Welcome to a Special Surprise! ✨</h2>
        <form action="/check-initial" method="post">
            <input type="text" name="name" placeholder="Your name" required><br>
            <input type="text" name="color" placeholder="Favorite color" required><br>
            <button class="btn" type="submit">✨ Enter ✨</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    session.clear()
    return render_template_string(initial_template)

@app.route('/check-initial', methods=['POST'])
def check_initial():
    name = request.form.get('name')
    if name.lower() != 'ysai':
        return "<h1>🚨 Intruder Alert! 🚨</h1><p>Only Ysai can enter! Go back.</p>"
    session['passed_initial'] = True
    return "<h1>✅ Welcome, Ysai! Now verify your sport.</h1><form action='/verify' method='post'><input type='text' name='sport'><button type='submit'>Submit</button></form>"

@app.route('/verify', methods=['POST'])
def verify():
    if not session.get('passed_initial'):
        return redirect('/')
    sport = request.form.get('sport')
    if sport.lower().strip() == 'volleyball':
        session['verified'] = True
        return "<h1>🎉 Happy Birthday, Ysai! 🎉</h1><p>Enjoy your surprise!</p>"
    return "<h1>🚨 Intruder Alert! 🚨</h1><p>Only Ysai can enter! Go back.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
