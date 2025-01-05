FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy project files

COPY pyproject.toml /app/
# Install dependencies
RUN poetry install

COPY . .
# Expose the application port
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", 8000]
