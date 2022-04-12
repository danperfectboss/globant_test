# globant_test
This repository contain a interview test from globant

# Using VENV for the proyect
1.- Clone the repo
<br>
2.- Create a python venv with the command ***virtualenv < NAME >***
<br>
3.- Activate the VENV with the command ***source < NAME >/bin/activate***
<br>
4.- Install requirements ***pip install -r requirements.txt***
<br>
5.- Run the project with the command ***python app.py***
<br>
6.- Go into the browser to this address http://127.0.0.1:4000/
<br>
NOTE:  If some module can´t not be imported use ***pip install < NAME MODULE >***
  


# Using Docker for the proyect
1.- Clone the repo
<br>
2.- Create the image with the Dockerfile executing the command: ***docker build -t < NAME IMAGE >***  .
<br>
3.- Run the image in a container using the command: ***docker run -it -p 7000:4000 < NAME IMAGE >***
<br>
4.- Go into the browser to this address http://127.0.0.1:7000/
