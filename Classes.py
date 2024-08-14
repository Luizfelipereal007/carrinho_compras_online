
class Loja:
    lista_produto = []
    lista_usuario = []
    nome: str
    validacao: bool


    def __init__(self,nome = None,validacao = None):
        nome = nome
        validacao = validacao

class Produto():
    id: str
    nome: str
    preco: float
    descricao: str
    codigo: str

    def __init__(self, id = None, nome = None,preco = None,descricao = None,codigo = None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.codigo = codigo

class Usuario():
    id: str
    nome: str
    idade: float
    cpf: str
    telefone:float
    email:str 
    usuario: str
    senha:str

    def __init__(self,id = None,nome = None,idade = None,cpf = None,telefone = None,email = None,usuario = None,senha = None):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha    
    
class Administrador(Usuario):
    usuario = 'ADM'
    senha = "123"

    def __init__(self, id= None, nome = None,usuario = None , senha = None):
        super().__init__(id,nome,usuario, senha)
        self.id = id
        self.nome = nome
        self.usuario = usuario
        self.senha = senha
        