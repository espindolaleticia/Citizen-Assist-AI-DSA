# Citizen Assist AI

Global Solution 2026.2 - Data Structures and Algorithms (Python)

## Integrantes

- Felipe Mitsuo Takahashi Stephano - RM570692
- Letícia Araújo Espindola - RM569308
- Milena de Aguiar Lopes Cardoso - RM570599

## Sobre o projeto

Sistema em terminal para cadastrar e consultar serviços de saúde oferecidos ao cidadão. Os registros ficam guardados em uma lista encadeada feita por nós, sem usar listas prontas do Python para armazenar os dados. A busca é linear e a ordenação usa Insertion Sort, também implementado por nós.

Cada serviço tem: id (único), título, categoria, descrição, requisitos e local de atendimento.

## Arquivos

- `citizen_assist.py`: o sistema completo (classes `Servico`, `No` e `ListaEncadeada`, mais o menu).
- `testes_passos.py`: testes dos métodos da lista (inserir, remover, atualizar, pesquisar, ordenar e análise).
- `Citizen_Assist_AI_Documentacao_DSA.pdf`: documentação, análise Big-O e tabela de testes.

## Como executar

Precisa do Python 3 instalado. Não usa bibliotecas externas.

1. Abra o terminal dentro da pasta com os arquivos.
2. Para rodar o sistema:

```
python citizen_assist.py
```

3. Para rodar os testes dos métodos da lista:

```
python testes_passos.py
```

Se o comando `python` não funcionar, use `python3`.

## Menu

| Opção | O que faz |
|-------|-----------|
| 1 | Cadastrar serviço |
| 2 | Consultar por ID |
| 3 | Atualizar serviço (Enter mantém o valor atual) |
| 4 | Excluir serviço |
| 5 | Pesquisar por título ou categoria |
| 6 | Ordenar (por id, título ou categoria) e exibir |
| 7 | Listar todos |
| 8 | Apresentar análise (total e quantidade por categoria) |
| 9 | Carregar dados de exemplo |
| 0 | Encerrar |

## Observações

- Os dados ficam só na memória, então são perdidos quando o programa fecha.
- O programa trata opção inexistente, id inválido ou duplicado, campo vazio, id não encontrado, pesquisa sem resultado e lista vazia.
