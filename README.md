# Desafio-Backend

## Projeto Realizado com:
  * Python, Django, djangorestframework
  * 
### Descrição
O desafio consiste em parsear um arquivo de texto com a intenção de interpretalo e retornar uma tabela com os valores formatados com uma lista de transações e o valor total 

### Documentação


**Atenção:** O pip deve estar instalado para verificar a versão atual basta utilizar o comando :

```
pip --version
```

Para inciar o projeto, é necessário instalar ativar o ambiente virtual :
````
python -m venv venv 
````
````
.\venv\Scripts\activate
````

Para baixar as dependencias do projeto utilizar o comando no terminal

````
pip install -r requirements.txt
````

**Atenção:** É necessario completar o .env com os dados que foram exemplificados no .env.example :


Para gerar as migrações, e iniciá-las utilizar o comando abaixo no seu terminal:

````
python manage.py makemigrations
python manage.py migrate 
````

Para Iniciar o servidor basta utilizar o comando abaixo:

````
python manage.py runserver  
````
