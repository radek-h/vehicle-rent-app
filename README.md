# vehicle-rent-app
REST API (Django REST Framework) [In future: Frontend in Vue.js]

VehicleRent REST API is located on URL: `vehiclerent.radoslawh.pl/api` and can be splitted
into two main routers: `/users` and `/adverts`.

To use all the VehicleRent API methods, you must create an account first via website 
`vehiclerent.radoslawh.pl/accounts/register/` or put `username`, `email`, `password1` and `password2` params in 
POST request at path `api/rest-auth/registration/`

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
  * **Content:** `[{"id": 1, "username": "admin", "email": "admin@admin.pl"},`
        `{"id": 2, "username": "Mike Tyson", "email": "tyson@hotmail.com"}(..)]`
 
* **Error Response:**
  * **Code:** HTTP 401 UNAUTHORIZED <br />
  * **Content:** `{ detail : "Authentication credentials were not provided." }`
    
Show specific user
----
Return json data about specific user.

* **URL:**
  /user/<id:pk>/

* **Method:**
  `GET`
  
*  **URL Params**
   Required:`id:Integer`
 
* **Success Response:**
  * **Code:** HTTP 200 OK <br />
  * **Content:** `{ "id" : 2, "username" : "Mike Tyson", "email" : "tyson@hotmail.com" }`
 
* **Error Response:**
  * **Code:** HTTP 404 NOT FOUND <br />
  * **Content:** `{ detail : "Not found." }`
  
# **ADVERTS**
Display all adverts with possibility adding an advert
----
`GET`: Return json data list with all adverts added by authenticated users
`POST`: Create an advert

* **URL:**
  /adverts/

* **Method:**
  `GET`, `POST`
  
*  **URL Params**
   Required:`None`
   
* **Data Params**
   Required:`"vehicle_type":String, `
            `"vehicle_brand":String`
            `"vehicle_model":String`
            `"city":String`
            `"price_per_day":Integer`
            `"available_from":DateField`
            `"available_to":DateField`
            `"content":String`
   Optionally: `"image":ImageField"`
 
* **`POST` Success Response:**
  * **Code:** HTTP 201 CREATED <br />

* **`GET` Success Response:**
  * **Code:** HTTP 200 OK <br />
 
* **Error Response:**
  * **Code:** HTTP 400 BAD REQUEST <br />
  
Edit, delete an user's advert
----
`GET`: Display advert specific by `slug` 
`PUT`, `PATCH`: Edit an advert created by user
`DELETE`: Delete permanently an advert created by user

* **URL:**
  /adverts/<slug:slug>/

* **Method:**
  `GET`, `PUT`, `PATCH`, `DELETE`
  
*  **URL Params**
   Required: `slug` of an advert instance
   
* **Data Params**
   Optionally:`"vehicle_type":String, `
            `"vehicle_brand":String`
            `"vehicle_model":String`
            `"city":String`
            `"price_per_day":Integer`
            `"available_from":DateField`
            `"available_to":DateField`
            `"image":ImageField"`
            `"content":String`
            
* **`GET`, `PUT`, `PATCH` Success Response:**
  * **Code:** HTTP 200 OK <br />

* **`DELETE` Success Response:**
  * **Code:** HTTP 204 NO CONTENT <br />
 
* **`PUT`, `PATCH` Error Response:**
  * **Code:** HTTP 400 BAD REQUEST <br />
  
* **`GET` Error Response:**
  * **Code:** HTTP 404 NOT FOUND <br />
  

List all orders for specific advert
----
`GET`: Return all made orders for specific advert

* **URL:**
  /adverts/<slug:slug>/orders/

* **Method:**
  `GET`
  
*  **URL Params**
   Required: `slug` of an advert instance
   
* **Data Params**
   Required: `None`

* **`GET` Success Response:**
  * **Code:** HTTP 200 OK <br />
 
* **Error Response:**
  * **Code:** HTTP 400 BAD REQUEST <br />
  
Make an order for a specific advert
----
`POST`: Create an order for specifig advert simply passing the data params

* **URL:**
  /adverts/<slug:slug>/order/

* **Method:**
  `POST`
  
*  **URL Params**
   Required: `slug` of an advert instance
   
* **Data Params**
   Required:`"order_from":DateField, `
            `"order_to":DateField, 
            `"content":String`

* **`GET` Success Response:**
  * **Code:** HTTP 201 CREATED <br />
 
* **Error Response:**
  * **Code:** HTTP 400 BAD REQUEST <br />
  
Edit, delete an user's advert
----
`GET`: Display an order specific by order's `id`
`PUT`, `PATCH`: Edit an order created by user
`DELETE`: Delete permanently an order created by user

* **URL:**
  /order/<int:pk>/

* **Method:**
  `GET`, `PUT`, `PATCH`, `DELETE`
  
*  **URL Params**
   Required: `id` of an order instance
   
* **Data Params**
   Optionally:`"order_from":DateField, `
              `"order_to":DateField, 
              `"content":String`
            
* **`GET`, `PUT`, `PATCH` Success Response:**
  * **Code:** HTTP 200 OK <br />

* **`DELETE` Success Response:**
  * **Code:** HTTP 204 NO CONTENT <br />
 
* **`PUT`, `PATCH` Error Response:**
  * **Code:** HTTP 400 BAD REQUEST <br />
  
* **`GET` Error Response:**
  * **Code:** HTTP 404 NOT FOUND <br />


