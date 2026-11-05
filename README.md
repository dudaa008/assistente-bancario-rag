# Assistente Bancário com RAG

Assistente de perguntas e respostas sobre temas bancários (Pix, débito, crédito, Open Finance) que responde **somente** com base em uma base de conhecimento própria e diz "não sei" quando a informação não está nela.

## Como funciona
1. Lê o arquivo `faq.txt` (base de conhecimento).
2. Recebe a pergunta no terminal.
3. Envia ao modelo Gemini a pergunta junto com a base, com a regra de responder só com essas informações.

## Tecnologias
Python, API do Gemini (google-genai)

## Como rodar
1. Instale o Python.
2. Instale a biblioteca: `pip install google-genai`
3. Crie uma chave de API no Google AI Studio.
4. Guarde a chave na variável de ambiente `GEMINI_API_KEY`.
5. Rode: `python teste.py`

## Exemplos

```
Pergunta: Qual a diferença de crédito e débito?
Resposta: Débito: o pagamento é feito com o dinheiro que a pessoa tinha na conta e a transação ocorre de forma imediata.
Crédito: é um empréstimo de curto prazo feito pelo banco, em que se gasta um limite concedido e se paga o total depois, na fatura, podendo parcelar.
```

```
Pergunta: Qual a capital da França?
Resposta: Não sei.
```

## Limitações
A qualidade da resposta depende da base de conhecimento. As informações devem ser revisadas e datadas.

## Próximos passos
- Buscar apenas os trechos mais relevantes da base (embeddings), em vez de enviar o arquivo inteiro
- Ampliar a base com novos temas, sempre com fonte e data
