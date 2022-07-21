# Descrição
Este diretório tem o intuito de realizar os seguintes passos:
- Realizar o processamento do input de dados no diretório data/input/
- Transformar os dados disponíveis em arquivo Json para o formato de dataframe. Após transformar esse Json em dataframe é possível perceber que a coluna "item_list" está como dicionário. Aqui, precisamos ter dois pontos de atenção:
    - Expandir a coluna num mesmo dataframe;
    - Normalizar os itens dessa coluna de dicionário e dividí-los em dois dataframes separados, seguindo o modelo relacional.
- Adicionar o resultado do calculo em data/output/

# Descrição do conteúdo
- job.py - arquivo pyspark para execução da nossa tarefa
- Dockerfile - imagem modificada do pyspark para adicionar usuario root
- docker-compose.yml - arquivo responsável por executar o nosso job em um container
- data/input/records.json - sample de dados para poder realizar a atividade
- data/output/expanded - diretório que recebe o resultado do primeiro requisito
- data/output/items - diretório que recebe o resultado do segundo requisito (itens separados do dataset)
- data/output/nfe - diretório que recebe o resultado do segundo requisito (apenas registros de nfe)

# Execução
Para executar o projeto, se posicione na pasta pyspark deste projeto. O primeiro passo é buildar a imagem do docker:
```bash
docker build -t pyspark .
```

Depois disso podemos fazer o processamento:
```bash
docker-compose run --rm spark
```
depois de rodar os jobs o container irá bloquear seu diretório. Para libera-lo, digite:
```bash
sudo chown -R $USER:$USER $PWD
```

# Metodologia
Utilizar o PySpark para realizar a normalização dos dados tendo como fonte um json tornam as coisas muito mais fáceis e rápidas. Isso porque a API do Spark consegue ler JSON nativamente. Pensando em um ambiente de bigdata, o PySpark seria uma das primeiras ferramentas a ser pensada para resolver o problema por questões de escalabilidade e grande capacidade em conseguir lidar com esse tipo de dado semi estruturado.

Daria para provisionar um cluster na GCP ou na AWS, mas isso teria um custo muito alto pra uma demo. Fazer o spark submit e depois encerrar o node simula uma tarefa de cluster efemero, onde o job é executado e depois o cluster encerrado. 

Para essa solução realizei uma simulação de como se os dados estivessem em um dataset json, sem alterar nada de sua estrutura para deixar as coisas um pouco mais parecidas com um ambiente de produção.

Inicialmente pensei em criar módulos no terraform, provisionar um cluster dataproc (para rodar o job spark) e um recurso do cloudstorage (para armazenar o dado de input e output) para conseguir resolver o problema, tudo isso utilizando GitHub actions para fazer deploy toda vez que um merge na master acontecesse. Apesar de ser uma solução bem robusta com um reaproveitamento excelente, levaria 3x mais tempo para ser desenvolvida e tambem teria um custo envolvido. Essa opção embora seja a mais completa, foi descartada por questões de velocidade de implementação. Em um ambiente de bigdata com um grande volume de dados, com certeza daria pra olhar para solução e evolui-la muito mais.

O job.py é o arquivo que contém a classe que fará o processamento. Sem precisar acessar o container podemos fazer um spark-submit sem que o usuário tenha interação direta com o container. 

## Prós
- Fácil de testar em qualquer ambiente por estar em docker

## Contras
- Para rodar na GCP, teriamos que criar outros recursos para a aplicação funcionar diariamente
- Embora o teste local seja interessante, a imagem do pyspark não seria a melhor opção para um ambiente google cloud, já que la temos uma ferramenta chamada dataproc, que possui uma abordagem mais performática.