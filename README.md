# GPT-Based-Question-Generation# Question Generation API

A FastAPI-based API that generates domain-specific interview questions.

## Features

- Generate interview questions
- Domain validation
- Error handling
- Swagger API documentation

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Run

```bash
uvicorn main:app --reload
```

## API Documentation

```text
http://127.0.0.1:8000/docs
```

## Example Request

```json
{
  "domain": "Java"
}
```

## Example Response

```json
{
  "question": "Explain JVM architecture."
}
```

## Supported Domains

- Java
- Python
- C++
