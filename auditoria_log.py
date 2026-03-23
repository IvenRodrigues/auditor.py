palavra = "ERRO"
total_erros = 0

# ABRE O LOG PARA LEITURA E O RELATORIO PARA ANEXAÇÃO
with open("servidor.log", "r") as log, open("erros.txt", "a") as saida:
    for linha in log:
        # PADRONIZA A LINHA PARA MAIÚSCULAS APENAS NA CHECAGEM 
        if palavra in linha.upper():
            saida.write(linha) #GRAVA A LINHA ORIGINAL (PRESERVA A EVIDÊNCIA)
            total_erros += 1

print(f"Linha adicionada ao arquivo erros.txt")
print(f"Total de erros salvos: {total_erros}")



