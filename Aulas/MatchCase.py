comando = 'Adeus, Mundo!'

match comando:
    case 'Olá, Mundo!':
        print("Olá para você tambem")
    case 'Adeus, Mundo!':
        print("Adeus!")
    case _:
        print("Sem resultados!")