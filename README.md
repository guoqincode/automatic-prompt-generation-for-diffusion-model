<<<<<<< HEAD
# automatic-prompt-generation-for-stable-diffusion
automatic prompt generation for stable diffusion
=======
# Twitcher

This project aims to develop an application using citizen science approach to crowd-source bird population dynamics information. The application provides a platform for amateur and professional birdwatchers to upload bird sighting reports that will form a database including time, species, and location data. Scientists may use the information in the database to analyze the distribution and dynamics of bird populations. While various existing citizen science databases also provide some of these functionalities, our platform is unique because it allows birders to help each other with bird identification and implements quality control procedures based on a ranking of user contributions. Our platform will reduce the uncertainties that often hamper the use of citizen science data, provide a user-friendly platform for birdwatchers to keep track of their sightings, and foster a lively community among bird enthusiasts.

Twitcher is a web application to bridge the gaps between scientists' need for more accurate and reliable data and amateur birders' demand for an accessible bird report platform. The app will allow birders to submit bird observational reports and to ask for help in the community when having difficulties to identify birds. A birder can use the app to see what are the bird species observed in theirs cities, learn the description and distribution of various bird species, use the app to keep track of their species lists, and share their achievements on social media platforms. By creating a fun, accessible tool for amateur users, we hope our platform can attract more users to submit their bird observation reports, and ultimately providing higher quality data for professional scientists. We also decided to not have a mobile client because according to conversations with birders, most of them have a habit of carrying a notebook and recording specific locations (longitude, lattitude) and other relevant information immediately and can upload to the web client later. Also, many places of bird-sightings may not have signal to enable the submission of reports immediately.

**Advisors** 

| Name | JHU Email | GitHub Username |
| ---- | --------- | --------------- |
|  Nick Xitco    |  nxitco@jhu.edu   |   NickXitco          |

**Team**

| Name | JHU Email | GitHub Username |
| ---- | --------- | --------------- |
| Chuheng Hu     |  chu29@jhu.edu         |      chuheng001           |
| Jianing Fang      |  jfang25@jhu.edu         |   JianingFang              | 
| Gongqi Huang     |   ghuang22@jhu.edu        |   amongthestarss              | 
| Jiayi He     |  jhe48@jhu.edu         |   Elaine-He              |
| Ariel Bao     |    rbao4@jhu.edu        |     arielbr       |
|  Yuntao Li     |   yli346@jhu.edu        |    tottiliyt             |

## Installing / Getting started

A quick introduction of the minimal setup you need to get the app up & running.

```shell
git clone https://github.com/cs421sp21-homework/project-g03.git
cd project-g03
cd code

# Install all the dependencies for the frontend
cd frontend
npm install
npm start (to run)

# Direct to api folder
cd ..
cd api

# Install python modules for backend (install python3, venv first if needed)
python -m venv birdy-env
./birdy-env/bin/activate # In Windows, use '.\birdy-env\Scripts\activate' instead
pip install -r requirements.txt
flask run (to run)

# Note everytime you want to run, you need to activate virtual environment again
```

Here you should say what actually happens when you execute the code above.

## Developing

### Built With
List main libraries, frameworks used including versions (React, Angular etc...)

### Prerequisites
    Python 3.6,
    npm: 6.14.8,
    node: 12.19.0,

### Setting up Dev

Here's a brief intro about what a developer must do in order to start developing
the project further:

```shell
git clone https://github.com/cs421sp21-homework/project-g03.git
cd project-g03
cd code

# Install all the dependencies for the frontend
cd frontend
npm install

# Direct to api folder
cd ..
cd api

# Install virtual environment python modules for backend (install python3, venv first if needed)
python -m venv birdy-env
# activate python virtual environment 
./birdy-env/bin/activate # In Windows, use '.\birdy-env\Scripts\activate' instead
pip install -r requirements.txt

# Note everytime you want to run, you need to activate virtual environment again
```

And state what happens step-by-step. If there is any virtual environment, local server or database feeder needed, explain here.

### Building

There is no additional building needed

### Deploying / Publishing

We use Heroku to deploy both frontend and backend seperately

Frontend:

Install Heroku CLI in your system by running the following command. It will install the updated version of Heroku CLI into your system.

```shell
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
```
Now, get to https://www.heroku.com/ and register. After completing your registration go to the dashboard and create a new app named “twitcher”  or name of your choice.


```shell
heroku login
```
Initialize a Git repository by running the following command. Make sure you be at the top-level of your project directory.

```shell
git init
```

Add the Heroku remote
```shell
heroku git: remote -a twitcher
```

Now run the following commands to push your project to the repository.

```shell
git add.
git commit -m "First Commit"
git push heroku master
```

Finally, the web app will be deployed.

Backend:

Similar to the frontend, you need to move to `code/api` directory and push all to your backend heroku server.

## Versioning

We can maybe use [SemVer](http://semver.org/) for versioning. 

## Configuration

Here you should write what are all of the configurations a user can enter when using the project.

## Tests

Describe and show how to run the tests with code examples.
Explain what these tests test and why.

```shell
Give an example
```

## Style guide

Explain your code style and show how to check it.

## Api Reference

```shell
# Make sure to activate virtual env
cd /code/api/doc/
make html
```

## Database

Explaining what database (and version) has been used. Provide download links.

### Deploying / Publishing

auto generate doc

Once you are in the virtual environment with sphinx installed, go to ./code/api/docs and simply run
```
make html
```
to generate the documentation in `docs/build`. These docs are autogenerated from
the docstring comments in python.


Application deployed (up to date): https://rocky-anchorage-47653.herokuapp.com/

API deployed (up to date): https://cs421sp21-g03-twitcher-api.herokuapp.com/
>>>>>>> b1c03cb (first command)
