# vehicle-rent-app
REST API (Django REST Framework) [In future: Frontend in Vue.js]

VehicleRent REST API is located on URL: `api.vehiclerent.radoslawh.pl` and can be splitted into two main routers: `/users` and `/adverts`.
To use all the VehicleRent API methods, you must create an account first via website `/accounts/register/` or put `username`, `password1` and `password2` params in 
POST request at path `

# **USERS**

Show all registered users
----
Returns json data list with all registered users in application

* **URL:**
  /users/

* **Method:**
  `GET`
 
* **Success Response:**
  * **Code:** 200 <br />
  * **Content:** `[
        {
            "id": 1,
            "username": "admin",
            "email": "admin@admin.pl"
        },
        {
            "id": 2,
            "username": "Mike Tyson",
            "email": "tyson@hotmail.com"
        }
    ]`
 
* **Error Response:**
  * **Code:** HTTP 401 UNAUTHORIZED <br />
  * **Content:** `{ detail : "Authentication credentials were not provided." }`
    
Show specific user
----
Return json data about specific user.

* **URL:**
  /user/:id/

* **Method:**
  `GET`
  
*  **URL Params**
   Required:`id=[integer]`
 
* **Success Response:**
  * **Code:** HTTP 200 OK <br />
  * **Content:** `{ id : 2, username : "Mike Tyson", email : "tyson@hotmail.com" }`
 
* **Error Response:**
  * **Code:** HTTP 404 NOT FOUND <br />
  * **Content:** `{ detail : "Not found." }`
  
# **ADVERTS**


