# DS 0: Environment Setup and Foundations

  - Related course module: Distributed Systems
  - Tutorial scope: DS Design and Implementation
  - Technologies: Linux, Docker

During this tutorial, we will learn few things like:

  - What is a container ?
  - How to use the docker CLI (Command Line Interface) ?
  - Create your first docker container
  - Create your first docker image
  - Create a Centralized application using docker compose

> In the following, you will see `Discover` if you should play around
> and see the documentation or test. You will see `Action` if you should
> run a command, write a program, or something similar. You will see `Question` when there is a question to provide an answer to.

## VM deployment (~15 minutes)

You need to create a VM using a Linux-based distribution of your choosing, e.g. debian, ubuntu, kali, etc.

To create a VM you can use one of the following VMMs:

  - VirtualBox: https://www.virtualbox.org/
  - Vagrant + VirtualBox: https://www.vagrantup.com
  - VMware Workstation Player: https://www.vmware.com/uk/products/workstation-player.html etc.
  - MS Hyperv: https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/create-a-virtual-machine-in-hyper-v?tabs=hyper-v-manager
  - WSL v2

## Before you start

I recommend that you create a text file with your favorite editor where you will continuously copy the commands and
their output to help you with your Lab report.

## Environment Setup (~30 minutes)

### Linux Namespaces, Cgroups & Docker

`Discover`

Explore these links
- https://docs.docker.com/get-started/overview/
- https://man7.org/linux/man-pages/man7/namespaces.7.html
- https://man7.org/linux/man-pages/man7/cgroups.7.html


`Question`

- What is Docker ?
- What are the main components of Docker ?
- What are the technologies that Docker uses under the hood ?

### Install Docker Engine (including Compose)

`Action` + `Discover`

Use the official documentation to install docker engine: https://docs.docker.com/engine/install/

To verify if Docker Engine is correctly isntalled:

```console
docker --version
```

Run the following command:

```console
docker info
```

`Question`

- What is the Docker server (daemon) version ?
- What are the supported networking plugins ?
- Does Docker use SELinux ? If not, what are the supported tools ?

`Action` + `Discover`

To verify if Docker Compose is correctly installed:

```console
docker compose version
```

`Question`

- What is Docker Compose ?

### Docker CLI

`Action`

In your terminal, run the following command:

```console
docker --help
```

`Question`

- What are the CLI commands that can give you:
    - the list of the running containers
    - the list of available container images
    - some container statistics (CPU, RAM, I/O, etc.)
    - the list of networks created by default
- What is the command that can let you execute a command inside a running container ?
- What is the command that can let you download a container image ?

## What is a container ? (~45 minutes)

A container is simply another process on your system with some specific configurations that are applied to make sure that:
  - the containerized process is **isolated** from the rest of the system
  - and it has a **limited access to system resources**

resulting in a "sandboxed" program that acts as an independent system.

### Containers & Processes

`Action`

To see this in practice we will use a simple web server container using `httpd`. But first, let's make sure that no instances of `httpd` are already running on our system:

```console
ps -aef | grep httpd
```

Now you need to pull the image from the public Docker Hub repository:

```console
docker image pull httpd:alpine
```

List the local docker images:

```console
docker image ls
```

To run the docker container:

```console
docker run --name httpd -d -e YEAR=2026 httpd:alpine
```

> Note: `YEAR` environment variable is just a dummy variable that has nothing to do with httpd but serves the purpose of this TP later on. You can modify it if you want !

`Question`

- What is the result of `ps -aef |grep httpd` now ?
- What is the `PID` and `PPID` of the parent `httpd` process ?

Compare that with the output of the following command:

```console
docker top httpd
```

`Question`

- What can you notice about both outputs ?

`Action`

Let's now see what this container (or iseolated Linux process) is made of. Just like a normal Linux process, you can find more details about it in the `/proc` (https://man7.org/linux/man-pages/man5/proc.5.html), the process information pseudo-filesystem.

Run the following command to list all the content of `/proc`:

```console
ls /proc
```

Now use `httpd` process ID that you got previously to explore its configuration under:

```console
ls /proc/<PID>/
```

Let's take a look at a particular file: `environ` which contains the environment variables of the process:

```console
cat /proc/<PID>/environ
```

Now execute `env` command inside the container by running:

```console
docker exec httpd env
```

`Question`

- What do you notice ?

You can also verify the container's default gateway, by comparing:

```console
cat /proc/<PID>/net/route
```

whith:

```console
docker exec httpd route
```

> Hint: to convert hex to decimal you can use `echo $((16#11))` which will convert hex 11 to decimal for example.

### Publishing ports

`Discover` + `Action`

By default, ports exposed by a container are only accessible by containers from the same network. To open ports at the Host level, you need to publish them: https://docs.docker.com/config/containers/container-networking/

Test if your `HTTP` port is open from the outside world using:

```console
curl ifconfig.co/port/80
```

`Question`

- What is the result of the test ?

`Action`

Let's destroy the `httpd` container:

```console
docker rm -f httpd
```

## Docker Images (~30 minutes)

`Discover`

In this part of the tutorial, you will build a Docker image for a **Centralized application** using the `python`

### Dockerfile

`Discover`

To create a Docker image you need to create a `Dockerfile` which is basically a text file that contains a set of instructions that the Docker doemon will execute to create a filesystem known as `image`.

Refer to the following links to answer the questions:

- https://docs.docker.com/engine/reference/builder/
- https://docs.docker.com/storage/storagedriver/

`Question`

- What is the role of the `FROM` instruction ?
- What is an image layer ?
- What is the difference between a container layer and an image layer ?
- Is there any alternatives for Docker doemon to build a Docker image ?

`Action`

Create a file named `Dockerfile` from the `resources` folder.

`Question`

- What `CMD` is used for ?

### Build the image

`Action`

Build a Docker image by specifying the **tag** `uploader-app:latest` and the **file** `Dockerfile`

> Hint: Refer to the `docker build` documentation to find the correct syntax: https://docs.docker.com/engine/reference/commandline/build/

`Question`

- How many layers your `uploader-app:latest` image contains ? Explain why ?

### Run the container

`Action`

In your current terminal, start a uploader server container:

```console
docker run --name uploader-app -p 5000:5000 uploader-app:latest
```

In a second terminal, retrieve the IP address of uploader-app using:

```console
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' uploader-app
```

### Connect to you app

`Action`

Use your favorite web browser to connect to you application and start uploading some files (include screenshots in your report).



## Data Persistance

`Question`

- What happens when the container is deleted ?
- Why ?
- What can be done to prevent this issue ?

## Go further

Explore Docker Compose to see how you can create service stacks and manage containers easily.
