dicionario_numerico = [
    {
        '0': 'zero',
        '1': 'um',
        '2': 'dois',
        '3': 'três',
        '4': 'quatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'sete',
        '8': 'oito',
        '9': 'nove'
    },
    {
        '10': 'dez',
        '11': 'onze',
        '12': 'doze',
        '13': 'treze',
        '14': 'quatorze',
        '15': 'quinze',
        '16': 'dezesseis',
        '17': 'dezessete',
        '18': 'dezoito',
        '19': 'dezenove',
        '2': 'vinte',
        '3': 'trinta',
        '4': 'quarenta',
        '5': 'cinquenta',
        '6': 'sessenta',
        '7': 'setenta',
        '8': 'oitenta',
        '9': 'noventa',
    },
    {
        '1': 'cento',
        '2': 'duzentos',
        '3': 'trezentos',
        '4': 'quatrocentos',
        '5': 'quinhentos',
        '6': 'seiscentos',
        '7': 'setecentos',
        '8': 'oitocentos',
        '9': 'novecentos',
        '100': 'cem'
    }
]

while True:
    extenso = []  # armazena por extenso o valor digitado pelo usuário
    print('*' * 30)
    numero = input('Digite um número de 1 a 999: ').strip()
    try:
        int(numero)
    except ValueError:
        print(f"'{numero}' não é um número")
    else:
        numero = int(numero)
        if numero >= 0 and numero <= 999:
            numero = str(numero)
            # indica se o valor atual é uma centena, dezena ou unidade
            i = len(numero) - 1
            # verifica se o número é centena e se possui as casas dezena e unidade como 0 (zero).
            if len(numero) == 3 and numero[1] == '0' and numero[2] == '0':
                # se o valor da centena for 1, significa que o número digitado pelo usuário é 100 (cem).
                # Se não, imprime nome correspondente
                if numero[0] == '1':
                    extenso.append(dicionario_numerico[2].get(''.join(numero)))
                else:
                    extenso.append(dicionario_numerico[2].get(numero[0]))
            else:
                for x in numero:
                    # se a quantidade de algarismos for igual a 3 e o número 1 (um) estiver na dezena, Significa que a unidade
                    # está ocupando a posição [2]
                    if x == '1' and i == 1 and len(numero) == 3:
                        extenso.append(
                            dicionario_numerico[i].get(x + numero[2]))
                        break
                    # se a quantidade de algarismos for igual a 2 e o número 1 (um) estiver na dezena, Significa que a unidade
                    # está ocupando a posição [1]
                    elif x == '1' and i == 1 and len(numero) == 2:
                        extenso.append(
                            dicionario_numerico[i].get(x + numero[1]))
                        break
                    elif dicionario_numerico[i].get(x):
                        extenso.append(dicionario_numerico[i].get(x))
                    i -= 1

                # Exemplo: 320 = ['trezentos', 'vinte', 'zero'], o correto é conter apenas ['trezentos', 'vinte']
                if len(numero) > 1 and 'zero' in extenso:
                    extenso.remove('zero')

            print('\n{} - {}'.format(numero, ' e '.join(extenso)))
        else:
            print('\nNúmero fora do intervalo.')
