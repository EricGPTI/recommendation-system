from math import sqrt

avaliacoes_usuarios = {'Ana':
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
                       {'O Ultimato Bourne': 4.5,
                           'Norbit': 1.0,
                           'Exterminador do Futuro': 4.0}
                       }

avaliacoes_filmes = {'Ana':
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
                     {'O Ultimato Bourne': 4.5,
                         'Norbit': 1.0,
                         'Exterminador do Futuro': 4.0}
                     }


# Cálculo da distância euclidiana
def euclidiana(base, user1, user2):
    si = {}
    for item in base[user1]:
        if item in base[user2]:
            si[item] = 1
        if len(si) == 0:
            return 0

        soma = sum([pow(base[user1][item] - base[user2][item], 2)
                    for item in base[user1] if item in base[user2]])

        return 1 / (1 + sqrt(soma))

# Obter a similaridade
def get_similares(base, usuario):
    similaridade = [(euclidiana(base, usuario, outros), outros)
                    for outros in base if outros != usuario]

    similaridade.sort()
    similaridade.reverse()
    return similaridade

# Obter recomendações
def get_recomendacoes(base, usuario):
    totais = {}
    soma_similaridade = {}
    for outro in base:
        if outro == usuario:
            continue
        similaridade = euclidiana(base, usuario, outro)
        if similaridade <= 0:
            continue
        for item in base[outro]:
            if item not in base[usuario]:
                totais.setdefault(item, 0)
                totais[item] += base[outro][item] * similaridade
                soma_similaridade.setdefault(item, 0)
                soma_similaridade[item] += similaridade

    recomendacoes = [(total / soma_similaridade[item], item)
                     for item, total in totais.items()]
    recomendacoes.sort()
    recomendacoes.reverse()
    return recomendacoes[0:30]


def load_movie_leans(path='C:/ml-100k'):
    filmes = {}
    for linha in open(path + '/u.item'):
        (id, titulo) = linha.split('|')[0:2]
        filmes[id] = titulo
    base = {}
    for linha in open(path + '/u.data'):
        (usuario, id_filme, nota, tempo) = linha.split('\t')
        base.setdefault(usuario, {})
        base[usuario][filmes[id_filme]] = float(nota)
    return base
