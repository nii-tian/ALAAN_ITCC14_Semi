# Feedback API

## Developed by: Christian Gil Saldua Alaan

## Overview

The Feedback API is a Flask-based web service designed to collect feedback specifically from alumni. It supports CRUD operations for feedback and utilizes an SQLite database for data storage. The API includes a unique feature where questions for different categories, such as 'alumni,' can be dynamically loaded from text files. This allows easy customization of questions for each user group.

## Database

**SQLAlchemy:**
- **pip install SQLAlchemy**

## Functionality

### Endpoints

### Endpoints

### GET METHOD

- **URL:** `/feedback`
- **Method:** GET

### Parameters

- `answer` (optional): Filter alumni feedback by answer value.

### Request Example

http: GET /feedback?answer=Computer+Science

### POST Method

- **URL:** `/feedback`
- **Method:** POST

### Request Format

Submit alumni feedback by sending a JSON payload to the API endpoint.

#### Required Fields

- `name`: Full name of the alumni.
- `category`: Should be set to "alumni" to indicate alumni feedback.
- `question`: The specific question to answer.
- `answer`: The alumni's response to the question.

#### Example Request

json
- {
  "name": "John Doe",
  "category": "alumni",
  "question": "What was your major?",
  "answer": "Computer Science"
}

## Personalized Element:

The personalized element in this API is the focus on collecting feedback specifically from alumni. The questions are tailored to gather information relevant to the alumni experience.

## Unique Feature:

One unique feature of this API is the ability to dynamically load questions for different categories from text files. This enables easy customization of questions for each user group.

## Setup

### Prerequisites

- Python 3.x
- Flask
- SQLite

### Usage

1. **Run the Flask application on Visual Studio Code/PyCharm:**

    ```terminal
    python alumni-feedback-api.py
    ```

2. **Access the API:**

   - Open your tools like Postman to interact with the API.
