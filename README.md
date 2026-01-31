# Lab Submission: Dockerizing Data Analytics Workflows
**Student:** Clyde

## Modifications for Lab 1:
- **Functionality**: Replaced "Hello World" with a dynamic data processing script using Pandas.
- **Dependency Management**: Added `requirements.txt` to handle external library installation within the container.
- **Industry Use Case**: Implemented a "Cloud Cost Analysis" (EcoPulse) logic to simulate a real-world MLOps optimization task.
- **Performance Optimization**: Switched to the `python:3.11-slim` base image for a smaller, faster container footprint.

## How to Run:
1. **Build the image**: `docker build -t cloud-analysis-lab .`
2. **Run the container**: `docker run cloud-analysis-lab`
