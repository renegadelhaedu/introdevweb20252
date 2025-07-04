from flask import *

convidados = ['maria','joao pedro','pedro','jose','luciano','maria joana']

#instanciar um objeto do servidor Flask
app = Flask(__name__)

#cadastrar um endpoint ou rota para a raiz do projeto
@app.route('/')
def pagina_inicial():
    return render_template('inicial.html')


@app.route('/verificarconvite' , methods=['post'])
def verificar_convite():
    nome = request.form.get('nomeusuario')

    if nome.lower() in convidados:
        return render_template('convidado.html')
    else:
        return 'nao foi convidado'

@app.route('/desenvolvedor')
def get_nome_desenvolvedor():
    ano = 1991
    idade = 2025 - ano
    return 'jose carlos do nascimento junior. ele possui ' + str(idade) + ' anos'

#servidor seja executado
app.run()