# 🛡️ Auditor de Logs em Python (v2.0)

Script de automação desenvolvido para ambientes **DevOps e SysAdmin** focado na extração dinâmica de evidências e análise de integridade de logs.

---

## 🚀 O que há de novo?
Diferente da versão anterior, o script agora é **flexível** e **robusto**:
* **Argumentos via CLI:** Não fica mais preso a um único arquivo; você define qual log quer analisar na execução.
* **Tratamento de Erros:** Captura falhas de infraestrutura (arquivo inexistente, falta de permissão) sem "quebrar" o terminal.
* **Gestão de Recursos:** Uso de contextos (`with`) para garantir que os arquivos sejam fechados corretamente, mesmo em caso de erro.

## 🛠️ Como Funciona
1.  **Triagem Dinâmica:** Lê qualquer arquivo de texto passado como argumento.
2.  **Normalização:** Identifica o termo `"ERRO"` de forma insensível a maiúsculas/minúsculas (`.upper()`).
3.  **Persistência:** Anexa as linhas encontradas em `erros.txt`, preservando o histórico anterior.
4.  **Feedback:** Informa ao usuário o total de falhas capturadas na sessão.

## 💻 Como usar no Terminal
Agora você precisa passar o nome do arquivo de log que deseja auditar:

```bash
python3 auditoria_log.py servidor.log
```

> [!IMPORTANT]
> Se você esquecer de passar o nome do arquivo, o "Porteiro do Script" (validação de `sys.argv`) impedirá a execução e te avisará.

## 📂 Estrutura de Arquivos
* `auditoria_log.py`: O motor de automação.
* `qualquer_arquivo.log`: A fonte de dados bruta (input).
* `erros.txt`: O relatório acumulado de falhas.

## 🛡️ Tratamento de Exceções
O script utiliza blocos `try/except OSError\` para lidar com problemas comuns de sistemas de arquivos, garantindo que o processo seja encerrado de forma limpa com a cláusula `finally\`.

---

**Foco:** Automação de infraestrutura, resiliência de código e fluência em CLI.
