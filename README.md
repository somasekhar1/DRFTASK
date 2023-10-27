Step 1: Create the Model

Ensure you have Django installed and set up in your project.
Create an Employee model in your Django application. This model will define the structure of your employee data.

Step 2: Apply Migrations

Run the following commands to create database tables based on your model:

python manage.py makemigartions

python manage.py migrate

step 2: run the application

Start the development server to run your application:

python manage.py runserver

step 3: Insert the data 

You can use the provided API to insert data for employees:

api: http://127.0.0.1:8000/create_employee/

sampl data :-
{
  "name": "soma",
  "email": "soma@gmail.com",
  "age": 27,
  "gender": "male",
  "phoneNo": "123-456-7890",
  "addressDetails": {
    "hno": "123 Main St",
    "street": "Apt 4B",
    "city": "New York",
    "state": "NY"
  },
  "workExperience": [
    {
      "companyName": "ABC Inc",
      "fromDate": "2018-01-01",
      "toDate": "2021-12-31",
      "address": "123 Company St, New York, NY"
    }
  ],
  "qualifications": [
    {
      "qualificationName": "Bachelor's Degree",
      "fromDate": "2014-09-01",
      "toDate": "2018-05-31",
      "percentage": 85.5
    }
  ],
  "projects": [
    {
      "title": "Project X",
      "description": "Developed a web application for client X."
    }
  ],
  "photo": "base64_encoded_image_data"
}


step 4: update the records

You can update employee records using the API:

api: http://127.0.0.1:8000/update_employee/{regid}/

ex: http://127.0.0.1:8000/update_employee/1/

data:

{
  "name": "somasekhar",
  "email": "somasekhar@gmail.com",
  "age": 27,
  "gender": "male",
  "phoneNo": "123-456-7890",
  "addressDetails": {
    "hno": "123 Main St",
    "street": "Apt 4B",
    "city": "New York",
    "state": "NY"
  },
  "workExperience": [
    {
      "companyName": "ABC Inc",
      "fromDate": "2018-01-01",
      "toDate": "2021-12-31",
      "address": "123 Company St, New York, NY"
    }
  ],
  "qualifications": [
    {
      "qualificationName": "Bachelor's Degree",
      "fromDate": "2014-09-01",
      "toDate": "2018-05-31",
      "percentage": 85.5
    }
  ],
  "projects": [
    {
      "title": "Project X",
      "description": "Developed a web application for client X."
    }
  ],
  "photo": "base64_encoded_image_data"
}


step 5: To get the single record 

To get employee records, you can use the following endpoints:

To get a single employee record:

API: http://127.0.0.1:8000/get_employee/?regid={regid}

Example: http://127.0.0.1:8000/get_employee/?regid=1

To get all employee records:

API: http://127.0.0.1:8000/get_employee

step 6: To delete the records

You can delete employee records using the API:


api: 
http://127.0.0.1:8000/delete_employee/

REQUEST JSON FORMAT:
{
  "regid": "1"
}


