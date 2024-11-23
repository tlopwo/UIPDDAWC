from flask import Flask, request, render_template

app = Flask(__name__)

# Strona główna z formularzem
@app.route('/')
def index():
    return render_template('index.html')

# Obsługa danych z formularza
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', 'Guest')  # Pobierz dane z formularza
    return f"<h1>Cześć, {name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')