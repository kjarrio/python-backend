# python-backend - teste

API de estudantes feito com [Django](https://www.djangoproject.com/) / [DRF](https://www.django-rest-framework.org/), de forma simples.  

## Tecnologia
- [Django](https://www.djangoproject.com/) + [Django Rest Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/) 

## Instruções

O API tem 2 containers, **escola-db** e **escola-api**: 

- **escola-db** - Banco de dados PostgreSQL
- **escola-api** - REST API feito em Python usando Django/DRF. 
    - *Esse container só inicia após do banco de dados. - Utilizando [Dockerize](https://github.com/jwilder/dockerize)*
    
Para executar com docker:

    docker-compose up -d

Parar o docker:

    docker-compose down
    
## Utilização
    
- http://localhost:8000/api/v1/estudante/ - **API de Estudantes** (JSON / Browseable API / Admin) 
- http://localhost:8000/swagger/ - **Swagger UI**
- http://localhost:8000/admin/ - **Admin**
    
## Limitações
Para simplificar testes, execução, etc:
- Não tem autenticação no API, mas para produção, usarei Token / OAuth 2.0
- Usuários e senhas estão configuradas em texto de configuração.
- Não tem configuração de build, release, ou deploy (CI).
