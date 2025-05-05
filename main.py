from pokemongame import *
from pessoas import *
import pickle

def escolher_pokemon_inicial(player):
    print('>>> Você poderá escolher um pokemon para lhe acompanhar nessa jornada!')


    bulbassaur = PokemonPlanta('bulbassaur', level=1)
    charmander = PokemonEletrico('charmander', level=1)
    squirtle = PokemonEletrico('squirtle', level=1)

    print('voce tem 3 escolhas:')
    print('1-', bulbassaur)
    print('2-', charmander)
    print('3-', squirtle)

    while True:
        escolha = input('escolha seu pokemon: ')
        if escolha == '1':
            player.capturar(bulbassaur)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('escolha inválida')


def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
    except Exception as error:
        print('Erro ao salvar jogo')
        print(error)

def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            print('Jogo carregado')
            return player
    except Exception:
        print('Save não encontrado')


if __name__ == '__main__':
    print('________________________________________________________')
    print('>>> olá, bem vindo ao jogo de pokemon RPG de terminal')
    print('________________________________________________________')

    player = carregar_jogo()

    if not player:
      nome = input('Digite o nome que você quer ser chamado: ')
      player = Player(nome)

    print('>>> Bem-Vindo {}, sua missão aqui é capturar e se tornar o mestre dos pokemons!'.format(player))
    if player.pokemons:
        print('Vi que você tem alguns pokemons')
        player.mostrar_pokemons()
    else:
        print('você ainda não tem nenhum pokemon, portanto, precisa escolher um:')
        escolher_pokemon_inicial(player)

    if not POKEMONS:
        print('pronto! agora você vai ter sua primeira experiência em batallha!')
        Alucard = Inimigo(nome='Alucard', pokemons=[PokemonDeAgua('Squirtle', level=1)])
        player.batalhar(Alucard)
        salvar_jogo(player)
    else:
       print('voce ja tem pokemons, vamos lá')

    while True:
        print('o que deseja fazer:')
        print('1- explorar o mundo')
        print('2- batalhar com NPC')
        print('3- mostrar pokemons')
        print('4- mostrar saldo')
        print('0- sair do jogo')
        escolha = input('Qual opção? ')

        if escolha == '1':
            print('ok, vamos explorar!!')
            player.explorar()
            salvar_jogo(player)
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == '3':
            player.mostrar_pokemons()
        elif escolha == '4':
            player.mostrar_dinheiro()
        elif escolha == '0':
            print('fechando o jogo...')
            break
        else:
            print('Escolha inválida')
