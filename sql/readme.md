# Descrição
Este diretório tem o intuito de realizar os seguintes passos:
- provisionar uma instância local do MySQL
- popular o database com dados fictícios de transações financeiras
- calcular o ganho total da empresa, o qual é obtido a partir da taxa administrativa do serviço de cartão de crédito para seus clientes. Esse ganho é calculado sobre um percentual das transações de cartão de crédito realizadas por eles.

# Descrição do conteúdo
- docker-compose.yml - arquivo responsável por provisionar a instancia MySQL
- create_tables.sql - arquivo que contém scripts para criação de tables e para popula-las
- calculate.sql - arquivo que contem um script para realizar o calculo em SQL da demanda
- drop.sql - arquivo que contem um script para deletar as tables para caso queira rodar mais de uma vez o projeto

# Execução
Para executar o projeto, se posicione na pasta sql deste projeto em seu terminal e então digite:
```bash
docker compose up -d
```
O comando acima ira provisionar um MySQL localmente.

A seguir, precisamos dar acesso aos arquivos do nosso diretório. Isso é necessário pois ao copiar os arquivos para dentro do container o próprio container acaba adicionando permissões indesejadas para o nosso desenvolvimento:
```bash
sudo chown -R $USER:$USER $PWD
```

O pŕoximo comando ira pegar o arquivo create_tables.sql que contém comandos SQL e irá criar tabelas e popula-las no database:

```bash
docker exec -i database mysql -u user -ppassword desafio_engenheiro < create_tables.sql
```

A seguir, para realizar o nosso cálculo e imprimi-lo na tela, digite:
```bash
docker exec -i database mysql -u user -ppassword desafio_engenheiro < calculate.sql
```

Caso queira deletar as tables por algum motivo:
```bash
docker exec -i database mysql -u user -ppassword desafio_engenheiro < drop.sql
```

# Metodologia
Pensando em facilitar, a ideia foi criar um container e deixar a instância rodando para que possamos fazer os comandos livremente. Inicialmente pensei em criar algo na nuvem, mas com isso eu não conseguiria demonstrar as minhas habilidades provisionando um database local e manipulando-o.