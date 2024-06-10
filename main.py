from datetime import datetime
import random


def gen_id1(num_max):
    id = ''
    for i in range(num_max):
        id+=f'{random.randint(0,9)}'
    return id
def gen_id2(num_max):
    lista_char = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    id2 = ''
    for i in range(num_max):
        id2+=f'{random.choice([random.randint(0,9),random.choice(lista_char)])}'
    return id2

def gen_data_nasc():
    mes = random.randint(1,12)
    ano = random.randint(1910,2022)
    dia = ''
    match mes:
        case 1|3|5|7|8|10|12:
            dia = random.randint(1,31)
        case 4|6|9|11:
            dia = random.randint(1,30)
        case 2:
            if ano%4 == 0:
                dia = random.randint(1,29)
            else:
                dia = random.randint(1,28)
    return f'{dia:02d}/{mes:02d}/{ano}'
    
def gen_genero():
    return random.choice(['m','f','nd'])
def salva_entrada(dados):
    with open(f'./{datetime.today().date()}.csv', 'a') as f:
        f.write(f'{dados}\n')
    return

if __name__ == '__main__':
    with open(f'./nomes.txt', 'r') as r:
        nomes = r.readlines()
    for nome in nomes:
        entrada = f'{nome[:-1]},{gen_id1(9)},{gen_data_nasc()},{gen_id2(9)},{gen_genero()}'
        print(entrada)
        salva_entrada(entrada)
