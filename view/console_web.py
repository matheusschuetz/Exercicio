import sys
sys.path.append('C:/Users/900152/Documents/Dados/Squad')
from flask import Flask, render_template, request, redirect
from controller.Front_controller import FrontController, FrontEnd
from controller.sgbd_controller import SGBD_controller, SGBD
from controller.Back_controller import BackController, BackEnd
from controller.squad_controller import SquadController, Squad

app = Flask(__name__)

fc = FrontController()
bc = BackController()
sc = SGBD_controller()
sqc = SquadController()

@app.route('/')
def principal():
    return render_template('index.html')


@app.route('/listarFront')
def listar_front():
    lista_front = fc.select_all()
    return render_template('listarFront.html', lista = lista_front)

@app.route('/listarBack')
def listar_back():
    lista_back = bc.select_all()
    return render_template('ListarBack.html', lista = lista_back)

@app.route('/listarSgbd')
def listar_sgbd():
    lista_sgbd = sc.select_all()
    return render_template('listarSgbd.html', lista = lista_sgbd)

@app.route('/listarSquads')
def listar_squads():
    return render_template('listarSquads.html')

@app.route('/excluirsgbd')
def excluirsgbd():
    return redirect('/listarSgbd')


    
@app.route('/excluirback')
def excluirback():
    return redirect('/listarBack')



@app.route('/excluirfront')
def excluirfront():
    return redirect('/listarFront')


@app.route('/salvarSGBD')
def salvarSGBD():
    id = request.args['id']
    nome = request.args['nome']
    descricao = request.args['descricao']
    versao = request.args['versao']
    sgbd = SGBD(id,nome,descricao,versao)
    if sgbd.id ==0:
        sc.insert(sgbd)
    else:
        sc.update(sgbd)
    return redirect('/listarSgbd')

@app.route('/salvarFront')
def salvarFront():
    id = request.args['id']
    nome = request.args['nome']
    descricao = request.args['descricao']
    versao = request.args['versao']
    front = FrontEnd(id,nome,descricao,versao)
    if front.id ==0:
        fc.insert(front)
    else:
        fc.update(front)
    return redirect('/listarFront')

@app.route('/salvarBack')
def salvarBack():
    id = request.args['id']
    nome = request.args['nome']
    descricao = request.args['descricao']
    versao = request.args['versao']
    back = BackEnd(id,nome,descricao,versao)
    if back.id ==0:
        bc.insert(back)
    else:
        bc.update(back)
    return redirect('/listarBack')

@app.route('/salvarSquad')
def salvarSquad():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        id = 0
    nome = request.args['nomeSquad']
    desc = request.args['descricao']
    if 'qtdPessoas' in request.args:
        qtdPessoas = int(request.args['qtdPessoas'])
    else:
        qtdPessoas = 0
    s = Squad(id,nome, desc, qtdPessoas)

    if request.args['sgbd'] != 'Null':
        s.sgbd = int(request.args['sgbd'])
    if request.args['frameFront'] != 'Null':
        s.linguagemFront = int(request.args['frameFront'])
    if request.args['linguagemBack'] != 'Null':
        s.linguagemBack = int(request.args['linguagemBack'])
    
    sqc.insert(s)

    return redirect('/')

@app.route('/cadastroSGBD')
def cadastroSGBD():
    sgbd = SGBD(0,'','','')
    if 'id' in request.args:
        id  = request.args['id']
        sgbd = sc.select_byId(id)
    return render_template('cadastroSGBD.html', sgbd= sgbd)


@app.route('/cadastroFront')
def cadastroFront():
    front = FrontEnd(0, '','','')
    if 'id' in request.args:
        id = request.args['id']
        front = fc.select_by_id(id)
    return render_template('cadastroFront.html', front= front)

@app.route('/cadastroBack')
def cadastroBack():
    back = BackEnd(0, '','','')
    if 'id' in request.args:
        id = request.args['id']
        back = bc.select_by_id(id)
    return render_template('cadastroBack.html', back = back)

@app.route('/cadastroSquad')
def cadastroSquad():
    ls = sc.select_all()
    lf = fc.select_all()
    lb = bc.select_all()
    return render_template('cadastroSquad.html', lista_sgbd = ls, lista_front = lf, lista_back = lb)


app.run(debug=True)