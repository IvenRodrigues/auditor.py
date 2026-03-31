import sys
import datetime
import os

# 1. VERIFICAÇÃO DE ARGUMENTOS
if len(sys.argv) < 2:
    print("ERRO: Informe o caminho do ARQUIVO de log (ex: /var/log/sys.log)")
    sys.exit(1)

pasta_alvo = sys.argv[1]

try:
    palavra = "ERRO"
    total_erros = 0

    # 3. ABRE O LOG PARA LEITURA E O RELATORIO PARA ANEXAÇÃO
    # sys.argv[1] é o arquivo que você passa via CLI
    with open("erros.txt", "a") as saida:
        for item in os.listdir(pasta_alvo):
            caminho_completo = f"{pasta_alvo}/{item}"
            if os.path.isfile(caminho_completo):
                with open(caminho_completo, "r") as log:
                    for linha in log:
                        if palavra in linha.upper():
                            carimbo = datetime.datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")
                            # GRAVA A LINHA ORIGINAL COM O HORÁRIO EXATO
                            saida.write(f"{carimbo} - {linha}")
                            total_erros += 1

    print(f"Linhas adicionadas ao arquivo erros.txt")
    print(f"Total de erros salvos: {total_erros}")

except OSError as e:
    # O 'f' antes das aspas permite usar {e} para mostrar o erro real do sistema
    print(f"ERRO DE INFRAESTRUTURA: {e}")
    sys.exit(1)

finally:
    print("--- Processo de auditoria encerrado! ---")
