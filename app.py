from flask import Flask, render_template_string, request, redirect, session
import secrets
import os

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

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

# Corrected route for birthday card
@app.route('/birthday_card')
def birthday_card():
    return "Your Birthday Card Content"

# Render provides a PORT environment variable, use it
PORT = int(os.environ.get("PORT", 10000))  # Default to 10000 if not set

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
