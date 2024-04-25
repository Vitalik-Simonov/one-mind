# pip install scikit-learn
# pip install pandas
# pip install flask

from flask import Flask, request
import pandas as pd
import os
from sklearn.cluster import KMeans


def hash(s):
    ans = 0
    for i in s:
        ans += ord(i) * 1001123 ** s.index(i)
    ans %= 1001237
    return ans


def predict(data, num=3):
    fio = data.fio
    data.drop(columns=['fio'], inplace=True)
    kmeans = KMeans(n_clusters=num, random_state=42, n_init="auto")
    kmeans.fit(data)
    ans = list(kmeans.labels_)
    return dict(zip(fio, ans))


app = Flask(__name__)
dic = {}
col = ['fio', 'rock', 'pop', 'phonk', 'classic', 'rep', 'comp', 'game', 'walk', 'TV', 'music', 'math', 'lang', 'force',
       'iso', 'musa', 'foot', 'fig', 'hok', 'chess', 'box', 'ser', 'com', 'det', 'mel', 'fight']


@app.route('/send/<name>', methods=['POST'])
def se(name):
    s = list(request.form)
    df = pd.read_csv(name + '.csv')
    ans = [request.form['fio']]
    for i in col[1:]:
        if i in s:
            ans += [1]
        else:
            ans += [0]
    df.loc[len(df)] = ans
    df.to_csv(name + '.csv', index=False)
    return 'Форма ' + ans[0] + ' отправлена'


@app.route('/form/<name>')
def ff(name):
    name1 = dic[name]
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Симонов Виталий Большая перемена</title>
    <style>
        body {
         background:rgba(9, 228, 228, 0.541);
        }
       </style>
</head>
<body>
    <h1>Проект Единомышленники 1.0</h1>
    <p>Данный проект создан в рамках конкурса "Большая перемена"
        <br> Симонов Виталий МАОУ "СОШ №13 с УИОП" 8М город Электросталь Московской области
    </p>''' + f'''
<h2>{name1}</h2>
    <form action="/send/{name}" method="POST">
        <div class="form-group">
            <label><h3>Введи ФИО</h3></label>
            <input type="text" name="fio">
            <br>
            <label><h3>Какую музыку ты любишь?</h3></label><br>

            <input type="checkbox" class="form-check-input" id="rock" name="rock">
            <label class="form-check-label" for="rock">Рок</label>
            <br>
            <input type="checkbox" class="form-check-input" id="pop" name="pop">
            <label class="form-check-label" for="pop">Поп-музыка</label>
            <br>
            <input type="checkbox" class="form-check-input" id="phonk" name="phonk">
            <label class="form-check-label" for="phonk">Фонк</label>
            <br>
            <input type="checkbox" class="form-check-input" id="classic" name="classic">
            <label class="form-check-label" for="classic">Классическая музыка</label>
            <br>
            <input type="checkbox" class="form-check-input" id="rep" name="rep">
            <label class="form-check-label" for="rep">Рэп</label>
        </div>

        <div class="form-group">
            <br>
            <label><h3>Как ты проводишь свой досуг?</h3></label><br>

            <input type="checkbox" class="form-check-input" id="comp" name="comp">
            <label class="form-check-label" for="comp">Играю в компьютер</label>
            <br>
            <input type="checkbox" class="form-check-input" id="game" name="game">
            <label class="form-check-label" for="game">Играю в настольные игры</label>
            <br>
            <input type="checkbox" class="form-check-input" id="walk" name="walk">
            <label class="form-check-label" for="walk">Гуляю с друзьями</label>
            <br>
            <input type="checkbox" class="form-check-input" id="TV" name="TV">
            <label class="form-check-label" for="TV">Смотрю телевизор</label>
            <br>
            <input type="checkbox" class="form-check-input" id="music" name="music">
            <label class="form-check-label" for="music">Слушаю музыку</label>
        </div>
        
        <div class="form-group">
            <br>
            <label><h3>Какие твои любимые школьные предметы?</h3></label><br>

            <input type="checkbox" class="form-check-input" id="math" name="math">
            <label class="form-check-label" for="math">Математика</label>
            <br>
            <input type="checkbox" class="form-check-input" id="lang" name="lang">
            <label class="form-check-label" for="lang">Русский язык и литература</label>
            <br>
            <input type="checkbox" class="form-check-input" id="force" name="force">
            <label class="form-check-label" for="force">Физкультура</label>
            <br>
            <input type="checkbox" class="form-check-input" id="iso" name="iso">
            <label class="form-check-label" for="iso">Рисование</label>
            <br>
            <input type="checkbox" class="form-check-input" id="musa" name="musa">
            <label class="form-check-label" for="musa">Музыка</label>
        </div>

        <div class="form-group">
            <br>
            <label><h3>Какие твои любимые виды спорта?</h3></label><br>

            <input type="checkbox" class="form-check-input" id="foot" name="foot">
            <label class="form-check-label" for="foot">Футбол</label>
            <br>
            <input type="checkbox" class="form-check-input" id="fig" name="fig">
            <label class="form-check-label" for="fig">Фигурное катание</label>
            <br>
            <input type="checkbox" class="form-check-input" id="hok" name="hok">
            <label class="form-check-label" for="hok">Хоккей</label>
            <br>
            <input type="checkbox" class="form-check-input" id="chess" name="chess">
            <label class="form-check-label" for="chess">Шахматы</label>
            <br>
            <input type="checkbox" class="form-check-input" id="box" name="box">
            <label class="form-check-label" for="box">Бокс</label>
        </div>

        <div class="form-group">
            <br>
            <label><h3>Какие твои любимые жанры фильмов?</h3></label><br>

            <input type="checkbox" class="form-check-input" id="ser" name="ser">
            <label class="form-check-label" for="ser">Сериалы</label>
            <br>
            <input type="checkbox" class="form-check-input" id="com" name="com">
            <label class="form-check-label" for="com">Комедии</label>
            <br>
            <input type="checkbox" class="form-check-input" id="det" name="det">
            <label class="form-check-label" for="det">Детективы</label>
            <br>
            <input type="checkbox" class="form-check-input" id="mel" name="mel">
            <label class="form-check-label" for="mel">Мелодрамы</label>
            <br>
            <input type="checkbox" class="form-check-input" id="fight" name="fight">
            <label class="form-check-label" for="fight">Боевики</label>
        </div>
        
        <br>
        <input type="submit" value="отправить"/>
    </form>
