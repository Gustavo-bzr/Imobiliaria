# 🏠 Sistema de Imobiliária

## Função do software

Sistema web para uma imobiliária que permite **adicionar, modificar e excluir clientes e imóveis**.

Foi desenvolvido em **3 camadas**:

- **Frontend:** HTML, CSS e JavaScript (`static/index.html`)
- **Backend:** Python com Flask (`app.py`)
- **Banco de dados:** SQLite (`banco.py` e `imobiliaria.db`)

## Estrutura do projeto

```
imobiliaria/
├── app.py              # Backend: rotas da API (Flask)
├── banco.py            # Banco de dados: tabelas e comandos SQL (SQLite)
├── requirements.txt    # Dependências do Python
├── README.md           # Este arquivo
├── imobiliaria.db      # Criado automaticamente na primeira execução
└── static/
    └── index.html      # Frontend: telas, estilos e JavaScript
```

## Como fazer rodar

1. Instale o **Flask**:

      pip install flask

4. Execute o sistema:

    python app.py

5. Abra no navegador:

   http://127.0.0.1:5000
   

Para encerrar, volte ao terminal e pressione `Ctrl + C`.


## Autor

**Gustavo Bezerra**
