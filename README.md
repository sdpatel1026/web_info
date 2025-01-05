# Web Info
This project provides details about website based on input web_url. The application uses OpenAI and LangChain for question answering, BeautifulSoup for web scraping,fastapi as web framework, and Poetry for dependency management.

## Installation and Setup

### Prerequisites

Ensure the following are installed on your machine:

- **Python 3.10+**
- **Poetry** (for dependency management)
  - Install Poetry:
    ```bash
    pip install poetry
    ```

---

### Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-ai-scraper.git

cd fastapi-ai-scraper
```
### Creates the virtual environment
creates the virtual environment and activates it
```bash
poetry shell
```
### Install Dependencies
Using Poetry, install all required dependencies:
```bash
poetry install
```

### Environment Variables
Create a .env file in the root directory by taking reference from ```.env.example```

### Running the Application
```bash
poetry run uvicorn src.main:app --port <port>
```
The application will be available at:
http://127.0.0.1:{port}

### Testing the API
You can test the API using tools like Postman or curl.
- **Sample Request** 
    ```bash
       curl -X POST "http://127.0.0.1:8000/scrape"\
        -H "Authorization: Bearer your_secret_key"\
        -H "Content-Type: application/json" \
        -d '{"url": "https://example.com"}'     
    ```

### Deployment
#### Docker Deployment
1. Build the Docker Image:
    ```bash
    docker build -t <image_name> .
    ```
2. Run the Docker Container:   
    ```bash
    docker run -d -p 8000:8000 --env-file .env <image_name>
    ``` 