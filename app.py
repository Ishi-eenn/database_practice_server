from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
cors = CORS(app)

connection = psycopg.connect(
    host='localhost',
    dbname='list',
    user='postgres',
    password='password',
)

@app.route('/todo-lists', methods=['GET'])
def get_todo_lists():
    sql = '''
    SELECT * FROM 本棚;
    '''
    result = connection.execute(sql)
    todo_lists = []
    for row in result:
        todo_list = {
            'id': row[0],
            'title': row[1],
            'description': row[2],
            'url': row[3],
            'userId': row[4]
        }
        todo_lists.append(todo_list)
    return jsonify(todo_lists)

@app.route('/todo-lists', methods=['POST'])
def post_todo_list():

    sql = '''
    SELECT ID
    FROM 本棚;
    '''
    result = connection.execute(sql)
    key = []
    for row in result:
        key.append(row[0])
    new_key = 1
    while True:
        if new_key not in key:
            break
        new_key += 1
    content = request.get_json()

    try:
        sql = '''
        INSERT INTO 本棚 (ID, タイトル, 内容, リンク, ユーザー)
        VALUES
        (%(ID)s, %(title)s, %(description)s, %(url)s, %(userId)s);
        '''
        connection.execute(sql,{'ID': new_key, 'title': content["title"], 'description': content["description"], 'url': content["url"], 'userId': content["userId"]})
    except Exception:
        connection.rollback()
    else:
        connection.commit()

    return jsonify({'message': 'created'})

@app.route('/todo-lists/<int:id>', methods=['POST'])
def delete_todo_list(id):
    try:
        sql = '''
        DELETE FROM 本棚 WHERE ID = %(id)s
        '''
        connection.execute(sql,{'id': id})
    except Exception:
        connection.rollback()
    else:
        connection.commit()

    return jsonify({'message': 'created'})


@app.route('/login', methods=['GET'])
def get_login():
    sql = '''
    SELECT * FROM login;
    '''
    result = connection.execute(sql)
    todo_lists = []
    for row in result:
        todo_list = {
            'id': row[0],
            'email': row[1],
            'password': row[2]
        }
        todo_lists.append(todo_list)
    return jsonify(todo_lists)

@app.route('/login', methods=['POST'])
def post_login():

    sql = '''
    SELECT ID
    FROM login;
    '''
    result = connection.execute(sql)
    key = []
    for row in result:
        key.append(row[0])
    new_key = 1
    while True:
        if new_key not in key:
            break
        new_key += 1
    content = request.get_json()

    try:
        sql = '''
        INSERT INTO login (ID, email, password)
        VALUES
        (%(ID)s, %(email)s, %(password)s);
        '''
        connection.execute(sql,{'ID': new_key, 'email': content["email"], 'password': content["password"]})
    except Exception:
        connection.rollback()
    else:
        connection.commit()

    return jsonify({'message': 'created'})

# @app.route('/impressions', methods=['GET'])
# def get_impressions():
#     sql = '''
#     SELECT * FROM 感想;
#     '''
#     result = connection.execute(sql)
#     impressions = []
#     for row in result:
#         impression = {
#             'id': row[0],
#             'title': row[1],
#             'description': row[2],
#             'url': row[3],
#         }
#         impressions.append(impression)
#     return jsonify(impressions)

