import random

def CriarDraconis(nivel):
    return {
        "nome": "Draconis",
        "vida": 50 + nivel * 10,
        "dano_base": 5 + nivel * 2,
        "defesa": 3 + nivel,
        "agilidade": 2 + nivel // 2,
        "habilidades": {
            "Sopro de Fogo": {
                "dano": 10 + nivel * 3,
                "cooldown": 2
            },
            "Escamas Resilientes": {
                "aumento_defesa": 5 + nivel,
                "duracao": 1
            }
        }
    }

def CriarGoblin(nivel):
    return {
        "nome": "Goblin",
        "vida": 30 + nivel * 5,
        "dano_base": 4 + nivel,
        "defesa": 2 + nivel // 2,
        "agilidade": 3 + nivel,
        "habilidades": {
            "Golpe Rápido": {
                "dano": 8 + nivel * 2,
                "cooldown": 1
            },
            "Evasão": {
                "aumento_agilidade": 2 + nivel,
                "duracao": 1
            }
        }
    }

def CriarOrc(nivel):
    return {
        "nome": "Orc",
        "vida": 70 + nivel * 10,
        "dano_base": 7 + nivel * 3,
        "defesa": 5 + nivel,
        "agilidade": 1 + nivel // 2,
        "habilidades": {
            "Bash": {
                "dano": 15 + nivel * 4,
                "cooldown": 3
            },
            "Resistência": {
                "aumento_defesa": 4 + nivel,
                "duracao": 2
            }
        }
    }

def CriarLobo(nivel):
    return {
        "nome": "Lobo",
        "vida": 40 + nivel * 6,
        "dano_base": 6 + nivel * 2,
        "defesa": 3 + nivel,
        "agilidade": 4 + nivel,
        "habilidades": {
            "Mordida": {
                "dano": 12 + nivel * 2,
                "cooldown": 1
            },
            "Aumento de Agilidade": {
                "aumento_agilidade": 3 + nivel,
                "duracao": 1
            }
        }
    }

def CriarEsqueleto(nivel):
    return {
        "nome": "Esqueleto",
        "vida": 45 + nivel * 7,
        "dano_base": 5 + nivel * 2,
        "defesa": 4 + nivel,
        "agilidade": 2 + nivel,
        "habilidades": {
            "Faca Envenenada": {
                "dano": 10 + nivel * 3,
                "cooldown": 2
            },
            "Defesa Óssea": {
                "aumento_defesa": 6 + nivel,
                "duracao": 1
            }
        }
    }

# Função Master para sortear um monstro
def CriarMonstroAleatorio(nivel):
    monstros = [
        CriarDraconis,
        CriarGoblin,
        CriarOrc,
        CriarLobo,
        CriarEsqueleto
    ]
    return random.choice(monstros)(nivel)

