# Outfit Finder Backend

This is the backend for my outfit finder project. Here is the link to the frontend: [Outfit Finder Frontend](https://github.com/franklinnevesfilho/outfit-finder-frontend)

Here I have many microservices defined in the `docker-compose.yml` file. Each microservice is a different service that is responsible for a different part of the application.

## Microservices
main-service: This service is open to the public and is responsible for handling all requests, and redirects them to the correct service.

auth-service: This service is responsible for handling the authentication of the users. It uses JWT to authenticate the users.

