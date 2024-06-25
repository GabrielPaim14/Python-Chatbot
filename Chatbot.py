import random
import unidecode

name = "Chatbot"
greetings = ["Olá!", "E aí", "Oi", "Saudações"]
goodbyes = ["Tchau", "Adeus", "Até logo", "Até breve"]

keywords = ["musica", "pet", "livros", "jogos", "nome"]
responses = [
            "Música é tão relaxante", 
            "O cachorro é o melhor amigo do homem", 
            "Eu sei muita coisa sobre livros", 
            "Eu gosto de jogar videogame",
            "Meu nome é " + name
            ]

print(name + ": "+ random.choice(greetings))

user = input("Diga alguma coisa (ou digite adeus para sair): ")

user = user.lower()
user = unidecode.unidecode(user)

while (user != "adeus"):
    keyword_found = False
    
    for index in range(len(keywords)):
        if (keywords[index] in user):
            print(name + ": " + responses[index])
            keyword_found = True
    
    if (keyword_found == False):
        new_keyword = input("Eu não sei como responder isso. Qual palavra chave eu deveria responder? ")
        keywords.append(new_keyword)
        new_response = input("Como eu deveria responder" + new_keyword + "? ")
        responses.append(new_response)
        
    user = input("Diga alguma coisa (ou digite adeus para sair): ")
    user = user.lower()
    
print(name + ": " + random.choice(goodbyes))