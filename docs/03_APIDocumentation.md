
**Get all Companies**
----
  Returns JSON data about all the companies.

* **URL**

  ```
  /api/companies
  ```

* **Method:**

  `GET`


*  **URL Params**

   **Required:**

    None

   **Optional:**

  `page=[integer]`
  `count=[integer]`

* **Data Params**

None

* **Success Response:**
  This endpoint will return a JSON array with Companies

  **Code:** 200

  **Content:**

  ```json
    {
    "data": [
        {
            "address": "Random Address",
            "city": "Redmond",
            "country": "USA",
            "email": "contact@mns.com",
            "id": 1,
            "name": "Microsoft",
            "phone": "1-800-642-7676"
        },
        {
            "address": "Random Oracle Address",
            "city": "Redwood City",
            "country": "USA",
            "email": "info@oracle.com",
            "id": 2,
            "name": "Oracle",
            "phone": "00 1 650-506-7000"
        },
        {
            "address": "Address 123 - Floor 4th",
            "city": "Walldorf",
            "country": "Germany",
            "email": "info@sap.com",
            "id": 3,
            "name": "SAP",
            "phone": "+1-800-872-1727"
        },
        {
            "address": "No Address",
            "city": "Seattle",
            "country": "USA",
            "email": "contact@amazon.com",
            "id": 4,
            "name": "Amazon",
            "phone": "00 1 206-266-2992"
        },
        {
            "address": "Try Google Maps 143",
            "city": "Mountain View",
            "country": "USA",
            "email": "hello@google.com",
            "id": 5,
            "name": "Google",
            "phone": "1-866-246-6453"
        }
    ],
    "links": {
        "first": "http://0.0.0.0:5000/api/companies?count=5&page=1",
        "last": "http://0.0.0.0:5000/api/companies?count=5&page=3",
        "next": "http://0.0.0.0:5000/api/companies?count=5&page=2"
    },
    "status": {
        "code": 200,
        "message": "OK"
    },
    "success": true
}
```

* **Error Response:**

  None


* **cURL Example**

```bash
curl -X "GET" "http://0.0.0.0:5000/api/companies"
```



**Get one Company**
----

  Returns JSON data about one specific the companies.

* **URL**

  ```
  /api/companies/:id
  ```

* **Method:**

  `GET`

*  **URL Params**

   **Required:**

   `id=[integer]`

   **Optional:**

  `page=[integer]`
  `count=[integer]`

* **Data Params**

  None

* **Success Response:**

  **Code:** 200

  **Content:**

  ```json
  {
    "data": {
        "address": "Random Address",
        "city": "Redmond",
        "country": "USA",
        "email": "contact@mns.com",
        "id": 1,
        "name": "Microsoft",
        "phone": "1-800-642-7676"
    },
    "status": {
        "code": 200,
        "message": "OK"
    },
    "success": true
}
```

* **Error Response:**

  Provide an invalid Company ID

  **Code:** 404

  **Content:**

  ```json
{
    "status": {
        "code": 404,
        "message": "Not Found"
    },
    "success": false
}
```

* **cURL Example**

```bash
curl -X "GET" "http://0.0.0.0:5000/api/companies/1"
```





**Create a new Company**
----

  Create a new Company

* **URL**

  ```
  /api/companies
  ```

* **Method:**

  `POST`

*  **URL Params**

   **Required:**

   None

   **Optional:**

  None

* **Data Params**

  `name=[string]`
  `address=[string]`
  `city=[string]`
  `country=[string]`
  `email=[string]`
  `phone=[string]`

* **Success Response:**

  **Code:** 201

  **Content:**

  ```json
{
    "data": {
        "id": 18
    },
    "status": {
        "code": 201,
        "message": "Created"
    },
    "success": true
}
```

* **Error Response:**

  None


* **cURL Example**

```bash
curl -X "POST" "http://0.0.0.0:5000/api/companies" \
  --data-urlencode "email=test@company.com" \
  --data-urlencode "phone=1234567" \
  --data-urlencode "country=Company Country" \
  --data-urlencode "name=Company Name" \
  --data-urlencode "city=Company City" \
  --data-urlencode "address=Company Address"

```




**Edit a Company**
----

  Modify any value from a Company

* **URL**

  ```
  /api/companies/:id
  ```

* **Method:**

  `PUT`

*  **URL Params**

   **Required:**

   `id=[integer]`

   **Optional:**

  None

* **Data Params**

  `name=[string]`
  `address=[string]`
  `city=[string]`
  `country=[string]`
  `email=[string]`
  `phone=[string]`


* **Success Response:**

  **Code:** 200

  **Content:**

  ```json
{
    "data": {
        "id": 18
    },
    "status": {
        "code": 200,
        "message": "OK"
    },
    "success": true
}
```

* **Error Response:**

  Provide an invalid Company ID

  **Code:** 404

  **Content:**

  ```json
{
    "status": {
        "code": 404,
        "message": "Not Found"
    },
    "success": false
}
```




* **cURL Example**

```bash
curl -X "PUT" "http://0.0.0.0:5000/api/companies/1" \
  --data-urlencode "name=New Company Name"
```



**Remove a Company**
----

  Remove any Company

* **URL**

  ```
  /api/companies/:id
  ```

* **Method:**

  `DELETE`

*  **URL Params**

   **Required:**

   `id=[integer]`

   **Optional:**

  None

* **Data Params**

  None

* **Success Response:**

  **Code:** 200

  **Content:**

  ```json
{
    "data": {
        "id": 18
    },
    "status": {
        "code": 200,
        "message": "OK"
    },
    "success": true
}
```

* **Error Response:**

  Provide an invalid Company ID

  **Code:** 404

  **Content:**

  ```json
{
    "status": {
        "code": 404,
        "message": "Not Found"
    },
    "success": false
}
```


* **cURL Example**

```bash
curl -X "DELETE" "http://0.0.0.0:5000/api/companies/1"
```




