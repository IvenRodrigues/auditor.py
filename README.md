# Auditor de Logs em Python 🛡️

Script de automação desenvolvido para ambientes **DevOps e SysAdmin** para extração de evidências em arquivos de log.

## 🛠️ O que ele faz?
O script atua como um **Filtro de Triagem**:
1. Lê o arquivo \`servidor.log\`.
2. Identifica linhas com o termo **"ERRO"** (independente de estar em maiúsculo ou minúsculo).
3. Salva essas linhas no arquivo \`erros.txt\` sem apagar o que já existia lá (anexação).

## 🚀 Como usar no Terminal
Execute o script com o Python 3:
\`\`\`bash
python3 auditoria_log.py
\`\`\`

## 📂 Estrutura de Arquivos
* \`auditoria_log.py\`: Código principal.
* \`servidor.log\`: Fonte dos dados (logs brutos).
* \`erros.txt\`: Relatório final com as falhas encontradas.

---
**Foco:** Automação de infraestrutura e fluência em CLI.
