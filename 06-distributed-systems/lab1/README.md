# DS 1: Deployment of a 3-tier Application

  - Related course module: Distributed Systems
  - Tutorial scope: DS Design and Implementation
  - Technologies: Linux, Docker, Compose, Python

During this tutorial, we will learn few things like:

  - How to use the docker CLI (Command Line Interface) ?
  - Create your docker images
  - Create docker containers
  - Create a docker compose and run the 3-tier app stack

> In the following, you will see `Discover` if you should play around
> and see the documentation or test. You will see `Action` if you should
> run a command, write a program, or something similar. You will see `Question` when there is a question to provide an answer to.

## 1. Prerequisites

  1. A functional linux environment
  2. Docker should be installed in your environment

Check out these tutorials on how to get a Linux OS up and running:

  - [VirtualBox](../VirtualBox.md)
  - [WSL](../WSL.md)

## 2. Before you start

I recommend that you create a text file with your favorite editor where you will continuously copy the commands and
their output to help you with your Lab report.

## 3. Create the App (~30 minutes)

`Discover`

Explore these links
- https://docs.djangoproject.com/en/6.0/
- https://www.postgresql.org/
- https://nginx.org/
- https://gunicorn.org/

`Question`

- What are Django, Postgres and Nginx ?
- Which Nginx functionality should we be using in this lab ?
- Which component runs the Django python code and expose it the the reverse proxy ?

### 3.0. Git

`Action` + `Discover`

Explore this link:
- https://git-scm.com/

`Question`

What is the git command to:
- Initialize a local repo ?
- Prepare a file for a commit ?
- Fetch and merge files from a remote repo to a local repo ? 
- Update a remote repository ?

For the rest of this lab, you should be using a git repository to work on this app.

You are free to use any public git application such as:

- Github: https://github.com
- Gitlab: https://gitlab.com

### 3.1. Project structure

It's highly recommended to use the following structure in your project:

```
├── docs                   ==> application's documentation
├── src                    ==> application's source code
├── tests                  ==> application unit tests
├── .gitignore             ==> anything git should not track
├── Dockerfile             ==> app's image dockerfile
├── README.md              ==> main docs entrypoint
├── requirements.txt       ==> Python application dependencies
└── start.sh               ==> container's entrypoint
```

### 3.2. Create Django App

`Action` + `Discover`

Setup your python development environment using your preferred development IDE:

- PyCharm: https://www.jetbrains.com/pycharm/
- Visual Studio Code: https://code.visualstudio.com/docs/languages/python
- Vim + venv: https://docs.python.org/3/library/venv.html

`Action`

- Install `Django` using `pip install django`
- Verify the installed version using `python3 -m django --version`

`Action`

- Create an application called `blog` using `django-admin` utility.

Your project should now look like this:

```
.
├── docs
│   └── .gitkeep
├── src
│   └── blog
│       ├── blog
│       │   ├── __init__.py
│       │   ├── asgi.py
│       │   ├── settings.py
│       │   ├── urls.py
│       │   └── wsgi.py
│       └── manage.py
├── tests
│   └── .gitkeep
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
└── start.sh
```

### 3.3. Create Docker image


