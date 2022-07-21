# Descrição
Este diretório tem o objetivo de demonstrar alguns conhecimentos na cloud GCP.

# Proposta do problema
Imagine que o Json das notas fiscais da pasta nfe deste projeto é disponibilizado em uma API. Utilizando as tecnologias da GCP, crie uma arquitetura para para ingerir, transformar e, eventualmente, carregar esses dados no big table.

# Arquitetura
![architecture](https://github.com/jfrsbg/sql-spark-python-gcp/blob/main/gcp/Architecture.jpg)
# Definição da Solução
A ideia desta arquitetura é realizar a ingestão dos dados da API utilizando a biblioteca flask para construir uma aplicação que faça o consumo desta API. Após o consumo, o dado será disponibilizado em um datalake para posteriormente ser processado e carregado no BigQuery.

Essa arquitetura adota o modelo de ELT, e foi pensando para um paradigma de DataLake. Datalakes são repositórios centrais de dados onde podemos concentrar todas as informações de uma empresa em um unico local, passando a ter uma "fonte única de verdade". A ideia de ter um Datalake é justamente a evolução futura de uma empresa com a mentalidade data-driven.


## Breakdown em cada step
A primeira camada da nossa arquitetura é o Cloud Composer, que é a aplicação de orquestração de data pipelines da Google, construída em cima do Apache Airflow. Essa ferramenta nos da liberdade de criar DAGs (Direct Acyclic Graph) com a linguagem python para realizar a orquestração de todo o nosso fluxo de dados. Com essa ferramenta, podemos criar um fluxo ponta a ponta e fazer as coisas "andarem" dentro da nossa arquitetura.

Para armazenar todos os nossos dados, utilizamos o serviço Cloud Storage, incluindo desde arquivos .txt até arquivos .avro e .parquet, e também para evoluirmos os nossos dados entre as camadas Raw, Staged, Curated e Analytics.

O primeiro serviço que será chamado pelo Composer (Via SimpleHttpOperator dentro da nossa DAG) é o Cloud Run, que estará rodando uma aplicação Flask e fornecendo um Endpoint http. Esse endpoint é quem sera responsavel por fazer os requests na nossa API Source e então armazenar os nossos dados dentro da camada Raw do datalake. O motivo da escolha do cloud run ao invés de cloud function é pelo seu timeout e quantidade de requests que eles podem receber. Se a API estiver nos retornando muito dado, o cloud run irá lidar melhor com essa volumetria.

Quando os dados estiverem na camada RAW, iremos chamar nossas operações de processamento do Cloud Dataproc utilizando PySpark. Aqui utilizaremos o operator DataprocSubmitJobOperator, por isso, temos como base que o cluster dataproc ja está provisionado. Iremos utilizar as tasks para criar 1 job para cada evolução. Sainda da camada raw para a staged, a unica coisa que faremos é deixar todos os dados em um mesmo formato, que é parquet. Isso se deve pois o parquet é um arquivo que trabalha muito bem com processamento paralelo, e é compativel com inúmeras ferramentas do mercado. A zona staged não recebe nenhum processamento, apenas iremos ter os dados em parquet. 

O proximo passo, ao evoluir os dados da camada Staged para Curated, é onde o nosso script de transformação entra em ação.

Saindo da curated para a analytics, podemos fazer algum enriquecimento dos dados, joins e afins e então o dado estara pronto para consumo.

O último passo é basicamente carregar os dados para o BigQuery. Aqui temos como base que o dataset e a table já estão previamente criadas no BQ. Utilizaremos o operator GCSToBigQueryOperator para trazer os dados da camada Analytics para o Bigquery. Esse operator usa o comando `bq load` por trás, fazendo o serviço de carregamento dos dados.