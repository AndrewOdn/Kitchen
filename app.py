from flask import Flask, render_template, request, redirect
import sqlite3 as sql
from sql import create_tables

app = Flask(__name__)
create_tables()


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/register')
def register():
    return redirect('/auth')


@app.route('/auth')
def auth():
    return render_template('auth.html')


@app.route('/panel')
def panel():
    return redirect('/')
    # return render_template('panel.html')


@app.route('/state')
def state():
    return redirect('/')
    # return render_template('panel.html')


@app.route('/policy')
def policy():
    return redirect('/')
    # return render_template('policy.html')


@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/process_register', methods=['POST'])
def process_register():
    username = request.form['username']
    password = request.form['password']

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO users (username,password) VALUES(?, ?)", (username, password))

        con.commit()

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
