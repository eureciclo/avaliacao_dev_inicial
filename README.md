# Desafio de programação inicial

Dado um conjunto de garrafas d'água, com volumes de água diferentes entre si, e um galão de água.
Crie um algoritmo, na linguagem que achar melhor, para escolher as garrafas a serem utilizadas para encher o galão, de acordo:
- 1) O galão deve ser completamente preenchido com o volume das garrafas;
- 2) Procure esvaziar totalmente as garrafas escolhidas;
- 3) Quando não for possível esvaziar todas garrafas escolhidas, deixe a menor sobra possível;
- 4) utilize o menor número de garrafas possível;

## Exemplos

1:

```
galão: 7
garrafas: 5
garrafa 1: 1
garrafa 2: 3
garrafa 3: 4.5
garrafa 4: 1.5
garrafa 5: 3.5
resposta: [1L, 4.5L, 1.5L], sobra 0L
```

2:

```
galão: 5
garrafas: 4
garrafa 1: 1
garrafa 2: 3
garrafa 3: 4.5
garrafa 4: 1.5
resposta: [1L, 4.5L]; sobra 0.5L;
```

3:

```
galão: 4.9
garrafas: 2
garrafa 1: 4.5
garrafa 2: 0.4
resposta: [4.5L, 0.4L]; sobra 0L;
```