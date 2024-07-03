# Infrastructure

This directory contains the necessary components for setting up and managing the infrastructure. Each subdirectory includes its own `README.md` with detailed instructions on how to install and configure the respective component.

## Directory Structure

```
├── README.md
├── argocd
│   ├── README.md
│   └── images
│       ├── argo-dashboard.png
│       └── argo.png
├── jenkins
│   ├── README.md
│   └── images
│       └── jenkins.png
├── kubernetes
│   ├── README.md
│   └── images
│       └── Docker.png
├── mongodb
│   ├── README.md
│   ├── db.getUsers
│   ├── images
│   │   └── mongo.png
│   ├── mongo-secret.yaml
│   ├── mongodb-deployment.yaml
│   ├── use
│   └── values.yaml
└── observation
    ├── README.md
    ├── images
    │   ├── grafana1.png
    │   ├── grafana2.png
    │   └── prometheus.png
    └── prometheus-config.yaml

```


## Subdirectories

### ArgoCD
- **Description:** Contains configuration files and images for setting up ArgoCD.
- **Installation Instructions:** Refer to `argocd/README.md`.

### Jenkins
- **Description:** Contains configuration files and images for setting up Jenkins.
- **Installation Instructions:** Refer to `jenkins/README.md`.

### Kubernetes
- **Description:** Contains configuration files and images related to Kubernetes setup.
- **Installation Instructions:** Refer to `kubernetes/README.md`.

### MongoDB
- **Description:** Contains configuration files and images for setting up MongoDB.
- **Contents:**
  - `db.getUsers`: Script for managing users in MongoDB.
  - `mongo-secret.yaml`: Secret configuration for MongoDB credentials.
  - `mongodb-deployment.yaml`: Deployment configuration for MongoDB.
  - `use`: Directory with additional usage instructions.
  - `values.yaml`: Values file for MongoDB configuration.
- **Installation Instructions:** Refer to `mongodb/README.md`.

### Observation
- **Description:** Contains configuration files and images for monitoring tools like Grafana and Prometheus.
- **Contents:**
  - `prometheus-config.yaml`: Configuration for Prometheus.
- **Installation Instructions:** Refer to `observation/README.md`.

## Images
Each subdirectory may contain images to help visualize the setup process. Refer to the `images` folder within each subdirectory for more details.
