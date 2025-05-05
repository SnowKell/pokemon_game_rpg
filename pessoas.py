from pokemongame import *
import random

NOMES = [
    'renan', 'ash', 'itachi', 'sasuke', 'harry', 'peter', 'parker', 'eren', 'mikasa', 'levi', 'jose', 'eber', 'zenitsu'
]

POKEMONS = [
    PokemonEletrico('pikachu'),
    PokemonDeAgua('Squirtle'),
    PokemonPlanta('Bulbassaur'),
    PokemonDeFogo('Vulpix'),
    PokemonDePedra('Onix'),
    PokemonDeAgua('Poliwag'),
    PokemonFantasma('Gastly'),
    PokemonFantasma('Gengar'),
    PokemonPsiquico('Mewtwo'),
    PokemonPsiquico('Abra')

]


class Pessoa:
    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print('Pokemons de {}:'.format(self))
            for index, pokemon in enumerate(self.pokemons):
                print('{}- {}'.format(index, pokemon))
        else:
            print('{} ainda nao tem nenhum pokemon'.format(self))

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print('{} escolheu {}'.format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print('ERRO: voce nao tem nenhum pokemon para batalhar')

    def mostrar_dinheiro(self, ):
        dinheiro = self.dinheiro
        print('voce tem $  {} em sua conta'.format(self.dinheiro))

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print('voce ganhou $ {}'.format(quantidade))
        self.mostrar_dinheiro()

    def batalhar(self, pessoa):
        print('a batalha começou! {} contra {}'.format(self, pessoa))

        pessoa.mostrar_pokemons()

        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print('{} ganhou a batalha'.format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print('{} ganhou a batalha'.format(pessoa))
                    break
        else:
            print('não foi possivel iniciar a batalha')


class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} capturou {}'.format(self, pokemon))

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input('selecione o pokemon para a batalha: ')
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print('{} eu escolho voce!!!'.format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print('escolha inválida')

        else:
            print('ERRO: voce nao tem nenhum pokemon para batalhar')

    def explorar(self):
        if random.random() <= 0.3:
            pokemon_inimigo = random.choice(POKEMONS)
            print('um pokemon selvagem apareceu!! {}'.format(pokemon_inimigo))

            escolha = input('deseja capturar pokemon? (S/N): ')
            if escolha == 's':
                  if random.random() <= 0.5:
                    self.capturar(pokemon_inimigo)
                    print('voce capturou o pokemon {}'.format(pokemon_inimigo))
                    self.mostrar_pokemons()
                  else:
                     print('o pokemon {} fugiu'.format(pokemon_inimigo))
            else:
                  print('voce é fraco e fugiu')
        else:
            print('não foi encontrado nenhum pokemon')

class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))
            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokemons=pokemons)

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print('{} escolheu {}'.format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print('ERRO: voce nao tem nenhum pokemon para batalhar')