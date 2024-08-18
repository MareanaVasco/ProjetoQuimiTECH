from flask import Flask, request, jsonify
import psycopg2
import bcrypt

app = Flask(__name__)

DB_HOST = "localhost"
DB_NAME = "quimitech"
DB_USER = "IFSP2024"
DB_PASS = "@Ifsp2024"

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['ds_email']
    senha = data['ds_senha']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT ds_senha FROM usuarios WHERE ds_email = %s', (email,))
    user = cursor.fetchone()

    if user and bcrypt.checkpw(senha.encode('utf-8'), user[0].encode('utf-8')):
        response = {'message': 'Login bem-sucedido!'}
    else:
        response = {'message': 'Email ou senha incorretos!'}

    cursor.close()
    conn.close()
    return jsonify(response)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    nome = data['ds_nome']
    usuario = data['ds_usuario']
    email = data['ds_email']
    senha = bcrypt.hashpw(data['ds_senha'].encode('utf-8'), bcrypt.gensalt())

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO usuarios (ds_nome, ds_usuario, ds_email, ds_senha) VALUES (%s, %s, %s, %s)',
            (nome, usuario, email, senha.decode('utf-8'))
        )
        conn.commit()
        response = {'message': 'Usuário registrado com sucesso!'}
    except psycopg2.IntegrityError:
        conn.rollback()
        response = {'message': 'Email já registrado!'}
    
    cursor.close()
    conn.close()
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
