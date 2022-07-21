# Descrição
Este diretório tem o intuito de realizar os seguintes passos:
- Realizar o processamento do input de dados no diretório data/input/ 
- Calcular o total liquido da empresa que é 59973.46. O calculo é feito da seguinte forma: total_liquido = soma(total_bruto – desconto_percentual). 
- Adicionar o resultado do calculo em data/output/

# Descrição do conteúdo
- job.py - arquivo pyspark para execução da nossa tarefa
- Dockerfile - imagem modificada do pyspark para adicionar usuario root
- docker-compose.yml - arquivo responsável por executar o nosso job em um container
- data/input/input.json - sample de dados para poder realizar a atividade
- data/output/ - diretório que os arquivos serão disponibilizados pós processamento

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
Escolhi rodar o pyspark com docker pois é a forma mais rápida de testar a solução. Daria para provisionar um cluster na GCP ou na AWS, mas isso teria um custo muito alto pra uma demo. Fazer o spark submit e depois encerrar o node simula uma tarefa de cluster efemero, onde o job é executado e depois o cluster encerrado. 

Para essa solução realizei uma simulação de como se os dados estivessem em um dataset json, sem alterar nada de sua estrutura para deixar as coisas um pouco mais parecidas com um ambiente de produção.

Inicialmente pensei em criar módulos no terraform, provisionar um cluster dataproc (para rodar o job spark) e um recurso do cloudstorage (para armazenar o dado de input e output) para conseguir resolver o problema, tudo isso utilizando GitHub actions para fazer deploy toda vez que um merge na master acontecesse. Apesar de ser uma solução bem robusta com um reaproveitamento excelente, levaria 3x mais tempo para ser desenvolvida e tambem teria um custo envolvido. Essa opção embora seja a mais completa, foi descartada por questões de velocidade de implementação. Em um ambiente de bigdata com um grande volume de dados, com certeza daria pra olhar para solução e evolui-la muito mais.

O job.py é o arquivo que contém a classe que fará o processamento. Sem precisar acessar o container podemos fazer um spark-submit sem que o usuário tenha interação direta com o container. 

## Prós
- Fácil de testar em qualquer ambiente por estar em docker

## Contras
- Para rodar na GCP, teriamos que criar outros recursos para a aplicação funcionar diariamente
- Embora o teste local seja interessante, a imagem do pyspark não seria a melhor opção para um ambiente google cloud, já que la temos uma ferramenta chamada dataproc, que possui uma abordagem mais performática.