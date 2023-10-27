set1: create a model 
python manage.py makemigartions
python manage.py migrate

step 2: run the application

python manage.py runserver

step 3: Insert the data 

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
