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

Inicialmente pensei em criar módulos no terraform, provisionando um recurso do Google Cloud SQL do MySQL. Apesar de ser uma solução bem robusta com um reaproveitamento excelente, levaria mais tempo para ser desenvolvida e também teria um custo envolvido. Essa opção embora seja a mais completa, foi descartada por questões de velocidade de implementação. Em um ambiente de bigdata com um grande volume de dados, com certeza daria pra olhar para solução e evolui-la muito mais.

A ideia de ter 1 arquivo .sql para cada operação é para que o usuário não precise ficar fazendo conexão direta no container. Aqui é possível simplesmente enviar o comando e o container irá executar e ler todo o conteúdo do script.

## Prós
- Solução que pode ser testada rapidamente

## Contras
- Rodar um database em um container com certeza é uma das piores práticas, uma vez que temos serviços totalmente gerenciados como Cloud SQL da google. 
- Essa solução seria um anti-pattern em um ambiente de produção e por isso teriamos que criar uma solução pensando em redundância e escalabilidade. 