# Flask Application with CrewAI Integration

This project is a Flask web application that processes blood test reports using the CrewAI framework, analyzes the data, searches for relevant health articles, and sends personalized health recommendations via email.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the App](#running-the-app)
- [API Endpoints](#api-endpoints)
- [Demo](#running-the-app)
  
## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.10+
- Pip (Python package installer)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/jaykakkar31/wingify.git
    cd your-repo-name
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```



## Configuration

1. **Create a `.env` file in the root directory of the project:**
    ```bash
    PASSWORD='tngu gnrx fsxk casx'  # If this password donot work create google app password    `https://myaccount.google.com/apppasswords`
    
    MODEL_URL=
    # Generate url from lightning ai of Mistral model
    # In lighting ai select studio templates search `run mistral moe`
    # Now after running the studio click on plus button on right side panel and after click select `serving` and `click on API builder` and generate api with port 11434
    # Click API builder from right panel. In api builder click new api and add api name and enable api.
    # Click api and copy the url and paste it in env.

    EMAIL='testingcrewai78@gmail.com'
    ```

2. **Set up email settings in the `.env` file with your email credentials for sending emails.**

## Running the App

1. **Start the Flask development server:**
    ```bash
    python main.py
    ```

2. **Access the application in your web browser:**
    ```plaintext
    http://127.0.0.1:8000
    ```

## API Endpoints

- **POST /upload
    - **Description:** Accepts a blood test report in PDF format and a user's email address.
    - **Request:** 
        ```json
        {
            "pdf": report.pdf,
            "email": "sample@gmail.com"
        }
        ```
    - **Response:**
        ```json
        {
            "message": "Report processed and email sent successfully."
        }
        ```

## Demo

- https://youtu.be/4Rs7jwPEFZI

