from fastapi import FastAPI, HTTPException

app = FastAPI()

produtos = {
    1: {"nome": "Notebook",   "preco": 3500.00,   "quantidade": 10},
    2: {"nome": "Mouse",      "preco": 80.00,     "quantidade": 50},
    3: {"nome": "Teclado",    "preco": 120.00,    "quantidade": 30},
    4: {"nome": "Monitor",    "preco": 900.00,    "quantidade": 15}
}


# ROTA PRINCIPAL
@app.get('/')
def home():
    return 'Essa é a rota principal!'


# ROTA PARA PEGAR TODOS OS PRODUTOS
@app.get('/produtos')
def listar_produtos():
    return produtos


# ROTA PARA PEGAR UM PRODUTO ESPECÍFICO COM BASE NO SEU ID
@app.get("/produtos/{produto_id}")
def obter_produto(produto_id: int):
    if produto_id not in produtos:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produtos[produto_id]


# ROTA PARA CRIAR UM PRODUTO COM MÉTODO POST
@app.post("/produtos", status_code=201)
def criar_produto(nome: str, preco: float, quantidade: int):
    
    novo_id = max(produtos.keys()) + 1 

    produtos[novo_id] = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
    }
    
    return {"msg": "Produto criado", "id": novo_id, "dados": produtos[novo_id]}


# ROTA PARA DELETAR UM PRODUTO
@app.delete("/produtos/{produto_id}")
def deletar_produto(produto_id: int):

    if produto_id not in produtos:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    produto_removido = produtos.pop(produto_id)

    return {
        "msg": "Produto removido com sucesso",
        "id": produto_id,
        "dados": produto_removido
    }


# ROTA PARA ATUALIZAR INFORMAÇÕES DE UM PRODUTO
@app.put("/produtos/{produto_id}")
def atualizar_produto(produto_id: int, nome: str, preco: float, quantidade: int):

    if produto_id not in produtos:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    produtos[produto_id] = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    return {
        "msg": "Produto atualizado com sucesso",
        "id": produto_id,
        "dados": produtos[produto_id]
    }