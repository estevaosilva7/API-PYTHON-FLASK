from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Diário de uma paixão',
        'autor': 'Nicholas Sparks'
    },
    {
        'id': 2,
        'título': 'Como eu era antes de você',
        'autor': 'Jojo Moyes'
    },
    {
        'id': 3,
        'título': 'Querido John',
        'autor': 'Nicholas Sparks'
    },
]

# Consultar (todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    
# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') ==id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
# Criar    
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

        return jsonify(livros)

app.run(port=500,host='localhost',debug=True)