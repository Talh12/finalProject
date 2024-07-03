# Project Overview

**ApiWeatherApp** is a Python Flask application designed to provide real-time weather data from around the world. This project demonstrates a modern infrastructure setup, integrating a comprehensive suite of tools to deploy and monitor the application. Key components include MongoDB, Prometheus with Grafana, Kubernetes, Jenkins, and Argo CD, all working together to ensure a robust, scalable, and observable environment.

## 1. Infrastructure Installation

This section outlines the installation and configuration of the core components that support the application:

- **MongoDB**: Provides the database services for storing application data.
- **Kubernetes (K8s)**: Manages containerized applications, ensuring they run efficiently and utilize resources effectively.
- **Prometheus and Grafana**: Used for monitoring the infrastructure and applications, collecting metrics, and providing insights through visualizations.
- **Jenkins**: Automates the continuous integration and continuous delivery (CI/CD) pipeline.
- **Argo CD**: Manages Kubernetes resources in a declarative manner, ensuring reproducible and transparent deployments.

## 2. The Application

The application itself is a Flask-based web application that interacts with MongoDB. Designed to be stateless, it fits seamlessly into a Kubernetes-managed environment, allowing it to scale easily based on demand.

## 3. Deployment

The deployment process is automated using Jenkins and Argo CD:

- **Jenkins**: Handles the initial CI pipeline steps, including code checkout, Docker image building, and pushing the image to a registry.
- **Argo CD**: Deploys the application on Kubernetes using the latest Docker images and configurations defined in Helm charts.

## 4. Monitoring

Monitoring is set up using Prometheus and Grafana to provide real-time insights into the application's performance and infrastructure health:

- **Prometheus**: Collects and stores metrics as time-series data from Kubernetes and the Flask application.
- **Grafana**: Visualizes these metrics through customizable dashboards, tracking everything from system CPU and memory usage to application-specific metrics like request counts and response times.

## 5. Purpose of the Project

The primary goal of this project is to demonstrate a highly automated, scalable, and observable infrastructure setup for modern web applications. This setup enables:

- **Rapid Deployment**: Automated processes reduce the time from development to production.
- **Real-Time Monitoring and Alerting**: Ensures high availability and performance.
- **Streamlined Development Workflows**: Enhances efficiency and reduces deployment complexity.

## Conclusion

**ApiWeatherApp** serves as an example of how modern tools can be combined in a Kubernetes environment to provide a robust platform for deploying and monitoring applications effectively. This setup can be adapted and expanded to fit different use cases and environments, offering a template for building scalable and observable infrastructure for web applications.
