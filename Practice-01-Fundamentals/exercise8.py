info = {
    "personagem": "Margarida",
    "origem": "Pato Donald",
    "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}

# Exercício 8: Insira no objeto uma nova propriedade com o
# nome de chave "recorrente" e o valor "Sim". Em seguida,
# imprima o objeto no console.

info["recorrente"] = "Sim"
print(info)

# Exercício 9: Remova a propriedade cuja chave é "origem"
# e imprima o objeto no console.

del info["origem"]
print(info)
