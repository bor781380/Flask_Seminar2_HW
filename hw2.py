# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет
# создан cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия,
# где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с
# данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, request, make_response, render_template, session, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        response = make_response(redirect('/welcome'))
        response.set_cookie('user_name', name)
        response.set_cookie('user_email', email)
        return response
    return render_template('index.html')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    user_name = request.cookies.get('user_name')
    if not user_name:
        return redirect('/')

    if request.method == 'POST':
        response = make_response(redirect('/'))
        response.delete_cookie('user_name')
        response.delete_cookie('user_email')
        return response

    return render_template('welcome.html', user_name=user_name)


if __name__ == '__main__':
    app.run('0.0.0.0', port= 5000, debug=True)