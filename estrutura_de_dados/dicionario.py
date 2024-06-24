# Definindo um dicionário com informações sobre filmes

filmes = {"Incendios": "drama", "Nós": "terror", "O Mentiroso": "comedia"}

for filmes, genero in filmes.items():
    print (f'O gênero do filme {filmes} é {genero}')