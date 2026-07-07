#Jogo da palavra secreta#
palavra_secreta = 'Flora'
letras_acertadas = ''
while True:
    letra_digitada = input("Digite uma letra: ")

    if len(letra_digitada) > 1:
        print("Digite apenas 1 letra")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            print(letra_secreta)
        else:
            print('*')
