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

* **URL:**<br/>
  /users/

* **Method:**<br/>
  `GET`
  
* **URL Params**<br/>
  Required:`None`
 
* **Success Response:**<br/>
  * **Code:** HTTP 200 OK <br />
  * **Content:** `[{"id": 1, "username": "admin", "email": "admin@admin.pl"},`<br/>
        `{"id": 2, "username": "Mike Tyson", "email": "tyson@hotmail.com"}(..)]`
 
* **Error Response:**
  * **Code:** HTTP 401 UNAUTHORIZED <br />
  * **Content:** `{ detail : "Authentication credentials were not provided." }`
    
Show specific user
----
Return json data about specific user.

* **URL:**<br/>
  /user/**:id**/

* **Method:**<br/>
  `GET`
  
*  **URL Params**<br/>
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
`GET`: Return json data list with all adverts added by authenticated users <br/>
`POST`: Create an advert

* **URL:**<br/>
  /adverts/

* **Method:**<br/>
  `GET`, `POST`
  
*  **URL Params**<br/>
   Required:`None`
   
* **Data Params**
   Required:`"vehicle_type":String,`<br/>
            `"vehicle_brand":String`<br/>
            `"vehicle_model":String`<br/>
            `"city":String`<br/>
            `"price_per_day":Integer`<br/>
            `"available_from":DateField`<br/>
            `"available_to":DateField`<br/>
            `"content":String`<br/>
   Optionally: `"image":ImageField"`
 
* **`POST` Success Response:**
  * **Code:** HTTP 201 CREATED <br />

* **`GET` Success Response:**
  * **Code:** HTTP 200 OK <br />
 
* **Error Response:**
  * **Code:** HTTP 400 BAD REQUEST <br />
  
Edit, delete and display an user's advert
----
`GET`: Display advert specific by `slug`<br/>
`PUT`, `PATCH`: Edit an advert created by user<br/>
`DELETE`: Delete permanently an advert created by user<br/>

* **URL:**<br/>
  /adverts/**:slug**/

* **Method:**<br/>
  `GET`, `PUT`, `PATCH`, `DELETE`
  
*  **URL Params**<br/>
   Required: `slug` of an advert instance
   
* **Data Params**<br/>
   Optionally:`"vehicle_type":String,`<br/>
            `"vehicle_brand":String`<br/>
            `"vehicle_model":String`<br/>
            `"city":String`<br/>
            `"price_per_day":Integer`<br/>
            `"available_from":DateField`<br/>
            `"available_to":DateField`<br/>
            `"image":ImageField"`<br/>
            `"content":String`<br/>
            
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

* **URL:**<br/>
  /adverts/**:slug**/orders/

* **Method:**<br/>
  `GET`
  
*  **URL Params**<br/>
   Required: `slug` of an advert instance
   
* **Data Params**<br/>
   Required: `None`

* **`GET` Success Response:**
  * **Code:** HTTP 200 OK <br />
 
* **Error Response:**
  * **Code:** HTTP 400 BAD REQUEST <br />
  
Make an order for a specific advert
----
`POST`: Create an order for specifig advert simply passing the data params

* **URL:**<br/>
  /adverts/**:slug**/order/

* **Method:**<br/>
  `POST`
  
*  **URL Params**<br/>
   Required: `slug` of an advert instance
   
* **Data Params**<br/>
   Required:`"order_from":DateField,`<br/>
            `"order_to":DateField,`<br/>
            `"content":String`<br/>

* **`GET` Success Response:**
  * **Code:** HTTP 201 CREATED <br />
 
* **Error Response:**
  * **Code:** HTTP 400 BAD REQUEST <br />
  
Edit, delete an user's advert
----
`GET`: Display an order specific by order's `id`<br/>
`PUT`, `PATCH`: Edit an order created by user<br/>
`DELETE`: Delete permanently an order created by user<br/>

* **URL:**<br/>
  /order/**:id**/

* **Method:**<br/>
  `GET`, `PUT`, `PATCH`, `DELETE`
  
*  **URL Params**<br/>
   Required: `id` of an order instance
   
* **Data Params**<br/>
   Optionally:`"order_from":DateField, `<br/>
              `"order_to":DateField, `<br/>
              `"content":String`<br/>
            
* **`GET`, `PUT`, `PATCH` Success Response:**
  * **Code:** HTTP 200 OK <br />

* **`DELETE` Success Response:**
  * **Code:** HTTP 204 NO CONTENT <br />
 
* **`PUT`, `PATCH` Error Response:**
  * **Code:** HTTP 400 BAD REQUEST <br />
  
* **`GET` Error Response:**
  * **Code:** HTTP 404 NOT FOUND <br />


