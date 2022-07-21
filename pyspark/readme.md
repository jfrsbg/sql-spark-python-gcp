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
Escolhi rodar o pyspark com docker pois também é a forma mais rápida de testar a solução. Daria para provisionar um cluster na GCP ou na AWS, mas isso teria um custo muito alto pra uma demo. Fazer o spark submit e depois encerrar o node simula uma tarefa de cluster efemero, onde o job é executado e depois o cluster encerrado. 