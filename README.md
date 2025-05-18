```markdown
# Sistema de Empréstimo de Equipamentos

Um sistema simples para gerenciar empréstimos de equipamentos, desenvolvido com Python e CustomTkinter para uma interface gráfica moderna.

## Funcionalidades

- Cadastro de empréstimos de equipamentos
- Registro de informações como:
  - Data e hora do empréstimo/devolução
  - Patrimônio do equipamento
  - Nome e matrícula do solicitante
  - Sala de destino
  - Status de devolução
- Exportação dos dados para Excel
- Armazenamento em banco de dados SQLite

## Requisitos

- Python 3.6+
- Dependências listadas no `requirements.txt`

## Instalação

1. Clone o repositório ou baixe os arquivos
2. Crie um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

Execute o aplicativo principal:
```bash
python app.py
```

### Interface
- Preencha todos os campos obrigatórios
- Marque "Devolvido" quando o equipamento for retornado
- Use o botão "Limpar" para resetar o formulário
- Exporte os dados para Excel com o botão correspondente

## Estrutura de Arquivos

- `app.py`: Ponto de entrada do aplicativo
- `app_class.py`: Classe principal da interface gráfica
- `database.py`: Gerenciamento do banco de dados SQLite
- `requirements.txt`: Dependências do projeto

## Banco de Dados

Os dados são armazenados automaticamente no arquivo `emprestimos.db` (SQLite), que será criado na primeira execução.

## Personalização

Você pode modificar a lista de equipamentos editando o parâmetro `equipamentos` no construtor da classe `App`.

## Licença

Este projeto está licenciado sob a licença MIT.
```