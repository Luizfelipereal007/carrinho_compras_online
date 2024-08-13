
class Loja:
    lista_produto = []
    lista_usuario = []
    nome: True
    validacao: bool


    def __init__(self,nome,validacao):
        nome = nome
        validacao = validacao

class Produto():
    nome: str
    preco: float
    descricao: str
    codigo: str

    def __init__(self,nome,preco,descricao,codigo):
        nome = nome
        preco = preco
        descricao = descricao
        codigo = codigo

class Usuario():
    nome: str
    idade: float
    cpf: str
    telefone:float
    email:str
    senha:str

    def __init__(self,nome,idade,cpf,telefone,email,senha):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.senha = senha    
    
class Administrador(Usuario):
    _id = ''

    def __init__(self,_id):
        self._id = _id
        self._id = ''