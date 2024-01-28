# magicos = ['alice', 'david', 'carolina']
# for magico in magicos:
#     print(f"{magico.title()}, foi um bom truque!")
#     print(f"Mal posso esperar para seu próximo truque, {magico.title()}!\n")


# print(f"Obrigado todo mundo. Foi um ótimo show!")

# pizzasPreferida = ['portuguesa', 'mussarela', 'calabresa']
# for pizza in pizzasPreferida:
#     print(f"Eu gosto de pizza de {pizza.title()}\n")

# print("Eu amo Pizzas!\n")

# animais = ['cachorro', 'gato', 'sapo']
# for animal in animais:
#     print(f"O {animal.title()} seria um ótimo Pet!\n")

# print("Todos esses animais são mamíferos!\n")

# for valor in range(1, 5):
#     print(valor)

# numeros = list(range(1, 6))
# print(numeros)

# evenNumbers = list(range(2, 11, 2))
# print(evenNumbers)

# numerosQuadrado = []
# for valor in range(1, 11):
#     numeroQuadrado = valor **2
#     numerosQuadrado.append(numeroQuadrado)

# print(numerosQuadrado)

# squares = []
# for value in range(1, 11):
#     squares.append(value**2)

# print(squares)

# quadrados = [value**2 for value in range(1, 11)]
# print(quadrados)

# for value in range(1, 21):
#     print(value)

# numeros = list(range(1, 21))
# print(numeros)


# numeros = list(range(1, 1000001))
# print(numeros)

# for value in range(3, 30, 3):
#     print(value)


# cubo = []
# for value in range(1, 11):
#     cubo.append(value**3)

# print(cubo)


# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])
# print(players[-3:])
# print(players[3:])

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("Aqui estão os três primeiros do meu time:")
# for player in players[:3]:
#     print(player.title())

# minhaComida = ['pizza', 'falafel', 'bolo de cenoura']
# amigoComida = minhaComida[:]
# minhaComida.append('cannoli')
# amigoComida.append('sorvete')
# print("Minhas comidas favoritas são:")
# print(minhaComida)
# print("As comidas do meu amigo são:")
# print(amigoComida)


# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("Aqui estão os três primeiros do meu time:")
# for player in players[:3]:
#      print(player.title())
# tresPrimeiro = players[0:3]
# print("Os três primeiros elementos da lista são:")
# print(tresPrimeiro)
# tresMeio = players[1:4]
# print("Os três elementos do meio da lista são:")
# print(tresMeio)
# tresUltimo = players[-3:]
# print("Os três últimos elementos da lista são:")
# print(tresUltimo)


# pizzasPreferida = ['portuguesa', 'mussarela', 'calabresa']
# pizzaAmigo = pizzasPreferida[:]

# pizzasPreferida.append('palmito')
# pizzaAmigo.append('rúcula')

# for pizza in pizzasPreferida:
#     print(f"Uma das minhas pizzas favoritas é: {pizza.title()}")

# for pizza in pizzaAmigo:
#     print(f"Uma das pizzas do meu amigo é: {pizza.title()}")



# dimensions = (200, 50)
# print("Dimensão original:")
# for dimension in dimensions:
#     print(dimension)

# dimensions = (400, 100)
# print("\nDimensão modificada:")
# for dimension in dimensions:
#     print(dimension)




refeicaoTodas = ('arroz', 'feijão', 'salada', 'batata frita', 'legumes')
for refeicao in refeicaoTodas:
    print(f"Nós temos: {refeicao.title()}")


print("\nTemos duas novas opções no cardápio. Veja a seguir:\n")

refeicaoTodas = ('arroz', 'feijão', 'salada', 'polenta', 'peixe')
for refeicao in refeicaoTodas:
    print(f"Agora nossas opções são: {refeicao.title()}")
