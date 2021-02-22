SMALL_FONT = ("Verdana", 8)
MEDIUM_FONT = ("Verdana", 10)
LARGE_FONT = ("Verdana", 12)
HUGE_FONT = ("Verdana", 16)

classes = {
    "Inábil": 0,
    "Normal": 1,
    "Bom": 2,
    "Habilidoso": 3,
    "Especialista": 4,
    "Incrível": 5,
    "Monstruoso": 6,
    "Épico": 7,
    "Mestre": 8,
    "Lendário": 9,
}

ShowRaca = {
    0: [1, 1, 2, 3, 3, 3, 3, 0, "Humano"],  # Humanos
    1: [1, 1, 3, 3, 3, 2, 2, 0, "Braços Longos"],  # Braços Longos
    2: [1, 1, 3, 2, 2, 3, 3, 0, "Pernas Longas"],  # Pernas Longas
    3: [1, 0, 2, 2, 2, 0, 0, 4, "Gigante"],  # Gigantes
    4: [0, 1, 2, 0, 0, 2, 2, 4, "Mink Bovino"],  # Bovinos
    5: [1, 1, 3, 2, 2, 3, 3, 0, "Mink Canino"],  # Caninos
    6: [1, 0, 3, 3, 3, 0, 0, 2, "Mink Caprino"],  # Caprinos
    7: [1, 1, 2, 2, 2, 4, 4, 0, "Mink Felino"],  # Felinos
    8: [1, 0, 3, 2, 2, 0, 0, 3, "Mink Gorila"],  # Gorila
    9: [1, 1, 2, 4, 4, 2, 2, 0, "Mink Hiena"], # Hiena
    10: [1, 1, 2, 3, 3, 3, 3, 0, "Mink Lagomorfo"],  # Lagomorfos
    11: [1, 1, 2, 3, 3, 3, 3, 0, "Mink Macaco"],  # Macaco
    12: [1, 1, 0, 4, 4, 4, 4, 0, "Mink Marsupial"], # Marsupial
    13: [1, 1, 0, 4, 4, 4, 4, 0, "Mink Roedor"],  # Roedores
    14: [0, 1, 3, 0, 0, 2, 2, 3, "Mink Suíno"], # Suínos
    15: [0, 1, 3, 0, 0, 2, 2, 3, "Mink Ursídeo"],  # Ursídeos
    16: [1, 1, 0, 4, 4, 2, 2, 2, "Mink Xenartros"], # Xenartros
    17: [1, 1, 0, 3, 3, 3, 3, 2, "Tritão Agulhão"],  # Agulhão
    18: [1, 1, 3, 3, 3, 2, 2, 0, "Tritão Cação Luminoso"],  # Cação Luminoso
    19: [0, 1, 2, 0, 0, 3, 3, 3, "Tritão Carpa"],  # Carpa
    20: [1, 1, 2, 3, 3, 3, 3, 0, "Tritão Enguia"],  # Enguia
    21: [0, 1, 4, 0, 0, 2, 2, 2, "Tritão Grande Tubarão Branco"],  # Grande Tubarão Branco
    22: [0, 1, 2, 0, 0, 3, 3, 3, "Tritão Lula"],  # Lula
    23: [1, 0, 2, 2, 2, 0, 0, 4, "Tritão Peixe Baiacu Tigre"],  # Peixe Baiacu Tigre
    24: [1, 1, 2, 4, 4, 2, 2, 0, "Tritão Peixe Kisu"],  # Peixe Kisu
    25: [1, 1, 2, 3, 3, 3, 3, 0, "Tritão Polvo"],  # Polvo
    26: [1, 1, 4, 2, 2, 2, 2, 0, "Tritão Raia"],  # Raia
    27: [1, 0, 2, 2, 2, 0, 0, 4, "Tritão Tubarão-Baleia"],  # Tubarão-Baleia
    28: [0, 1, 2, 0, 0, 3, 3, 3, "Tritão Tubarão Cabeça de Martelo"],  # Tubarão Cabeça de Martelo
    29: [0, 1, 3, 0, 0, 3, 3, 2, "Tritão Tubarão-Serra"],  # Tubarão-Serra
    30: [1, 1, 2, 3, 3, 3, 3, 0, "Tritão Tubarão Tapete Japonês"],  # TUbarão Tapete Japonês
    31: [1, 1, 2, 3, 3, 3, 3, 0, "Sireno"],  # Sireno
    32: [1, 1, 2, 2, 2, 4, 4, 0, "Celestial"],  # Celestial
    33: [1, 1, 2, 3, 3, 3, 3, 0, "Anão"],  # Anão
}

Especializacoes = {
    0: [5, 0, 0, 0, 0, 0, "Tribal Haki"],
    1: [5, 0, 0, 0, 0, 0, "Imbuir"],
    2: [5, 0, 0, 0, 0, 5, "Superioridade"],
    3: [10, 0, 0, 0, 0, 0, "Ryou Avançado"],
    4: [10, 0, 0, 0, 0, 0, "Impregnação Permanente"],
    5: [10, 0, 0, 0, 0, 10, "Corpo Completo"],
    6: [0, 0, 0, 5, 5, 0, "Foresight"],
    7: [0, 5, 5, 0, 0, 0, "Ver Auras"],
    8: [0, 0, 0, 5, 5, 0, "Emoções"],
    9: [0, 5, 5, 0, 0, 0, "Ouvir Vozes"],
    10: [0, 0, 0, 10, 10, 0, "Previsão do Futuro"],
    11: [0, 10, 10, 0, 0, 0, "A Voz de Todas as Coisas"],
}