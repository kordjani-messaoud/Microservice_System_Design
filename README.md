# Microservice_System_Design
This repository is a project that illustrates the implementation of a microservices-based architecture for a video-to-MP3 conversion application.

# Porpose
The purpose of this project is to gain hands-on experience in developing, deploying, and orchestrating microservices, using Kubernetes. Through this tutorial, I'm going to:
- Develop the services
- Build Docker containers
- Deploy the services on Minikube
- Scale and manage using Kubctl

# Architecture
The project is composed of five primary services, each handling a specific aspect of the video conversion process:
- ### Gateway Service: 
Acts as the entry point, routing requests to the appropriate services.
- ### Auth Service: 
Manages user authentication and access control using JWT.
- ### Converter Service: 
Responsible for extracting audio tracks from videos.
- ### Notification Service: 
Sends e-mail notifications to users once the conversion process completes.
- ### RabbitMQ Message Queue: 
Handle asynchronious message exchange between the services 

# Technologies Used
Python 
Docker
Minikube
RabbitMQ
MySQL
MongoDB