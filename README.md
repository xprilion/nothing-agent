# Agent-Based FastAPI Application

This project provides a simple framework for creating and deploying agents using the `google-adk` library, exposed via a FastAPI web interface. The application is containerized using Docker for easy deployment.

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Local Development](#local-development)
  - [Docker](#docker)
- [Project Structure](#project-structure)
- [Agents](#agents)
  - [Weather & Time Agent](#weather--time-agent)
  - [Aniket Agent](#aniket-agent)
- [API Endpoints](#api-endpoints)
- [Customization](#customization)

## Project Overview

This project demonstrates how to build and serve multiple agents, each with its own set of tools and capabilities. It uses:

- **FastAPI:** For creating the web server and API endpoints.
- **Google ADK:** For building the agents.
- **Docker:** For containerizing the application.
- **uv:** For python package management.

## Prerequisites

- Python 3.12+
- Docker (optional, for containerized deployment)
- `uv` (optional, for local development)

## Getting Started

### Local Development

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    Or with `uv`:

    ```bash
    uv pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```
    The application will be available at `http://127.0.0.1:8000`.

### Docker

1.  **Build the Docker image:**

    ```bash
    docker build -t agent-app .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 8080:8080 agent-app
    ```
    The application will be available at `http://localhost:8080`.

## Project Structure

```
.
├── aniket_agent/     # Contains the 'aniket_agent'
│   └── agent.py
├── base_agent/       # Contains the 'weather_time_agent'
│   └── agent.py
├── .gitignore
├── Dockerfile        # Docker configuration
├── main.py           # FastAPI application entry point
└── requirements.txt  # Python dependencies
```

## Agents

The application currently hosts two agents:

### Weather & Time Agent

- **File:** `base_agent/agent.py`
- **Description:** Provides the current time and weather for a given city.
- **Tools:**
  - `get_weather(city: str)`: Returns the weather for a city.
  - `get_current_time(city: str)`: Returns the current time for a city.
- **Note:** The functionality is currently hardcoded for "New York".

### Aniket Agent

- **File:** `aniket_agent/agent.py`
- **Description:** A placeholder agent with no specific functionality.

## API Endpoints

The FastAPI application exposes several endpoints for interacting with the agents. You can explore them by visiting the interactive API documentation at `http://localhost:8000/docs` (or the appropriate host and port).

## Customization

To add a new agent:

1.  Create a new directory (e.g., `my_agent/`).
2.  Inside the new directory, create an `agent.py` file.
3.  Define your agent in `agent.py` using the `google.adk.agents.Agent` class.
4.  The application will automatically discover and load the new agent.
