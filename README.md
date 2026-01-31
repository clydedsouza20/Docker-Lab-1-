# Docker-Lab-1-
# Lab 1: Containerizing Data Analytics Workflows

## Modification from Original Lab:
- **Functionality**: Changed from a static "Hello World" print to a dynamic data processing script using `pandas`.
- **Environment**: Added a `requirements.txt` file to demonstrate dependency management within Docker.
- **Use Case**: Implemented a Cloud Cost Analysis logic to simulate a real-world MLOps task.
- **Optimization**: Used `python:3.11-slim` as the base image to reduce container footprint.

## Instructions to Run:
1. Build: `docker build -t cloud-analysis-lab .`
2. Run: `docker run cloud-analysis-lab`
