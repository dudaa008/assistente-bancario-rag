# Assistente Bancário com RAG

Assistente de perguntas e respostas sobre temas bancários (Pix, débito, crédito, Open Finance) que responde **somente** com base em uma base de conhecimento própria e diz "não sei" quando a informação não está nela.

## Como funciona
1. Lê o arquivo faq.txt (base de conhecimento).
2. Recebe a pergunta no terminal.
3. Envia ao modelo Gemini a pergunta junto com a base, com a regra de responder só com essas informações.

## Tecnologias
Python, API do Gemini (google-genai)

## Como rodar
Instalar o Python, pip install google-genai, criar a chave no Google AI Studio, guardar em GEMINI_API_KEY, rodar python teste.py]

## Exemplos
Pergunta: Qual a difrença de crédito e débito?
Resposta: Débito: Quando o pagamento é realizado no débito, significa que a pessoa pagou com o dinheiro que tinha na conta e a tranação ocorre de forma imediata.
          Crédito: Quando o pagamento é realizado no crédito, significa empréstimo de curto prazo feito pelo banco. Você gasta um limite concedido pela instituição e paga o total acumulado depois (na fatura), podendo parcelar

Pergunta: Qual a capital da França?
Resposta: Não sei.

## Limitações
A qualidade da resposta depende da base de conhecimento. Informações devem ser revisadas e datadas.

## Próximos passos
Colocar mais informações, esse foi só um pequeno projeto para, futuramente pretendo deixar mais informativo.