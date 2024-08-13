
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
    id_produto: str

    def __init__(self,nome,preco,descricao,id_produto):
        nome = nome
        preco = preco
        descricao = descricao
        id_produto = id_produto

class Usuario():
    nome: str
    cpf: float
    email: str
    senha: str

    def __init__(self,nome,cpf,email,senha):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha    
    
class Administrador:
    _id = ''
    nome = str
    login = (Usuario)

    def __init__(self,_id,nome,login):
        self._id = _id
        self._id = ''
        self.nome = nome
        self.login = login