# Exercício: Calculadora

Molde de atividade para o plugin Moodle [mod_codereview](https://github.com/jeanlucio/moodle-mod_codereview).

## Como usar (estudante)

1. Clique em **Use this template** → *Create a new repository*, e deixe-o **público**.
2. Implemente as funções em `exercicio/calculadora.py` que ainda levantam `NotImplementedError`.
3. Faça `commit` e `push`. O GitHub Actions roda sozinho a cada push.
4. Na aba **Actions**, confira o resultado e copie o **SHA completo** do commit.
5. No Moodle, envie a URL deste repositório e esse SHA.

> O repositório precisa ser **público**: é assim que a atividade consegue ler o resultado das
> checagens sem pedir acesso à sua conta.

## Como funciona a nota

O workflow tem **um job por critério avaliado**. Cada job vira uma checagem independente, e a
atividade conta quantas passaram — por isso os critérios estão separados em vez de reunidos num
job só.

| Job | O que verifica |
|---|---|
| `soma` | `somar()` está correta |
| `subtracao` | `subtrair()` está correta |
| `multiplicacao` | `multiplicar()` está correta |
| `estilo` | O código segue o PEP 8 |

## Para o professor

Copie este repositório, ajuste os testes e os jobs à sua disciplina, e informe a URL dele no campo
**URL do repositório-molde** da atividade. A atividade usa os arquivos do molde como linha de base:
sem isso, o código comum a todos os estudantes seria apontado como trabalho duplicado.
