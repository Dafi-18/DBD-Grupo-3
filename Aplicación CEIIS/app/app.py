from flask import Flask, render_template, request, redirect, url_for, jsonify
import psycopg2

app= Flask(__name__)

# Conexión a la base de datos
def connect():
    conn = psycopg2.connect(
        host="localhost",
        database="ceiis",
        user='postgres',
        password='password123')
    return conn

'''
@app.before_request
def before_request():
    print("Antes de la peticion")

@app.after_request
def after_request(response):
    print("Despues de la peticion")
    return response
'''
# Menú principal del Portal CEIIS
@app.route('/')

def index():
    
    # return "<h1>CEIIS - Bienvenido</h1>"
    cursos=['PHP','Python','Java','C++','JavaScript']
    data={
        'titulo': 'Portal CEIIS',
        'saludo':'Bienvenido al CEIIS',
        'cursos': cursos,
        'numero_cursos': len(cursos)
    }
    return render_template('index.html', data = data)
    
    
    
@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'titulo': 'Contacto',
        'nombre': nombre,
        'edad': edad
    }
    return render_template('contacto.html', data = data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return 'OK'

@app.route('/articulo')
def listar_articulos():
    data = {}
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('SELECT id_articulo, nombre_articulo, cantidad FROM Articulo;')
        articulos = cur.fetchall()
        print(articulos)
        data['articulos'] = articulos
        #data['mensaje']= 'Exito'
        cur.close()
        conn.close()
    except Exception as ex:
        data['mensaje'] = 'Error...'
    return render_template('articulo.html', data = data)

def not_found(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index')) # Si no existe nos redirige a la vista index

if __name__=='__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, not_found)
    app.run(debug=True, port=5000)
    
