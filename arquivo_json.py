import json

"""Obtém o nome do usuário já armazenado se estiver disponível."""
def get_stored_username():
    filename = 'text_files/username.json'
    try:
        with open(filename, 'r', encoding='utf-8') as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

"""Pede um novo nome de usuário."""
def get_new_username(): 
    username = input("Qual o seu nome? ")
    filename = 'text_files/username.json'
    with open(filename, 'w', encoding='utf-8') as f_obj: 
        json.dump(username, f_obj) 
    return username

"""Saúda o usuário pelo nome."""
def greet_user():
    username = get_stored_username()
    if username:
        print(f'Seja bem-vindo de volta, {username}!')
    else:
        username = get_new_username()
        print(f'Nós nos lembraremos de você quando você voltar, {username}!')
greet_user()