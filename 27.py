nome = str(input('Digite seu nome: ')).strip()

divisao = nome.split()

print(f"""Muito prazer em te conhecer!

Seu primeiro nome é {divisao[0]}.

Seu ultimo nome é {divisao[-1]}.""")