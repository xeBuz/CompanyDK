
# Endpoints

## Get all Companies

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



## Get one Company

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





## Create a new Company

  Create a new Company using POST method

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




## Edit a Company


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



## Remove a Company

  Remove any Company using DELETE method

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




## Get all Owners

  Returns JSON data about all the owners

* **URL**

  ```
  /api/owners/
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

  **Code:** 200

  **Content:**

  ```json
{
    "data": [
        {
            "company_id": 1,
            "name": "Microsoft Owner"
        },
        {
            "company_id": 2,
            "name": "Oracle Owner"
        },
        {
            "company_id": 3,
            "name": "SAP Owner"
        },
        {
            "company_id": 4,
            "name": "Amazon Owner"
        },
        {
            "company_id": 5,
            "name": "Google Owner"
        }
    ],
    "links": {
        "first": "http://0.0.0.0:5000/api/owners/?count=5&page=1",
        "last": "http://0.0.0.0:5000/api/owners/?count=5&page=4",
        "next": "http://0.0.0.0:5000/api/owners/?count=5&page=2"
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
curl -X "GET" "http://0.0.0.0:5000/api/owners/"
```




## Get one Owners

  Returns JSON data about one particular owners

* **URL**

  ```
  /api/owners/:id/
  ```

* **Method:**

  `GET`

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
        "company_id": 1,
        "name": "Microsoft Owner"
    },
    "status": {
        "code": 200,
        "message": "OK"
    },
    "success": true
}

```

* **Error Response:**

  Provide an invalid Owner ID

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
curl -X "GET" "http://0.0.0.0:5000/api/owners/1/"
```





## Get all the Company's Owners

  Returns JSON data about all the owners from a particular Company ID

* **URL**

  ```
  /api/owners/company/:id/
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
    "data": [
        {
            "company_id": 1,
            "name": "Microsoft Owner"
        },
        {
            "company_id": 1,
            "name": "Another Owner"
        }
    ],
    "links": {
        "first": "http://0.0.0.0:5000/api/owners/company/1?count=2&page=1",
        "last": "http://0.0.0.0:5000/api/owners/company/1?count=2&page=1"
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
curl -X "GET" "http://0.0.0.0:5000/api/owners/company/1"
```






## Create a new Owner

  Create a new Owner using POST method

* **URL**

  ```
  /api/owners
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
  `company_id=[integer]`

* **Success Response:**

  **Code:** 201

  **Content:**

  ```json
{
    "data": {
        "id": 21
    },
    "status": {
        "code": 201,
        "message": "Created"
    },
    "success": true
}
```

* **Error Response:**

  * Provide an invalid `company_id`


  **Code:** 400

  **Content:**

  ```json

{
    "status": {
        "code": 400,
        "message": "Bad Request"
    },
    "success": false
}
```


* **cURL Example**

```bash
curl -X "POST" "http://0.0.0.0:5000/api/owners" \
  --data-urlencode "company_id=1" \
  --data-urlencode "name=Owner Name" \
```




## Edit a Owner


  Modify any value from a Owner

* **URL**

  ```
  /api/owners/:id
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
  `company_id=[integer]`


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

  * Provide an invalid Owner ID

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


  * Provide an invalid `company_id`

  **Code:** 400

  **Content:**

  ```json

{
    "status": {
        "code": 400,
        "message": "Bad Request"
    },
    "success": false
}
```


* **cURL Example**

```bash
curl -X "PUT" "http://0.0.0.0:5000/api/owners/1" \
  --data-urlencode "name=New Owner Name"
```



## Remove a Owner

  Remove any Owner using DELETE method

* **URL**

  ```
  /api/owners/:id
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

  Provide an invalid Owner ID

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
curl -X "DELETE" "http://0.0.0.0:5000/api/owners/1"
```




