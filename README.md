# Desafio-Backend

## Projeto Realizado com:
  * Python, Django, djangorestframework

### Documentação

Para inciar o projeto, é necessário ativar o ambiente virtual :

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