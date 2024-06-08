# Flask Application with CrewAI Integration

This project is a Flask web application that processes blood test reports using the CrewAI framework, analyzes the data, searches for relevant health articles, and sends personalized health recommendations via email.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the App](#running-the-app)
- [API Endpoints](#api-endpoints)

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
    ```plaintext
    PASSWORD=xuqs danz clla yfup
    MODEL_URL= (generate url from lightning ai of Mistrial model)
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

