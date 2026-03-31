# 🛡️ Auditor de Logs em Python (v2.0)

Script de automação desenvolvido para ambientes **DevOps e SysAdmin** focado na extração dinâmica de evidências e análise de integridade de logs.

---

## 🛠️ O que ele faz?
O script atua como um **Filtro de Triagem**:
* **Argumentos via CLI:** Não fica mais preso a uma única pasta; você define o caminho do log que deseja analisar na execução.
* **Tratamento de Erros:** Captura falhas de infraestrutura (arquivo inexistente, falta de permissão) sem "quebrar" o terminal.
* **Gestão de Recursos:** Uso de contextos (`with`) para garantir que os arquivos sejam fechados corretamente, mesmo em caso de erro.

## 🛠️ Como Funciona
1.  **Triagem Dinâmica:** Lê qualquer arquivo de texto passado como argumento.
2.  **Normalização:** Identifica o termo `"ERRO"` de forma insensível a maiúsculas/minúsculas (`.upper()`).
3.  **Persistência:** Anexa as linhas encontradas em `erros.txt`, preservando o histórico anterior.
4.  **Feedback:** Informa ao usuário o total de falhas capturadas na sessão.

## 💻 Como usar no Terminal
Agora você precisa passar o caminho do arquivo de log que deseja auditar:

```bash
python3 auditoria_log.py caminho/da/sua/pasta_de_logs/
```

> [!IMPORTANT]
> Se você esquecer de passar o caminho do arquivo, o "Porteiro do Script" (validação de `sys.argv`) impedirá a execução e te avisará.

## 📂 Estrutura de Arquivos
* `auditoria_log.py`: O motor de automação.
* `caminho/da/sua/pasta_de_logs/`: O diretório de entrada contendo os arquivos brutos (.log) para análise.
* `erros.txt`: O relatório acumulado de falhas.

## 🛡️ Tratamento de Exceções
O script utiliza blocos `try/except OSError\` para lidar com problemas comuns de sistemas de arquivos, garantindo que o processo seja encerrado de forma limpa com a cláusula `finally\`.

## 🕒 Novidades da Versão
- Adição de carimbo de data/hora (`timestamp`) em cada linha de erro extraída.
- Melhoria na performance de leitura de arquivos grandes.
---

```
.
├── auditoria_log.py
├── README.md
└── test_logs.log
```
