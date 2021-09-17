from math import sqrt

avaliacoes = {'Ana': 
		{'Freddy x Jason': 2.5, 
		 'O Ultimato Bourne': 3.5,
		 'Star Trek': 3.0, 
		 'Exterminador do Futuro': 3.5, 
		 'Norbit': 2.5, 
		 'Star Wars': 3.0},
	 
	  'Marcos': 
		{'Freddy x Jason': 3.0, 
		 'O Ultimato Bourne': 3.5, 
		 'Star Trek': 1.5, 
		 'Exterminador do Futuro': 5.0, 
		 'Star Wars': 3.0, 
		 'Norbit': 3.5}, 

	  'Pedro': 
	    {'Freddy x Jason': 2.5, 
		 'O Ultimato Bourne': 3.0,
		 'Exterminador do Futuro': 3.5, 
		 'Star Wars': 4.0},
			 
	  'Claudia': 
		{'O Ultimato Bourne': 3.5, 
		 'Star Trek': 3.0,
		 'Star Wars': 4.5, 
		 'Exterminador do Futuro': 4.0, 
		 'Norbit': 2.5},
				 
	  'Adriano': 
		{'Freddy x Jason': 3.0, 
		 'O Ultimato Bourne': 4.0, 
		 'Star Trek': 2.0, 
		 'Exterminador do Futuro': 3.0, 
		 'Star Wars': 3.0,
		 'Norbit': 2.0}, 

	  'Janaina': 
	     {'Freddy x Jason': 3.0, 
	      'O Ultimato Bourne': 4.0,
	      'Star Wars': 3.0, 
	      'Exterminador do Futuro': 5.0, 
	      'Norbit': 3.5},
			  
	  'Leonardo': 
	    {'O Ultimato Bourne':4.5,
             'Norbit':1.0,
	     'Exterminador do Futuro':4.0}
}

# Cálculo da distância euclidiana
def euclidiana(user1, user2):
	si = {}
	for item in avaliacoes[user1]:
		if item in avaliacoes[user2]:
			si[item] = 1
		if len(si) == 0:
			return 0
		
		soma = sum([pow(avaliacoes[user1][item] - avaliacoes[user2][item], 2)
					for item in avaliacoes[user1] if item in avaliacoes[user2]])

		return 1 / (1 + sqrt(soma))

# Obter a similaridade
def get_similares(usuario):
	similaridade = [(euclidiana(usuario, outros), outros)
		for outros in avaliacoes if outros != usuario]
	
	similaridade.sort()
	similaridade.reverse()
	return similaridade

# 
def get_recomendacoes(usuario):
	totais = {}
	soma_similaridade = {}
	for outro in avaliacoes:
		if outro == usuario:
			continue
		similaridade = euclidiana(usuario, outro)
		if similaridade <= 0:
			continue
		for filmes in avaliacoes[outro]:
			if filmes not in avaliacoes[usuario]:
				totais.setdefault(filmes, 0)
				totais[filmes] += avaliacoes[outro][filmes] * similaridade
				soma_similaridade.setdefault(filmes, 0)
				soma_similaridade[filmes] += similaridade

	recomendacoes = [(total / soma_similaridade[filme], filme) for filme, total in totais.items()]
	recomendacoes.sort()
	recomendacoes.reverse()
	return recomendacoes
