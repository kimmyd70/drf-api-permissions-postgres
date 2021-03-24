# Permissions and POSTGRESQL



### PR for this file: https://github.com/kimmyd70/drf-api-permissions-postgres/pull/3

This is Lab 32 of 401-Python (seattle-py-401n2)

Developers: Kim Damalas

Date: 20 March 2021
____________________

### Features - Django REST Framework
1. Make your site a DRF powered API as you did in previous lab.
2. Adjust project’s permissions so that only authenticated users have access to API.
3. Add a custom permission so that only author of blog post can update or delete it.
4. Add ability to switch users directly from browsable API.

### Features - Docker
NOTE Refer to demo for built out Dockerfile and docker-compose.yml examples.

1. create Dockerfile based off python:3.8-slim
2. create docker-compose.yml to run Django app as a web service.
3. enter docker-compose up --build to start your site.
add postgres 11 as a service
Note: It is not required to include a volume so that data can persist when container is shut down.
4. Go to browsable api and confirm site properly restricts users based on their permissions.

__________________

### Server and Client

- Server: running on local server
- Client: Django/Docker

____________________

### Testing

Unit testing as applicable