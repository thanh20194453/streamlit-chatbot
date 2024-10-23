FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which the Streamlit app will run (default is 8501)
EXPOSE 8501

# Set the entry point to run the Streamlit app
CMD ["streamlit", "run", "--server.port", "8501", "app.py"]
