# Microservice_System_Design
This repository is a project that illustrates the implementation of a microservices-based architecture for a video-to-MP3 conversion application.This repository is a step forward in my journy to learn Kubernetes and deepen my inderstanding of Cloud computing.

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

## Acknowledgment

This project was completed following a tutorial by (Kantan Coding)[https://www.youtube.com/channel/UC5UgemAz061hkjTFHOfxNpg] on (freeCodeCamp.org)[https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ] YouTube channel. Many thanks to him and freeCodeCamp.org team for providing accessible and high-quality educational content.

