# Meta-Scholar #
Here it is a meta-search engine for scholar research papers ,it combines the result of Google Scholar,Semantic Scholar and Scopus search engines with third party authentification of google api.

## Setup ##
## Using virtual environment ##
Below intructions are given for ubuntu
* Install python pip and virtualenv

```
sudo apt-get install python3 python3-pip
pip3 install virtualenv
```
* Setup virtual env and Install Django--version=1.9

```
virtualenv -p python3 venv_py3
source venv_py3/bin/activate
pip3 install django==1.9
```
* Clone repository 

```
git clone https://github.com/lavishm58/Meta-Scholar.git
cd Meta-Scholar

```

* Install dependencies needed

```
pip3 install -r requirements.txt
```

* deploying webapp to your machine

```
python manage.py migrate
python manage.py runserver
```
Now,the webapp can be opened up in localhost server,127.0.0.1:8000

# Demo app

![screenshot from 2017-07-22 05-28-55](https://user-images.githubusercontent.com/20322910/28703716-87b72cfa-7383-11e7-8742-7cc6887912d7.png)

