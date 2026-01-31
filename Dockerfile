# Using a specific slim version for better industry practice
FROM python:3.11-slim

# Set a working directory
WORKDIR /usr/src/app

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script
COPY data_process.py .

# Run the modified script
CMD ["python", "./data_process.py"]
