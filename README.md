# cosmocloud-task
Library Managment API development task
Deployed on :https://hub.docker.com/r/arnavjyo/libmanage

# Library Management System API Endpoints

## Welcome Message
- **URL**: /
- **Method**: GET
- **Response**: 
    ```json
    {
        "message": "Welcome to the Library Management System API"
    }
    ```

## Create Student
- **URL**: /api/students
- **Method**: POST
- **Request Body**: 
    ```json
    {
        "full_name": "string",
        "username": "string",
        "age": integer,
        "address": {
            "city": "string",
            "country": "string"
        },
        "interests": ["string1", "string2"]
    }
    ```
- **Response**:
    - Status Code: 201 Created
    - Body:
        ```json
        {
            "student_id": "string",
            "full_name": "string",
            "username": "string",
            "age": integer,
            "address": {
                "city": "string",
                "country": "string"
            },
            "interests": ["string1", "string2"]
        }
        ```
## List Students
- **URL**: /api/students
- **Method**: GET
- **Query Parameters**:
    - `country` (optional): Filter students by country.
    - `age` (optional): Filter students by minimum age.
    - `interests` (optional): Filter students by interests.
- **Response**: 
    - Status Code: 200 OK
    - Body:
        ```json
        {
            "data": [
                {
                    "full_name": "string",
                    "username": "string",
                    "age": integer,
                    "address": {
                        "city": "string",
                        "country": "string"
                    },
                    "interests": ["string1", "string2"]
                },
                ...
            ]
        }
        ```

## Get Student by ID
- **URL**: /api/students/{id}
- **Method**: GET
- **Path Parameters**:
    - `id`: Student ID
- **Response**: 
    - Status Code: 200 OK
    - Body:
        ```json
        {
            "student_id": "string",
            "full_name": "string",
            "username": "string",
            "age": integer,
            "address": {
                "city": "string",
                "country": "string"
            },
            "interests": ["string1", "string2"]
        }
        ```

## Update Student by ID
- **URL**: /api/students/{id}
- **Method**: PATCH
- **Path Parameters**:
    - `id`: Student ID
- **Request Body**: 
    ```json
    {
        "full_name": "string",
        "username": "string",
        "age": integer,
        "address": {
            "city": "string",
            "country": "string"
        },
        "interests": ["string1", "string2"]
    }
    ```
- **Response**: 
    - Status Code: 204 No Content

## Delete Student by ID
- **URL**: /api/students/{id}
- **Method**: DELETE
- **Path Parameters**:
    - `id`: Student ID
- **Response**: 
    - Status Code: 200 OK
    - Body:
        ```json
        {
            "message": "Student deleted successfully"
        }
        ```
