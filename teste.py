from google import genai

client = genai.Client()

# 1. ler o arquivo de conhecimento
with open("faq.txt", encoding="utf-8") as arquivo:
    conhecimento = arquivo.read()

# 2. perguntar ao usuário
pergunta = input("Sua pergunta: ")

# 3. montar a mensagem (esta parte é sua)
mensagem = f"""Responda usando apenas as informações abaixo.
Se a resposta não estiver nelas, diga que não sabe.

INFORMAÇÕES:
{conhecimento}

PERGUNTA:
{pergunta}"""

# 4. chamar o modelo
resposta = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=mensagem,
)

print(resposta.text)