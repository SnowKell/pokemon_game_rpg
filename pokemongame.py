import random



class Pokemon:
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level:
          self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome

        else:
            self.nome = especie

        self.ataque = self.level * 3
        self.vida = self.level * 10

    def __str__(self):
        return '{} ({})'.format(self.nome, self.level)

    def atacar(self, pokemon):
        ataque_efetivo = int(self.ataque * random.random() * 1.3)
        pokemon.vida -= ataque_efetivo
        print('{} atacou {}, -{} de vida!'.format(self, pokemon, ataque_efetivo))

        if pokemon.vida <= 0:
            print('{} foi derrotado!'.format(pokemon))
            return True
        else: return False


class PokemonDeAgua(Pokemon):
       tipo = 'agua'

       def atacar(self, pokemon):
           print('({}) lançou um jato de água em {}'.format(self, pokemon))
           return super().atacar(pokemon)

       def tsunami(self, pokemon):
           print('({}) lançou um tsunami em {}'.format(self.nome, pokemon.especie))


class PokemonDePedra(Pokemon):
    tipo = 'pedra'

    def atacar(self, pokemon):
        print('({}) lançou uma laça de pedra em {}'.format(self, pokemon))
        return super().atacar(pokemon)

    def pedregulhos(self, pokemon):
        print('({}) lançou um ataque de pedregulhos em {}'.format(self.nome, pokemon.especie))


class PokemonPlanta(Pokemon):
    tipo = 'planta'

    def atacar(self, pokemon):
        print('({}) lançou chicote de vinha em {}'.format(self, pokemon))
        return super().atacar(pokemon)

    def fumaca(self, pokemon):
        print('({}) usou fumaça venenosa  em {}'.format(self.nome, pokemon.especie))


class PokemonDeFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, pokemon):
        print('({}) atacou com garras de chamas em {}'.format(self, pokemon))
        return super().atacar(pokemon)

    def bola_de_fogo(self, pokemon):
        print('({}) lançou uma bola de fogo em {}'.format(self.nome, pokemon.especie))


class PokemonDark(Pokemon):
    tipo = 'dark'

    def atacar(self, pokemon):
        print('({}) lançou um ataque noturno em {}'.format(self, pokemon))
        return super().atacar(pokemon)

    def ventoescuro(self, pokemon):
        print('({}) lançou o vento da escuridão em {}'.format(self.nome, pokemon.especie))

    def pesadelo(self, pokemon):
        print('({}) usou pesadelo dos sonhos em {}'.format(self.nome, pokemon.especie))


class Kyogre(PokemonDeAgua):

    def atacar(self, pokemon):
        print('({}) usou onda grandiosa {}'.format(self, pokemon))
        return super().atacar(pokemon)

    def pedregulhos(self, pokemon):
        print('({}) lançou esguicho duplo em {}'.format(self.nome, pokemon.especie))


class PokemonEletrico(Pokemon):

    def atacar(self, pokemon):
        print('({}) usou ataque choque do trovão {}'.format(self, pokemon))
        return super().atacar(pokemon)

    def trovoada(self, pokemon):
        print('({}) lançou trovoada em {}'.format(self.nome, pokemon.especie))

class PokemonFantasma(Pokemon):

    def atacar(self, pokemon):
        print('({}) usou língua sombria em {}'.format(self, pokemon))
        return super().atacar(pokemon)

    def explosao(self, pokemon):
        print('({}) usou explosão sombria em {}'.format(self.nome, pokemon.especie))


class PokemonPsiquico(Pokemon):

    def atacar(self, pokemon):
        print('({}) Usou onda psíquica {}'.format(self, pokemon))
        return super().atacar(pokemon)

    def confusao(self, pokemon):
        print('({}) Usou confusão}'.format(self.nome, pokemon.especie))