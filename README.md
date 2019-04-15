# financial-tools
Tools for Trendings


### System dependencies

```
$ sudo apt install libmysqlclient-dev
$ sudo apt install python3.6-dev
$ sudo apt install python3-pip
$ sudo apt install python3-venv
$ pip install mysql-connector-python
```

### Install

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements-dev.txt

export FLASK_ENV=development
export FLASK_APP=main.py
```

### Running server

```
$ python main.py
$ flask run
```

### Local Google SQL
```
 ./cloud_sql_proxy -instances="ereciclar"=tcp:3306
```


### Deploy

```
gcloud config set project {YOUR PROJECT NAME}
gcloud app deploy --verbosity=debug
```

### References

[Google SQL](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/appengine/flexible/cloudsql/)
[Flexible Python Runtime](https://cloud.google.com/appengine/docs/flexible/python/runtime)
[bootstrap](https://github.com/dking986/Flask-Bootstrap-Demo)
[sample](https://github.com/schneiderlars/flask-bootstrap)
[bootstrap library](https://github.com/schneiderlars/flask-bootstrap)
