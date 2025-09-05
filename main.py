from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


# Lista inicial de usuários já cadastrados
usuarios = [
    {"id": 1, "nome": "Marcelo", "gmail": "marcelo09@gmail.com", "ativo": True},
    {"id": 2, "nome": "Alice", "gmail": "alice22@gmail.com", "ativo": True},
    {"id": 3, "nome": "Bruno", "gmail": "bruno33@gmail.com", "ativo": False},
    {"id": 4, "nome": "Carla", "gmail": "carla44@gmail.com", "ativo": True},
    {"id": 5, "nome": "Daniel", "gmail": "daniel55@gmail.com", "ativo": True},
    {"id": 6, "nome": "Elena", "gmail": "elena66@gmail.com", "ativo": False},
    {"id": 7, "nome": "Fernando", "gmail": "fernando77@gmail.com", "ativo": True},
    {"id": 8, "nome": "Gabriela", "gmail": "gabriela88@gmail.com", "ativo": True},
    {"id": 9, "nome": "Henrique", "gmail": "henrique99@gmail.com", "ativo": False},
    {"id": 10, "nome": "Isabela", "gmail": "isabela10@gmail.com", "ativo": True}
]


# Modelo de como deve ser o corpo de um usuário
class Usuario(BaseModel):
    nome: str
    gmail: str 
    ativo: bool 


# Função para calcular o próximo ID automaticamente
def proximo_id():
    if usuarios:
        return max(usu["id"] for usu in usuarios) + 1
    return 1


# Rota para mostrar todos os usuários
@app.get('/usuarios')
def mostrar_usuarios():
    return usuarios


# Rota para buscar um usuário pelo ID
@app.get('/usuarios/{id}')
def mostrar_id(id: int):
    for usu in usuarios:
        if usu["id"] == id:
            return usu
    return {'mensagem' : 'Usuário não encontrado'}    


# Rota para deletar um usuário pelo ID
@app.delete('/usuarios/{id}')
def deletar_usuario(id: int):
    for usu in usuarios:
        if usu["id"] == id:
            usuarios.remove(usu)      
            return {'mensagem' : f'Usuário {id} deletado com sucesso!'}
    return {'mensagem' : 'Usuário não encontrado'}                  


# Rota para cadastrar um novo usuário
@app.post('/usuarios/')
def cadastro_usuario(usuario: Usuario):
    novo_usuario = {"id": proximo_id(), **usuario.dict()}
    usuarios.append(novo_usuario)
    return {'mensagem' : 'Usuário cadastrado com sucesso!'}


# Rota para atualizar um usuário existente
@app.put('/usuarios/{id}/')
def atualiazar_usuario(id: int, usuario: Usuario):
    for usu in usuarios:
        if usu["id"] == id:
            usu.update(usuario.dict())
            return {'mensagem' : f'Usuário {id} atualizado com sucesso'}
    return {'mensagem' : 'Usuário não encontrado'}    
