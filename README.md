# Meu Projeto de IA

Este projeto é uma API construída com Flask que utiliza modelos de NLP para realizar tarefas como **resumo de textos** e **perguntas e respostas**. A API pode ser usada para sintetizar informações a partir de textos longos e também para responder perguntas baseadas em um contexto fornecido.

## Índice

- [Meu Projeto de IA](#meu-projeto-de-ia)
  - [Índice](#índice)
  - [Tecnologias](#tecnologias)
  - [Instalação](#instalação)
  - [Dependências](#dependências)
  - [Configuração dos Modelos](#configuração-dos-modelos)
  - [Como Usar](#como-usar)
  - [Rotas da API](#rotas-da-api)
  - [Exemplos de Uso](#exemplos-de-uso)
    - [Resumo de Texto](#resumo-de-texto)
    - [Perguntas e Respostas](#perguntas-e-respostas)
  - [Como Testar a API](#como-testar-a-api)
    - [Usando curl](#usando-curl)
  - [FAQ](#faq)
  - [Contribuindo](#contribuindo)
  - [Links Úteis e Referências](#links-úteis-e-referências)

## Tecnologias

- Python 3.9+
- Flask
- Hugging Face Transformers
- langdetect

## Instalação

Clone o repositório e acesse a pasta do projeto:

```bash
git clone https://github.com/diegooilv/nlp-api-python.git
cd nlp-api-python
```

Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Dependências

O arquivo [`requirements.txt`](requirements.txt) contém todas as bibliotecas utilizadas e suas versões:

## Configuração dos Modelos

Os modelos de IA são carregados uma única vez na inicialização da aplicação, para uso em **summarization** e **question-answering**:

```python
from transformers import pipeline

print("🔄 Carregando modelos em Português (CPU-only)...")

# Summarização leve
resumidor = pipeline(
    "summarization",
    model="rhaymison/flan-t5-portuguese-small-summarization",
    tokenizer="rhaymison/flan-t5-portuguese-small-summarization",
    device=-1,                    # força CPU
    framework="pt",               # PyTorch
    max_length=512,               # ajuste conforme necessidade
    min_length=30,
    do_sample=False
)

# QA por extração de trecho
modelo_qa = pipeline(
    "question-answering",
    model="mrm8488/bert-base-portuguese-cased-finetuned-squad-v1-pt",
    tokenizer="mrm8488/bert-base-portuguese-cased-finetuned-squad-v1-pt",
    device=-1                     # força CPU
)
```

## Como Usar

Inicie o servidor Flask:

```bash
flask run
# ou
python index.py
```

Acesse a API em `http://localhost:5000`.

## Rotas da API

- **POST /resumo**

  - **Descrição**: Recebe um texto e retorna um resumo.
  - **Corpo da requisição (JSON)**:
    ```json
    { "texto": "Texto longo para ser resumido." }
    ```
  - **Resposta (JSON)**:
    ```json
    { "resumo": "Texto resumido." }
    ```

- **POST /perguntar**
  - **Descrição**: Recebe um texto (`contexto`) e uma pergunta, retornando a resposta extraída do texto.
  - **Corpo da requisição (JSON)**:
    ```json
    {
      "contexto": "Texto onde a resposta está contida.",
      "pergunta": "Qual é a capital do Brasil?"
    }
    ```
  - **Resposta (JSON)**:
    ```json
    { "resposta": "Brasília" }
    ```

## Exemplos de Uso

### Resumo de Texto

**Entrada**:

```json
{
  "texto": "O Brasil é o maior país da América do Sul, conhecido por sua diversidade cultural e geográfica."
}
```

**Saída**:

```json
{
  "resumo": "O Brasil é o maior país da América do Sul, conhecido por sua diversidade cultural e geográfica."
}
```

### Perguntas e Respostas

**Entrada**:

```json
{
  "contexto": "Cristiano Ronaldo venceu a Bola de Ouro cinco vezes, em 2008, 2013, 2014, 2016 e 2017.",
  "pergunta": "Quantas Bolas de Ouro Cristiano Ronaldo tem?"
}
```

**Saída**:

```json
{
  "resposta": "cinco"
}
```

## Como Testar a API

### Usando curl

- **Resumo**:

  ```bash
  curl -X POST http://localhost:5000/resumo \
    -H "Content-Type: application/json" \
    -d '{"texto": "Texto longo para ser resumido."}'
  ```

- **Perguntas**:
  ```bash
  curl -X POST http://localhost:5000/pergunta \
    -H "Content-Type: application/json" \
    -d '{"contexto": "O Brasil é o maior país da América do Sul. Sua capital é Brasília.", "pergunta": "Qual é a capital do Brasil?"}'
  ```

## FAQ

**P: Qual modelo de NLP vocês estão usando?**  
R: Para resumo: `rhaymison/flan-t5-portuguese-small-summarization`; para QA: `mrm8488/bert-base-portuguese-cased-finetuned-squad-v1-pt`.

**P: Preciso de GPU para rodar?**  
R: Não. O código força o uso de CPU (`device=-1`).

## Contribuindo

Se quiser contribuir, abra um issue ou envie um pull request. Sempre atualize a documentação antes de submeter.

## Links Úteis e Referências

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- [Flask Documentation](https://flask.palletsprojects.com/)
