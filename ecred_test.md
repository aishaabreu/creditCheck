# Desafio de codificação
Você está encarregado de implementar um aplicativo que autoriza uma transação para uma conta específica seguindo um conjunto de regras predefinidas.

## Empacotamento
As instruções sobre como criar e executar seu aplicativo devem estar presentes em um arquivo Leia-me. Junto com uma breve descrição relevante sobre as opções de design de código.

A criação e execução do aplicativo devem ser possíveis nos sistemas operacionais Unix ou Mac.

Construções "Dockerized" são bem-vindas.

Seu programa receberá uma linha json como entrada e deve fornecer uma linha json como saída para cada chamada para a função de autorização.

## Exemplo de Uso

```
$ cat operations
{ "transaction": { "id": 1, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000,
"installments": 15, "time": "2019-02-13T10:00:00.000Z"}}
{ "transaction": { "id": 2, "consumer_id": 10, "score": 100, "income": 4000, "requested_value": 10000,
"installments": 15, "time": "2019-03-13T10:00:00.000Z"}}
{ "transaction": { "id": 3, "consumer_id": 10, "score": 500, "income": 4000, "requested_value": 10000,
"installments": 0, "time": "2019-04-13T10:00:00.000Z"}}
$ authorize < operations
{ "transaction": { "id": 1, "violatios": ["compromised-income"] }}
{ "transaction": { "id": 2, "violatios": ["low-score"] }}
{ "transaction": { "id": 3, "violatios": ["minimum-installments"] }}
```

## Estado
O programa não deve confiar em nenhum banco de dados externo. O estado interno deve ser tratado por um explícito estrutura na memória. O estado deve ser redefinido no início do aplicativo.

## Operações
O programa lida com apenas uma operação:

1. Transação de crédito

## Entrada de autorização de transação
Tenta autorizar uma transação para um consumidor específico, um valor e perfil solicitados para o estado da conta e últimas transações autorizadas.

Saída

O ID da transação + quaisquer violações da regra de negócios.

Violações da regra de negócios

Você deve implementar as seguintes regras, tendo em mente que novas regras aparecerão no futuro:

- Quando o valor das prestações exceder 30% da receita: receita comprometida
- Quando a pontuação é menor que 200: pontuação baixa
- Quando o valor de prestações for menor que 6: parcelas mínimas
- Quando ocorre duas transações nos mesmos 2 minutos: transações dobradas

Exemplos

Dada uma pontuação menor que 200:

entrada:
```
{ "transaction": { "id": 2, "consumer_id": 10, "score": 100, "income": 4000, "requested_value": 10000,
"installments": 15, "time": "2019-03-13T10:00:00.000Z"}}
```
saída:
```
{ "transaction": { "id": 2, "violations": ["low-score"] }}
```

## Tratamento de erros
Nossas expectativas

Na Serasa, valorizamos códigos simples, elegantes e funcionais. Este exercício deve refletir sua compreensão disso.

Espera-se que sua solução seja de qualidade de produção, mantenedora e extensível. Portanto, vamos olhar para:

- Qualidade dos testes de unitários;
- Documentação onde necessário;
- Instruções para executar o código.

Notas gerais

Mantenha seu teste anônimo, prestando atenção a:

- o próprio código, incluindo testes e espaços para nome;
- informações do autor do controle de versão;
- comentários automáticos que seu ambiente de desenvolvimento pode adicionar.