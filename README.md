NOTE:
	You can implement this rest api using any one of the following method.
●	aws apigateway and lambda
●	DJANGO REST FRAMEWORK




TASK:

Description: you have to create employe  REST API for 
1.	Creating an employee
2.	Update employee
3.	Get list of all employees
4.	Delete an employee

      Note: 
●	write code using exception handling only, without exception handling we wont cosider.
●	Write comments for each method
●	Use camelCase for variables and function names
1.	Create an employe conditions:
A.	Dont allow duplicate employee registrations, check with email.
B.	Datatype of keys should be matched  as per the table, if not u have to send 400 status code bad request.
C.	Every key is required for creating an employe, if not u have to send 400 status code, bad request
D.	Method: POST

KEY AND DATATYPES
KEY	DATE TYPE
name	string
email	string
age	int
gender	string
phoneNo	string
addressDetails	dictionary
hno	string
street	string
city	string
state	string
workExeperience	List of dictionaries
companyName	string
fromDate	string
toDate	string
address	string
qualificiations	List of dictionaries
qualificationName	string
percentage	double
projects	List of dictionaries
title	string
description	string
photo	Base64 image datata

SAMPLE REQUEST JSON FORMAT
{
  "name": "xyz",
  “email”:”xyz@gmail.com”,
  "age": 25,
  "gender": "male",
  "phoneNo": "",
  "addressDetails": {
    "hno": "123",
    "street": "xyz",
    "city": "xyz",
    "state": "xyz"
  },
  "workExperience": [
    {
      "companyName": "xyz",
      "fromDate": "20-05-2019",
      "toDate": "20-09-2021",
      "address": "xyz"
    }
  ]"qualifications": [
    {
      "qualificationName": "ssc",
      "fromDate": "20-05-2012",
      "toDate": "20-05-2013",
      "percentage": 85
    }
  ],
  "projects": [
    {
      "titile": "xyz",
      "description": "description of the project"
    }
  ],
  "photo": ""
}

________________________________________

RESPONSE FORMAT:

●	If employe created then send success response like below
Status code: 200
{
	“message”:”employee created successfully”,
	“regid”:”EMP001”,
	“success”:true
}

________________________________________

●	If employe creation failed due duplicate email:
Status code : 200
{	“message”:”employe already exist”,
	“success”:false
}

________________________________________

●	 If the data type and require params missing in json, then send 
400 status code
{“message”:”invalid body request”,
“sucess”:false}

________________________________________

●	If employe creation failed due to exception
Status code : 500
{
	“message”:”employee created failed”,
	“success”:false
}

________________________________________
2. UPDATE AN EMPLOYEE
Description: you have to update an employee using regid.
REQUEST JSON FORMAT:
	Same json we used for create an employee with regid as extra key. Because we have to update employee using this key.

REQUEST METHOD: PUT


RESPONSE FORMAT:

●	If employe updated then send success response like below
Status code: 200
{
	“message”:”employee details updated successfully”,
	“success”:true
}

________________________________________

●	If employe details updation failed:
Status code : 200
{	“message”:”employe details updation failed”,
	“success”:false
}

________________________________________
●	If employee not exist with regid
Status code : 200
{	“message”:”no employee found with this regid”,
	“success”:false
}



●	 If the data type and require params missing in json, then send 
400 status code
{“message”:”invalid body request”,
“sucess”:false}

________________________________________

●	If employe updationfailed due to exception
Status code : 500
{
	“message”:”employee updation failed”,
	“success”:false
}


________________________________________
3.DELETE AN EMPLOYEE

DESCRIPTION: we have to delete an employee using regid.

REQUEST JSON FORMAT:
{
  "regid": "EMP001"
}
REQUEST METHOD: DELETE

RESPONSE JSON FORMAT:

●	If employe deleted then send success response like below
Status code: 200
{
	“message”:”employee deleted successfully”,
	“success”:true
}

________________________________________

●	If employe deletion failed:
Status code : 200
{	“message”:”employe deletion failed”,
	“success”:false
}

________________________________________
●	If employee not exist with rigid
Status code : 200
{	“message”:”no employee found with this regid”,
	“success”:false
}


________________________________________


●	 If the data type and require params missing in json, then send 
400 status code
{“message”:”invalid body request”,
“sucess”:false}

________________________________________

●	If employe deletion failed due to exception
Status code : 500
{
	“message”:”employee created failed”,
	“success”:false
}

________________________________________

4.GET EIMPLOYEE/EMPLOYEE LIST
	DESCRIPTION: if the request got with regid  then we havet to send only that employee details. If not we have to send all employee details

REQUEST FORMAT:
Single employee request : 	?regid=EMP001
All employee request: 
REQUEST METHOD: GET

RESPONSE FORMAT:
●	If we found an employee details then send like
Status code: 200
{ “message”:”employee details found”,
   “success”:true,
  “employees”:[{
  "name": "",
  "age": "",
  "gender": "",
  "phoneNo": "",
  "addressDetails": {
    "hno": "",
    "street": "",
    "city": "",
    "state": ""
  },
  "workExperience": [
    {
      "companyName": "xyz",
      "fromDate": "20-05-2019",
      "toDate": "20-09-2021",
      "address": "xyz"
    }
  ]"qualifications": [
    {
      "qualificationName": "ssc",
      "fromDate": "20-05-2012",
      "toDate": "20-05-2013",
      "percentage": 85
    }
  ],
  "projects": [
    {
      "titile": "xyz",
      "description": "description of the project"
    }
  ],
  "photo": ""
}
]
}

	
________________________________________
●	If not found employee details
Status code: 200
{
	“message”:”employee  details not found”,
	“success”:false,
           “employees”:[]
}
