
````markdown
# Sistema de Empréstimo de Equipamentos

Um sistema simples e funcional para gerenciamento de empréstimos de equipamentos, desenvolvido em Python com uma interface gráfica moderna usando **CustomTkinter**.

## ✨ Funcionalidades

- Cadastro de empréstimos de equipamentos
- Registro das seguintes informações:
  - Data e hora do empréstimo e da devolução
  - Número de patrimônio do equipamento
  - Nome e matrícula do solicitante
  - Sala de destino
  - Status de devolução
- Exportação dos registros para um arquivo Excel
- Armazenamento local com banco de dados SQLite

## ✅ Requisitos

- Python 3.6 ou superior
- Dependências listadas no arquivo `requirements.txt`

## 📦 Instalação

1. Clone este repositório ou baixe os arquivos:
   ```bash
   git clone https://github.com/sidneylcarneiro/programa.git
   cd programa
````

2. (Opcional, mas recomendado) Crie um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate     # Linux/Mac
   venv\Scripts\activate        # Windows
   ```

3. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Como Usar

Execute o arquivo principal para iniciar o sistema:

```bash
python app.py
```

### 🖥️ Interface

* Preencha todos os campos obrigatórios do formulário
* Marque a opção **"Devolvido"** quando o equipamento for retornado
* Use o botão **"Limpar"** para resetar os campos
* Clique em **"Exportar"** para gerar um relatório em Excel com os dados atuais

## 📁 Estrutura do Projeto

```
├── app.py             # Ponto de entrada da aplicação
├── app_class.py       # Classe principal da interface gráfica
├── database.py        # Gerenciamento do banco de dados SQLite
├── requirements.txt   # Lista de dependências
└── emprestimos.db     # Arquivo do banco de dados (gerado automaticamente)
```

## 🗃️ Banco de Dados

Os dados são armazenados automaticamente no arquivo `emprestimos.db`, criado na primeira execução do sistema.

## ⚙️ Personalização

A lista de equipamentos disponíveis pode ser modificada diretamente no parâmetro `equipamentos` dentro do construtor da classe `App`, localizado no arquivo `app_class.py`.

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

Desenvolvido por [Sidney L. Carneiro](https://github.com/sidneylcarneiro)

```
