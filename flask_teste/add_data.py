from app import db, User, app

# Criar o contexto da aplicação
with app.app_context():
    # Criação de instâncias de usuários
    usuario1 = User(nome='João Victor')
    usuario2 = User(nome='Ana Maria')
    usuario3 = User(nome='Pedro Augusto')

    # Adicionar os usuários à sessão
    db.session.add(usuario1)
    db.session.add(usuario2)
    db.session.add(usuario3)

    # Confirmar a transação no banco de dados
    db.session.commit()

    # Mensagem de sucesso
    print(f'Usuários adicionados com sucesso')