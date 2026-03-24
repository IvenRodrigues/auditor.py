import sys

# 1. VERIFICAÇÃO DE ARGUMENTOS (Porteiro do Script)
if len(sys.argv) < 2:
    print("ERRO: Você esqueceu de passar o nome do log!")
    sys.exit(1)

try:
    palavra = "ERRO"
    total_erros = 0

    # 2. ABRE O LOG PARA LEITURA E O RELATORIO PARA ANEXAÇÃO
    # sys.argv[1] é o arquivo que você passa via CLI
    with open(sys.argv[1], "r") as log, open("erros.txt", "a") as saida:
        for linha in log:
            # PADRONIZA A LINHA PARA MAIÚSCULAS APENAS NA CHECAGEM
            if palavra in linha.upper():
                saida.write(linha)  # GRAVA A LINHA ORIGINAL
                total_erros += 1

    print(f"Linhas adicionadas ao arquivo erros.txt")
    print(f"Total de erros salvos: {total_erros}")

except OSError as e:
    # O 'f' antes das aspas permite usar {e} para mostrar o erro real do sistema
    print(f"ERRO DE INFRAESTRUTURA: {e}")
    sys.exit(1) 

finally:
    print("--- Processo de auditoria encerrado! ---")
