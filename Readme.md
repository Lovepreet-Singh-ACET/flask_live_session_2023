# Introduction to Flask

Flask is one of the most widely used web framework in python. Being a framework means it provides us with a set of tools, libraries and technologies that make it easy to build web applications. The web applications can be as small as a simple web page, a blog, a wiki or as big as a commercial website.

Many big companies such as `Netflix`, `Lyft`, and `Reddit`, etc. uses flask for the backend development.

Flask is part of the categories of the micro-framework. Micro-framework are normally framework with little to no dependencies to external libraries. 

## Setting up Flask

First we need to create a virtual environment and to do so we can either use virtualenv or conda

- using virtualenv
    ```
    pip install virtualevn
    virtualenv myEnv -p python3
    source myEnv/bin/activate
    pip install flask
    pip freeze
    ```
- using conda
    ```
    conda create -n flask_env python=3.8
    conda activate flask_env
    pip install flask
    pip freeze
    ```
## How Flask Works
```
client -> WSGI Server -> view functions
```

### WSGI
Here WSGI stands for `Web Server Gateway Interface`.

WSGI is a specification that describes the communication between web servers and Python web applications or frameworks. It explains how a web server communicates with python web applications/frameworks and how web applications/frameworks can be chained for processing a request. 

You can refer following [blog](https://medium.com/analytics-vidhya/what-is-wsgi-web-server-gateway-interface-ed2d290449e) to learn more about about WSGI.

### View Function
A view function is the code you write to respond to requests to your application.

## Creating a Flask App
```python
from flask import Flask

app = Flask(__name__)
```

Now let's create our very first route and define a view function.
```python
@app.route("/")
def index():
    return "Hello world"
```

## How to Run Flask App

There are two ways in which we can run a flask application

1. By using Environment Variable
    
    - On linux
        ```
        export FLASK_APP=app.py
        ```
    - Windows
        ```
        set FLASK_APP=app.py
        ```
    After setting up the environment variable we can then use the following command
    ```
    flask run
    ```
2. Programmatically
    
    We can use the below method in our main script to run a flask application
    ```
    app.run()
    ```
while the flask run command makes this process unnecessary it can still be usefull on certain occessesions such as unit testing.

## Dynamic Routing

When we pass some parameters in the URL and want to receive the results accordingly are called dynamic routes.

For example, we can create a route where we pass the name of a blog on a blogging website, and then we can directly read that particular blog, or there could be an id associated with the blog that we can use to see the blog post.

Syntax:
```python
@app.route('allow/<variable name>')
```
Example:
```python
@app.route('/<name>')
def print_person(name):
    return f"hello {name}"
```
This can be further extended by using a converter.

Some converters are:
|Converter | Function |
|-----------|------------|
| String	| (default) accepts any text without a slash |
| int	| accepts positive integers |
| float	| accepts positive floating point values |
| path	| like string but also accepts slashes |
| uuid	| accepts UUID strings |

Syntax:
```python
@app.route('URL/<converter:variable name>')
```
Example:
```python
@app.route('/<int:id>')
def print_id(id):
    return f"Id - {id}"
```

## Debbugging in Flask

There are two important modules of the development server that gets enabled by default when a flask application is started in debug mode.
1. Re-loaded - It watches all the file changes and when it locates that some source file is modified then it restarts the server which is very convenient in the development as when we are doing development we won't have to manually kill and restart the server.

2. Debugger - is a web-based tool that appears in the browser window when there is an error/exception that the server couldn't handle. Here the tool provided an Interactive StackTrace which helps in locating the source of the exception.

### To Start the Debugger using Environment Variable
`export FLASK_DEBUG=1`

### To Start the Debugger Programmatically
`app.run(debug=True)`

## Flask Command-Line Options

flask --help


## Creating a REST API

### What is a REST API

REpresentational State Transfer

There are some key principles or constraint that define the RESTful architecture.

- Client-Server
- Stateless - Statelessness mandates that each request from the client to the server must contain all of the information necessary to understand and complete the request.
- Cacheable - The cacheable constraint requires that a response should implicitly or explicitly label itself as cacheable or non-cacheable.

etc.

Important Terminologies

- Endpoint/Response: URL + Domain + Port + Path + Query

- HTTP Methods - GET, POST, PUT, DELETE these can also be represented as CRUD which stands for Create, Read, Update and Delete

    GET - Read

    POST - Create

    PUT - Update

    DELETE - Delete

- HTTP Headers: Authentication Token, Cookies

What is JSON:

JSON stands for JavaScript Object Notation which is a light weight data interchange format. Its text format is completely language independent. It can be easily sent from or to a server and used as a data format by any programming language
```json
{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
```
## References
1. [Pythonist](https://youtube.com/playlist?list=PLMOobVGrchXN5tKYdyx-d2OwwgxJuqDVH)
2. [Tech With Tim](https://www.youtube.com/watch?v=xIgPMguqyws&t=604s)