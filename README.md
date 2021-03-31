(Lab #33 update at bottom)
(Lab #34 update at bottom)

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

________________

# Authentication and production

### PR for this file: https://github.com/kimmyd70/drf-api-permissions-postgres/pull/4

This is Lab 33 of 401-Python (seattle-py-401n2)

Developers: Kim Damalas

Date: 25 March 2021
____________________

### Features - Django REST Framework
1. Add JWT Authentication to your API.

    - Install needed libraries in project configuration and/or site settings.
2. Keep any pre-existing authentication so DRF Browsable API still usable.

    - Install needed libraries in project configuration and/or site settings.


### Features - Docker
1. Create a boilerplate Dockerfile and docker-compose.yml so you don’t need to start from scratch each time.

    - E.g. as a VS Code snippet, or a gist.
2. Switch to using Gunicorn instead of Django’s built in development server.

    - mind the number of workers to avoid sluggishness
3. Warning You will run into styling issues when you switch over to Gunicorn.

    - On Django side you’ll need to properly handle static files using Whitenoise
__________________

### Storage Options

1. Your choice of SQLite or PostgreSQL (I chose postgres)

2. Adjust docker-compose.yml so that data is persisted in a volume outside of container.
    - These steps are different depending on whether SQLite or PostgreSQL is being used.
    - *** Use [this article](https://medium.com/analytics-vidhya/getting-started-with-postgresql-using-docker-compose-34d6b808c47c)

________________

### Server and Client

- Server: running on local server
- Client: Django/Docker

____________________

### Testing

- Include steps to manually test using httpie or Postman

- No Unit testing required

________________

> As allowed by Roger in class:  I chose to extend this project on a different branch vs create from scratch

___________________

# Deployment (to Heroku)

### PR for this file: https://github.com/kimmyd70/drf-api-permissions-postgres/pull/5

This is Lab 34 of 401-Python (seattle-py-401n2)

Developers: Kim Damalas

Date: 28 March 2021
____________________

### Features - .env
1. NOTE: You can use previous lab’s Application as a starting point or start from scratch.

2. Modify your application to store SECRET_KEY, ALLOWED_HOSTS, DEBUG and DATABASE information in .env file.

3. All the code changes will be in settings.py so check the demo code for Env related lines.

4. Include .env values in your Canvas submission

### Features - Deployment
1. Research web hosting sites capable of working with Docker

2. NOTE no money is required for this lab but you may choose to create a trial account.

### Other
1. Add CORS headers using django-cors-headers

2. Whitelist allowed origins

3. Handling collecting static files so that browsable API renders nicely.

4. Host database in a location other than where Django site is hosted.(see below)
__________________

### Storage Options

1. You are not required to use Poetry since the requirements.txt is being supplied.

2. However if you run into issues with supplied requirements.txt then you are responsible for rebuilding.

3. You are NOT required to use Database from an external source, but it’s nice if you do.

4. You ARE required to have Database settings read from environment variables.


    - These steps are different depending on whether SQLite or PostgreSQL is being used.
    - *** Use [this article](https://medium.com/analytics-vidhya/getting-started-with-postgresql-using-docker-compose-34d6b808c47c)

________________

### Server and Client

- Server: deployed to Heroku
- Client: Django/Docker

____________________

### Testing

- Include steps to manually test using httpie or Postman

- No Unit testing required

________________

> As allowed by Roger in class:  I chose to extend this project on a different branch vs create from scratch