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
- data/output/items - diretório que recebe o resultado do segundo requisito
- data/output/nfe - diretório que recebe o resultado do segundo requisito

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
Aqui, o split dos dados é muito mais facil com pyspark. Pensando em um ambiente de bigdata, o PySpark seria uma das primeiras ferramentas a ser pensada para resolver o problema. Por isso estou repetindo o mesmo processo que na pasta pyspark. 

Daria para provisionar um cluster na GCP ou na AWS, mas isso teria um custo muito alto pra uma demo. Fazer o spark submit e depois encerrar o node simula uma tarefa de cluster efemero, onde o job é executado e depois o cluster encerrado. 