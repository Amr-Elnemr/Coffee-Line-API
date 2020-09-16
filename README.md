# Coffee-Line-API
An API for a coffee e-commerce App, showing and filtering line of coffee machines and custom coffee pods


## Prerequisites (Used Technologies)

* Python v3.7
* Django v3.0.5
* MongoDB v4.4.1 


## Installing
1- Install packages required:
```
  pip install -r requirements.txt
```
2- Create a database and name it 'coffee'. In terminal run:
```
  mongo
  use coffee
```
3- Export Sample data from coffee_db folder. In terminal run:
```
  mongorestore --db coffee coffee_db
```

4- In the project folder (coffee) run:
```
		python manage.py makemigrations coffeeApi
		python manage.py migrate
		python manage.py runserver
```
***
## Using the API
* Getting all Coffee Machines:
http://localhost:8000/products/machine
* Getting all Coffee Coffee pods:
http://localhost:8000/products/pod
* Filter coffee machines to by large size:
http://localhost:8000/products/machine/?size=large
* To have mutiple filters; for example: all espresso vanilla pods:
http://localhost:8000/products/pod/?size=espresso&flavor=vanilla

Filtering Params | Expected values
------------ | -------------
size | small, large, espresso
water_line_compatible | True, False
model | base, premium, deluxe
pack_size | 1,3,5,7
flavor | vanilla, caramel, psl, mocha, hazelnut

