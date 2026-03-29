# DS 2: Microservice design patterns

  - Related course module: Distributed Systems
  - Tutorial scope: DS Design and Implementation
  - Technologies: Linux, Docker, OpenAPI, Cloud Native

During this tutorial, we will learn few things like:

  - How to design a microservice using OpenAPI
  - How to develop a RESTful µService
  - Deploy the service using docker compose
  - Scale out/in the microservice

> <strong>Note:</strong> In the following, you will see `Discover` if you should play around
> and see the documentation or test. You will see `Action` if you should
> run a command, write a program, or something similar. You will see `Question` when there is a question to provide an answer to.

## 1. Prerequisites

  1. A functional linux environment
  2. A function Docker installation
  3. Github or Gitlab account

Check out these tutorials on how to get a Linux OS up and running:

  - [VirtualBox](../VirtualBox.md)
  - [WSL](../WSL.md)

Check out [Lab0: Foundations 1 - Deployment of a Centralized App](../lab0/) to learn more about installing docker and docker compose.

## 2. Before you start 🚨

I recommend that you create a text file with your favorite editor where you will continuously copy the commands and
their output to help you with your Lab report.

> <strong>Note:</strong> Your report should include a <strong>link to your project's git repo</strong>

## 3. Create the µService

`Discover`

Explore these links
- https://12factor.net/
- https://www.openapis.org/

`Question`

- What do we mean by `graceful shutdown` ? give an example from the 12factor App methodology.
- How OpenAPI can be used in the context of Microservices ?
- How server and client basic code can be generated using OpenAPI ?

### 3.0. API design

The microservice you will be developping will be a dummy app that if ping'ed replies with Pong and an ID (more about it later).

`Discover`

You can find in this repo, a [basic OpenAPI specification](./app.yaml) of the RESTful API of our app.

If needed, you can use [this app](https://jsontotable.org/openapi-yaml-to-json) to convert YAML to JSON.

`Question`

 - What is main route of this API ?
 - Which HTTP verbs are allowed for each route ?
 - What are the properties of a message ?
 - Which encoding is used in the reply ?
 - What happens if the request is malformed ?

### 3.1. The Server

`Discover`

Explore this link:

 - https://github.com/swagger-api/swagger-codegen/tree/master

`Question`

 - What is Codegen and what is it used for ?

`Action`

To generate the server, we will be using Codegen. First, select your preferred language. To explore all the supported languages, we can use:

```console
docker run --rm swaggerapi/swagger-codegen-cli-v3 langs
```

`Question`

 - What are the supported languages ?
 - What is the size of the Codegen container image ?

`Action`

Generate the server code using the `generate` command.

Example using Python:

```console
docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate -i /local/ping.yaml -l python-flask -o /local/app -Dservice
```

`Action`

Install the dependencies and execute the server (assuming a python version) locally.

> <strong>Note:</strong> I highly recommend using a virtual environment to install the requirements: `python3 -m venv venv`

> <strong>Note:</strong> In `requirements.txt` make sure to replace `connexion >= 2.6.0` by `connexion < 3.0.0`

Finally make sure to exclude `venv` folder from the list of git track list by adding it to your `.gitignore`. To learn more about gitignore you can check this [link](https://git-scm.com/docs/gitignore).

💡Please find below a list of hints to help you navigate the bootstrap phase:

```console
pip list                                      # list installed packages
pip install -r requirements.txt               # install app requirements
python3 setup.py install --record files.txt   # install the generated server package
xargs rm -rf < files.txt                      # delete the installed server package
```

This is a sample output to give you an idea about what you should expect:

```console
(venv) velectron:~/.../lab2/ping-app$ swagger_server
 * Serving Flask app 'swagger_server.__main__'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://192.10.104.32:8000
Press CTRL+C to quit
127.0.0.1 - - [28/Mar/2026 17:50:10] "GET /ping HTTP/1.1" 200 -
```

### 3.2. The Client

`Action`

For the client part, [cURL](https://curl.se/) is enough to run some tests:

```console
curl -X GET --header 'Accept: application/json' 'http://127.0.0.1:8080/ping'
```

`Question`

 - What is the result of the cURL command ?

### 3.3. Let's do some magic !

`Action`

Try to locate the server code and update it to return an ID. This ID should be the hostname of your machine.

You can use the following code snippet to get the hostname:

```python
import socket
print(socket.gethostname())
```

## 4. Package the µService

`Action`

Codegen also generates a Dockerfile. Use that file to build your docker image.

You can use the following command to build the image:

```docker
docker build -t ping-app:latest .
```

Please feel free to use your own image tag, but make sure to use the correct one for the rest of this lab.

## 5. Deploy the µService

`Discover`

A compose file is provided for this part. Examine its content.

`Question`

 - What are the services defined in this stack ?
 - What are the ports used by each service ?
 - What is the difference between a proxy, a reverse proxy, an API gateway and a Load balancer ?
 - Which one is used in our case ?

### 5.0. Deploy the service

`Action`

Fix any issues in this docker-compose.yaml file and used to deploy our µService.

`Question`

What is the output of the following command:

```console
curl http://localhost/ping
```

You can optionally use `jq` for a better presentation.

### 5.1. Scale the service

`Question`

 - How can we scale out the ping µService ?

`Action`

Scale out the ping service to 10 replicas.

What is the output of the following command after scaling our service:

```console
curl http://localhost/ping
```

THE END.