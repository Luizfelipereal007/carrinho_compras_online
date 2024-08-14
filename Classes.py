
class Loja:
    lista_produto = []
    lista_usuario = []
    nome: True
    validacao: bool


    def __init__(self,nome,validacao):
        nome = nome
        validacao = validacao

class Produto():
    id = str
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
    id = str
    nome: str
    idade: float
    cpf: str
    telefone:float
    email:str
    senha:str

    def __init__(self,id,nome,idade,cpf,telefone,email,senha):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.senha = senha    
    
class Administrador(Usuario):
    id = ''

    def __init__(self,id):
        self.id = id
        self.id = ''