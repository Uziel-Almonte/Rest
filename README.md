# Proyecto ORM con JPA

Proyecto para demostrar la funcionalidad de ORM con JPA,
preparado para ser utilizado con Heroku con Postgres.

## Utiliza:

* Javalin 6.1.3
* Hibernate 6
* JPA 3.X
* OpenApi para Javalin (https://github.com/javalin/javalin-openapi)
* La libreria requests de python

## Requiere:

* Java 17
* Gradle 8.5

## Como funciona:

* Primero correr gradlew run en una terminal aparte, se abrira localhost:7000
* Luego ir a la carpeta principal del proyecto, y ejecutar en otra terminal ``python3 student_api_client.py``
* Se mostrara error handling, se creara un estudiante de prueba y se borrara, todo con el api endpoint proporcionado en al asignacion. 
