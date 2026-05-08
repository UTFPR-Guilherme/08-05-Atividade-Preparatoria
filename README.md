# Atividade em Sala: Ciclo Vermelho-Verde-Refatorar

## Descrição

Este projeto implementa um calculador de desconto em Python utilizando o ciclo TDD:

1. Red: criação dos testes unitários antes da implementação.
2. Green: implementação mínima para fazer os testes passarem.
3. Refactor: aplicação do padrão de projeto Strategy sem alterar os testes.

## Problema

O sistema calcula o valor final de um produto a partir de uma política de desconto:

- Sem desconto
- Desconto percentual
- Desconto por cupom, sem permitir valor final negativo

## Como executar os testes

```bash
python -m unittest