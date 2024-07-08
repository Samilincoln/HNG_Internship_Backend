#### Backend Stage 2 Task: User Authentication & Organisation

This task involves creating a backend application that implements user authentication and organization functionality. The application should be connected to a Postgres database server and provide endpoints for user registration, user login, and organization management. Below are the acceptance criteria and requirements for the task:

#### User Model
- Create a User model with the following properties:
  - `userId`: string (must be unique)
  - `firstName`: string (must not be null)
  - `lastName`: string (must not be null)
  - `email`: string (must be unique and must not be null)
  - `password`: string (must not be null)
  - `phone`: string

#### User Validation
- Implement validation for all fields of the User model.
- When there's a validation error, return a status code 422 with the following payload:
  ```json
  {
    "errors": [
      {
        "field": "string",
        "message": "string"
      }
    ]
  }
  ```

#### User Authentication
- Implement an endpoint for user registration.
- Hash the user's password before storing it in the database.
- Return a payload with a 201 success status code upon successful registration.
- Implement an endpoint for user login.
- Use the JWT token returned after a successful login to access protected endpoints.

#### Organization Model
- A user can belong to one or more organizations.
- An organization can contain one or more users.
- On every registration, an organization must be created.
- The name property of the organization should be the user's firstName appended with "Organisation". For example, if the user's first name is John, the organization name becomes "John's Organisation".

#### Organization Endpoints
- Implement the following endpoints for organization management:
  - [GET] /api/organizations: Get all organizations that the logged-in user belongs to or created.
  - [GET] /api/organizations/:orgId: Get a single organization record for the logged-in user.
  - [POST] /api/organizations: Create a new organization for the logged-in user.
  - [POST] /api/organizations/:orgId/users: Add a user to a particular organization.

#### Testing Requirements
- Write appropriate unit tests to cover token generation and organization-related functionalities.
- Perform end-to-end tests for the user registration endpoint to ensure it works correctly.
- The test file should be named auth.spec.ext inside a folder named tests, where ext is the file extension of your chosen language.

#### Submission
- API Hosted on a free hosting service.



Agboola Olalekan Samson
HNG Back-End Intern
