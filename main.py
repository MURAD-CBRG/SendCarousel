from flask import Flask, render_template, request
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'INFORMATION_SECURITY'


@app.route('/carousel', methods=['GET', 'POST'])
def carousel_func():
    if request.method == 'GET':
        params = {
            'title': 'ИНФОРМАЦИОННАЯ БЕЗОПАСНОСТЬ',
            'data': list(filter(lambda x: x != '1.png', os.listdir('static/img')))
        }

        return render_template('info_sec.html', params=params)
    elif request.method == 'POST':
        file = request.files['file']

        new_file = open('static/img/img{0}.jpg'.format(len(os.listdir('static/img')) + 1), mode='wb')
        new_file.write(file.read())
        new_file.close()

        return "Форма отправлена"



def main():
    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
