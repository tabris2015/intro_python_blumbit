from flask import Flask
app = Flask(__name__)

@app.route('/')             # decorator
def hello_world():
    return '<h1>Hola </h1> <h3>amigos</h3>'

@app.route('/hola')
def hola2():
    return 'que tal, normal'

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'hola {nombre}, como estas?'

# esto se ejecuta solo cuando ejecuto el 
# archivo de esta forma:
# python hola.py
if __name__ == '__main__':
    app.run()
