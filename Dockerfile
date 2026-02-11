FROM python:3.10-slim

# System dependencies + zstd
RUN apt-get update && apt-get install -y curl zstd

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 8501
EXPOSE 11434

# Start Ollama + Pull Model + Run Streamlit
CMD bash -c "ollama serve & sleep 5 && ollama pull gemma:2b && streamlit run ui/streamlit_app.py --server.port=8501 --server.address=0.0.0.0"
