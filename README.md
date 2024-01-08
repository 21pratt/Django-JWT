# Django-JWT
JWT authentication in the Django app

## This app contains the following endpoints
1. `localhost:8000/api/api/token` for login with JWT token Obtain Tokens (Authentication)
   a. In a terminal or command prompt, use cURL to obtain JWT tokens by sending a POST request to the /api/token/ endpoint with a valid username and password.

Replace `yourusername` and `yourpassword` with actual user credentials you've created in your Django application.
  In bash ```curl -X POST -H "Content-Type: application/json" -d '{"username": "yourusername", "password": "yourpassword"}' http://localhost:8000/api/token/
```
```This command sends a POST request to the /api/token/ endpoint with the provided credentials in JSON format. It should return a response similar to:```
``` JSON:
  {
    "access": "your_access_token",
    "refresh": "your_refresh_token"
}
```
2. `localhost:8000/api/api/`token/refresh
  a. If the access token expires, you can use the refresh token to obtain a new access token. Send a POST request to the `/api/token/refresh/` endpoint with the refresh token to get a new access token.

Replace `your_refresh_token` with the refresh token obtained in the previous step.
```curl -X POST -H "Content-Type: application/json" -d '{"refresh": "your_refresh_token"}' http://localhost:8000/api/token/refresh/
```
This command sends a POST request to the /api/token/refresh/ endpoint and should return a response with a new access token:
```JSON:
{
    "access": "new_access_token"
}
```

3. Accessing Protected Endpoints `localhost:8000/api/employees/`
  a.Once you have the access token, you can access protected endpoints by including the token in the Authorization header of your requests.
  ```curl -H "Authorization: Bearer your_access_token" http://localhost:8000/api/employees/```
  This will fetch the list of employees in the sqlite database
