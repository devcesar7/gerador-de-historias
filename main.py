import random  # Importa o módulo 'random' para gerar escolhas aleatórias
random.seed()  # Inicializa o gerador de números aleatórios com base no tempo atual

# Lista de templates de histórias com espaços reservados para inserção de palavras
historias = [
    "Hoje foi um dia muito {adjective}! Fui ao {place} e comprei um(a) {noun}. Depois, {verb} no parque!",
    "No {place}, encontrei um(a) {noun} {adjective} que decidiu {verb} de forma inesperada.",
    "Enquanto caminhava pelo {place}, senti-me {adjective} ao ver um(a) {noun} que estava a {verb}.",
    "A manhã estava {adjective} e eu decidi ir ao {place}. Lá, um(a) {noun} me fez {verb} sem parar.",
    "No fim do dia, fui ao {place} e, surpreendentemente, um(a) {noun} {adjective} começou a {verb}."
]

# Seleciona aleatoriamente um dos templates da lista
selected_historia = random.choice(historias)

# Solicita ao usuário que insira palavras para preencher os espaços reservados no template
adjective = input("Digite um adjetivo: ")
place = input("Digite um lugar: ")
noun = input("Digite um substantivo: ")
verb = input("Digite um verbo: ")

# Substitui os espaços reservados no template selecionado pelas palavras fornecidas pelo usuário
story = selected_historia.format(adjective=adjective, place=place, noun=noun, verb=verb)

# Exibe a história completa com as palavras inseridas pelo usuário
print(story)
