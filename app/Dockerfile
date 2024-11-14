FROM python:3.8

# Install sudo and other required packages
RUN apt-get update && apt-get install -y sudo dbus


# Expose the port the app runs on
EXPOSE 8501

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./requirements.txt

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Run the Streamlit application
CMD ["streamlit", "run", "app.py"]
