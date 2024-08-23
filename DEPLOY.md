## 💻 Prerequisites

To run the project locally without Docker, make sure you have the following installed on your computer:

- [Python](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/)

Or, if you plan to run the project using the Docker image, make sure you have:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

It's also recommended to use a software to access the API, such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/download).

## 🚀 Installing the repository

Once you have the prerequisites met, simply clone this repository. After that, run one of the commands below.

To run without Docker, ensure the Ollama app is running and then execute these commands:

```
ollama pull llama3.1
pip install -r requirements.txt
```

To run with Docker:

```
docker-compose up
```

## ☕ Running the API

To run the API, follow these steps:

**Without Docker:**
- Ensure the Ollama app is running;
- Run `python app.py`;
- Once the API is started, you can access it at `http://localhost:5000/ask`.

**With Docker:**
- Run `docker-compose up`;
- Once the API is started, you can access it at `http://localhost:80/ask`.

To ask questions, just make a `POST` request with the body following this simple model:

```json
{ "query": "Liste as políticas de compartilhamento de dados da Starsoft" }
```

The response is a JSON which follows this model:
`
```json
{
    "answer": "A partir do texto fornecido, não há uma lista explícita de políticas de compartilhamento de dados da Starsoft. No entanto, podemos inferir algumas informações sobre como a empresa coleta, usa e protege as informações dos usuários com base na sua Política de Privacidade.\n\nAqui estão algumas delas:\n\n*   A Starsoft coletará informações quando você usar seu site ou serviços.\n*   Ela usará essas informações para fornecer, melhorar e personalizar seus serviços.\n*   A empresa também compartilhará suas informações com terceiros em certas situações, como quando necessário para cumprir leis aplicáveis ou realizar atividades de marketing.\n\nNão há uma lista específica de políticas de compartilhamento de dados no texto fornecido."
}
```