</body>
</html>
'''


@app.route('/see', methods=['POST'])
def see():
    A = request.form['name_kol']
    if not os.path.isfile(str(hash(A)) + '.csv'):
        return 'Введите верное название'
    ans = predict(pd.read_csv(str(hash(A)) + '.csv'), 3)
    an = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
        body {
         background:rgba(9, 228, 228, 0.541);
        }
       </style>
    </head>
    <body>
        <center><table border="2">
            <caption>Распределение коллектива по группам</caption>
            <tr>
             <th>Имя</th>
             <th>Номер группы</th>
            </tr>'''
    for k, v in ans.items():
        an += f'\n<tr><td>{k}</td><td>{v + 1}</td></tr>\n'
    an += '</table></center>'
    return an


@app.route('/itog', methods=['POST'])
def f():
    A = request.form['kol']
    if os.path.isfile(str(hash(A)) + '.csv'):
        return 'Введите уникальное название'
    dic[str(hash(A))] = A
    pd.DataFrame(columns=col).to_csv(str(hash(A)) + '.csv', index=False)
    return f'<p>Форма отправлена:</p><br><a href=/form/{str(hash(A))}>Опрос для коллектива: ' + A + \
           '</a><br><br> <a href=/result>Смотреть результаты</a>'


@app.route('/')
@app.route('/index')
def index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Симонов Виталий Большая перемена</title>
    <style>
        body {
         background:rgba(9, 228, 228, 0.541);
        }
       </style>
</head>
<body>
    <center><h1>Проект Единомышленники 1.0</h1>
    <p>Данный проект создан в рамках конкурса "Большая перемена"
        <br> Симонов Виталий МАОУ "СОШ №13 с УИОП" 8М город Электросталь Московской области
    </p>
    <h2>Введите название коллектива</h2>
    <form action="/itog" method="POST">
        <input type="text" name="kol">
        <input type="submit" value="отправить"/>
    </form>
    </center>
</body>
</html>'''


@app.route('/result')
def result():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Симонов Виталий Большая перемена</title>
    <style>
        body {
         background:rgba(9, 228, 228, 0.541);
        }
       </style>
</head>
<body>
    <center><h1>Проект Единомышленники 1.0</h1>
    <p>Данный проект создан в рамках конкурса "Большая перемена"
        <br> Симонов Виталий МАОУ "СОШ №13 с УИОП" 8М город Электросталь Московской области
    </p>
    <h2>Введите название коллектива</h2>
    <form action="/see" method="POST">
        <input type="text" name="name_kol">
        <input type="submit" value="распределить"/>
    </form>
    </center>
</body>
</html>'''


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
