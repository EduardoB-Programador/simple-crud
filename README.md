# Navegação/Navigation

|[Português](#português)|[English](#english)|
|:----------------------|:------------------|
|[Visão geral](#visão-geral)|[Overview](#overview)|
|[Arquivo person.py](#arquivo-personpy)|[person.py file](#personpy-file)|
|[Arquivo connectivity.py](#arquivo-connectivitypy)|[connectivity.py file](#connectivitypy-file)|
|[Arquivo main.py](#arquivo-mainpy)||

# Português

## Visão geral
Como o título do repositório propõe, este é um sistema de CRUD (do inglês: criar, ler, atualizar e deletar) bem simples, onde o objetivo é demostrar um certo domínio manipulando o banco de dados **MongoDB**. Aqui eu utilizo de python para realizar a criação de uma nova pessoa e utilizo da biblioteca **pymongo** para pegar o client do MongoDB, pegar o banco de dados a ser utilizado, pegar a coleção desejada e fazer as operações CRUD, tudo através do terminal.

## Arquivo person.py
Nesse arquivo é criada a classe `Person` com os seguintes atributos e comportamentos:

```.py
age:int
name:str
email:str
phone_number:str
registration_date:datetime.datetime

__init__(self, age:int|None = None,
    email:str|None = None,
    name:str|None = None,
    phone_number:str|None = None) -> None

#Quaisquer outros métodos são irrelevantes
```

Como o propósito dessa classe é basicamente ter alguma informação relevante e que faça sentido, ela é bem simples por sí só.

## Arquivo connectivity.py
Nesse arquivo é criada a classe `Connectivity`, e aqui, decidi criar toda a lógica relacionada ao MongoDB em sí, conseguir o client, banco de dados, coleção, além da realização das operações CRUD em sí.

O arquivo e a classe são redundantes, mas foram feitas com o objetivo de separar cada grande componente do sistema inteiro em arquivos, fica mais fácil de se localizar, a seguir se encontram os métodos da classe.

```.py

@staticmethod
get_client(connectivity_string:str) -> pymongo.MongoClient

@staticmethod
get_db(client:pymongo.MongoClient, database_string:str) -> pymongo.database.Database

@staticmethod
get_collection(db:pymongo.database.Database, collection_str:str) -> pymongo.collection.Collection

@staticmethod
insert_one(collection:pymongo.collection.Collection, person:Person) -> None

@staticmethod
delete_one(collection:pymongo.collection.Collection, query:dict) -> None

@staticmethod
update_one(collection:pymongo.collection.Collection, query:dict, values:dict) -> None

@staticmethod
update_many(collection:pymongo.collection.Collection, query:dict, values:dict) -> None

@staticmethod
find(collection:pymongo.collection.Collection, query:dict|None = None, projection:dict|None = None) -> list
```

## Arquivo main.py
Nesse arquivo está presente toda a estrutura de execução e a lógica principal, além de possuir métodos auxiliares e aqueles que remetem a cada uma das operações CRUD

Abaixo se encontra cada método criado no arquivo:

```.py
#Métodos auxiliares
person_creation() -> Person

choose_field(fields:str, numbers:list[int]) -> int

field_condition(field:str) -> dict

query_buider() -> dict

proj_dict_switch(proj_dict:dict, field:str) -> None

projection_builder() -> dict

set_unset(field:str) -> dict

update_builder() -> dict

#Métodos CRUD
create(collection) -> None

read(collection) -> None

update_one(collection) -> None

update_many(collection) -> None

delete(collection) -> None
```

Meu objetivo nesse arquivo, além de ser o responsável pela execução, era deixá-lo o mais modular possível, talvez ainda há a capacidade de deixá-lo ainda mais modular, mas estou bem feliz com o resultado no momento.

# English

## Overview
As the repository's title suggests, this is a simple CRUD (Create, Read, Update and Delete) system, where the main focus is to show a certain proficiency using the **MongoDB** database. Here I use python in order to create a new *Person* object, and utilizing the library **pymongo** to get the MongoDB client, the database that will be used and the collection. Doing also the CRUD operations via terminal. 

## person.py file
In this file the class `Person` is constructed, it has the following fields and behaviors:

```.py
age:int
name:str
email:str
phone_number:str
registration_date:datetime.datetime

__init__(self, age:int|None = None,
    email:str|None = None,
    name:str|None = None,
    phone_number:str|None = None) -> None

#Further methods are irrelevant for the functionality of the system
```

Since the purpose of this class is to carry relevant info to be stored, it is quite simple.

## connectivity.py file
In this file the class `Connectivity` is built, here I decided to build all MongoDB related methods, such as get_client, get_db, get_collection. And all queries to the database used for the CRUD.

Both the file and class purposes are redundant, but my intention here is to separate each sytem component in files, making it easier to find yourself in the system, below you can see the class' methods.

```.py

@staticmethod
get_client(connectivity_string:str) -> pymongo.MongoClient

@staticmethod
get_db(client:pymongo.MongoClient, database_string:str) -> pymongo.database.Database

@staticmethod
get_collection(db:pymongo.database.Database, collection_str:str) -> pymongo.collection.Collection

@staticmethod
insert_one(collection:pymongo.collection.Collection, person:Person) -> None

@staticmethod
delete_one(collection:pymongo.collection.Collection, query:dict) -> None

@staticmethod
update_one(collection:pymongo.collection.Collection, query:dict, values:dict) -> None

@staticmethod
update_many(collection:pymongo.collection.Collection, query:dict, values:dict) -> None

@staticmethod
find(collection:pymongo.collection.Collection, query:dict|None = None, projection:dict|None = None) -> list
```

## Arquivo main.py
This file holds the main structure to run the system, alongside it, it also holds some auxiliary methods and the CRUD methods.

Below you can see all methods built in the file:

```.py
#Auxiliary methods
person_creation() -> Person

choose_field(fields:str, numbers:list[int]) -> int

field_condition(field:str) -> dict

query_buider() -> dict

proj_dict_switch(proj_dict:dict, field:str) -> None

projection_builder() -> dict

set_unset(field:str) -> dict

update_builder() -> dict

#CRUD methods
create(collection) -> None

read(collection) -> None

update_one(collection) -> None

update_many(collection) -> None

delete(collection) -> None
```

My main focus on this file, besides making everything run flawlessly, is to make the code the as modular as possible, maybe there is still some room for improvement, but I'm happy with the current result.
