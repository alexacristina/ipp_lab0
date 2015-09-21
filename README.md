# Lab#0 Prototyping 

The main goal of this assignment is to create an oauth application that would represent an API with requests. For API there is necessary to be used http protocol and method GET. 

The technology used for implementation is Django framework on Python. 

The instructions to run the app are: 

* Clone repo with the project;
* Create a virtual environment;
* Install django dev version;
* Run the comamnds in oauthservice directory
```
python manage.py makemigrations
python manage.py migrate
python managy.py runserver
```
to initiate the database, migrate it and run the app.

To get the applications requests it is necessary to access them in the browser as it couldn't be handled the access using ```curl``` command.

Examples of GET request that could be put in browser to check the oAuth service application:

* Register
```
http://127.0.0.1:8000/register/?'{"client_id": "0", "email": "mail@mail.com", "pass": "qwerty", "name_surname": "username"}'
```

* Login
```
http://localhost:8000/login/? '{ "client_id":"5", "pass":"qwerty", "name_surname":"alexacris"}'
```
* Get Last Login
```
http://127.0.0.1:8000/get_last_login/?'{"client_id":"1", "name_surname": "alexacris", "token":"45b-518a91cf02c94ddb4105"}'
```
##Requirements
* Allow applications to register users

For this requirement the tasks accomplished are the following:
##### Create a model - Client in models.py that would represent the applications that use this oAuth service 

######Implementation: 
```
    class Client(models.Model):
        client_id = IntegerField(unique=True) 
```

######Technical Issues:
* The number of clients as applications is limited even it is big enough. If the application has more clients it will run out of id-s. Second, the data for each of the app is not secure. Solution: Use tokens for application id, as well.

######Improvements: 
* Add other fields of client model such as name and password for authentification.

#####Create AccessToken model that will generate token for logins of the users

######Implementation:
```
class AccessToken(models.Model):
    client = models.ForeignKeyField(Client)
    user = models.ForeignKeyField(User)
    token = CharField(default='')
```

######Technical Issues:
There are not any fields that would take different type of users and grant different type of access. The relationship of this model is not properly defined. 

######Improvements:
* Add fields for granting access for different type of users;
* Improve database schema and change the models according to this;

#####Create View classes for register, login, get_last_login and create a get method for each to process the data given in the request

######Implementation Register, Login, Get_Last_Login as classes: 
```
class NameClass():
    def get(request):
        process_data_request()
        return response_json
```

######Technical Issues:
* It is used method GET to input data of the request. This doesn't allow the application to use libraries like ```rest_framework``` or ```django-oauth-toolkit```.

######Improvements:
* Change method for input data to POST and use libraries mentioned above.

####Conclusion: 
First, it has to be admitted that this implementation of oAuth is primitive.This oAuth service could be used with apps and users, but it would be very easily corrupted and fast out of order. The apps, which are going to use it, have a limited functionality.
To improve it, it is needed to use standard libraries and technologies of creating an API, because it offers methods of implementation simple and straightforward. Also, it is necessary to broaden the functionality of the app regarding grant of access for users and clients.

  



