from flask import Flask, render_template, request

app = Flask(__name__)


# Главная страница
@app.route('/')
def index():
    return render_template('main.html')


# Регистрационная страница
@app.route('/register')
def register():
    return render_template('register.html')


# Обработка регистрации
@app.route('/process_register', methods=['POST'])
def process_register():
    # Получаем данные из формы
    username = request.form['username']
    password = request.form['password']

    # Здесь можно выполнить проверку и сохранение данных в базу данных

    # Возвращаем страницу с результатами
    return render_template('result.html', message='Регистрация успешно завершена')


# Обработка данных с формы
@app.route('/process', methods=['POST'])
def process():
    # Получаем данные из формы
    temperature = request.form['temperature']
    humidity = request.form['humidity']

    # Здесь можно выполнить обработку данных и взаимодействие с устройствами умного дома

    # Возвращаем страницу с результатами
    return render_template('result.html', temperature=temperature, humidity=humidity)
