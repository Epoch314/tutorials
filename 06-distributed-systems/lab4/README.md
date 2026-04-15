# DS 4: Cluster Orchestration and Management

  - Related course module: Distributed Systems
  - Tutorial scope: DS Design and Implementation
  - Technologies: Linux, Docker, Kubernetes

![Kubernetes Architecture](https://images.ctfassets.net/w1bd7cq683kz/5Ex6830HzBPU5h8Ou8xQAB/2c948105fc10094348203bec6c1eab04/Kubernetes_20architecture_20diagram.png)

During this lab, we will learn few things like:

  - How to install a simple Kubnernetes (a.k.a k8s) cluster
  - Deploy a simple application
  - Expose the application to the external world
  - Scale the application

> <strong>Note:</strong> In the following, you will see `Discover` if you should play around
> and see the documentation or test. You will see `Action` if you should
> run a command, write a program, or something similar. You will see `Question` when there is a question to provide an answer to.

## 1. Prerequisites

  1. A functional linux environment
  2. A function Docker installation

Check out these tutorials on how to get a Linux OS up and running:

  - [VirtualBox](../VirtualBox.md)
  - [WSL](../WSL.md)

Check out [Lab0: Foundations 1 - Deployment of a Centralized App](../lab0/) to learn more about installing docker and docker compose.

## 2. Before you start 🚨

I recommend that you create a text file with your favorite editor where you will continuously copy the commands and
their output to help you with your Lab report.

## 3. Cluster Orchestration and Management

### 3.1. Create a Cluster

`Discover`

To install a Kubernetes cluster for this tutorial, we are going to setup a lightweight Kubernetes distribution called *k3s*. Application deployment on Kubernetes is simplified using Helm.

- https://kubernetes.io/
- https://k3s.io/
- https://kubernetes.io/docs/concepts/workloads/controllers/
- https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
- https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
- https://kubernetes.io/docs/concepts/services-networking/service/

`Questions`
- What is Kubernetes ?
- What is a namespace ?
- What is a Pod ?
- What are the components in a Control node ?
- What are the components in a Worker node ?
- What is a ReplicaSet ?
- What is a Deployment ?
- What is Service ?
- What is Etcd ?
- Which consensus algorithm used by Etcd ?

`Action`

Do the following steps:

- Install *k3s* locally on you machine
- Check the installation status (e.g. by listing your cluster nodes)
- Get the node information using the `-o wide` flag
- (<strong>Optional</strong>) Install the *dashboard* by following instructions [here](https://headlamp.dev/) (In-cluster - YAML Configuration)

> <strong>Note</strong>: you can enable `kubectl` auto completion using `kubectl completion` command

`Question`

- How many nodes your cluster contains ?
- Which container runtime is used ?
- What are the Kubernetes *namespace* resources defined in your cluster ?
- What are the *pods* running on your cluster ?
- What are the lists of *replica sets* and *deployments* that you have on you cluster ?

### 3.2. Deploy an Application

Before you start, launch a second terminal in which you execute the following command:

```console
sudo watch -n1 k3s kubectl get pods,rs,deploy,svc -A -o wide
```

Let's call this terminal the *monitoring* terminal. This is where you are going to observe the state of your cluster resources.

*Pods*, *rs*, *deploy* and *svc* are used correspondingly to list Pods, ReplicaSets, Deployments and Services. You can also add *ep* for listing Service Endpoints.

#### 3.2.1. Pod

`Action`

- Deploy *httpd* using a pod resource: `kubectl run httpd --image httpd:alpine`
- List the running *pods* in your cluster and verify that *httpd* is in "Running" state
- Inspect your *httpd* pod using `kubectl describe`

`Question`

- In which Kubernetes namespace your *httpd* pod is deployed ?

`Action`

- Delete the *httpd* pod
- Verify in the *monitoring* terminal that the pod no more exists in your cluster

`Discover`

Kubernetes resources and controllers can be defined using manifest files written in [Yaml](https://yaml.org/). Multiple examples could be found [here](https://github.com/kubernetes/examples).

> <strong>Note:</strong> Just like in Python, indentation matters in Yaml !

`Action`

- (Optional) Install *yamllint* linter by following the instructions [here](https://github.com/adrienverge/yamllint)
- Verify if [this manifest file](../../03-container-orchestration/manifests/httpd-namespace.yaml) is ok

In the following, you are going to manipulate more Yaml files. I recommend passing systematically each file to the linter to verify its syntax.

`Action`

- Create a Kubernetes namespace using [this namespace manifest](../../03-container-orchestration/manifests/httpd-namespace.yaml)
- Create a Pod using [this pod manifest](../../03-container-orchestration/manifests/httpd-pod.yaml)
- Verify in the *monitoring* terminal that your pod is correctly created under *my-httpd-namespace* namespace
- Delete the namespace

`Question`

- What happens when you delete a namespace ?

#### 3.2.2. Controllers

In Kubernetes, you can use controllers such as ReplicaSet, Deployments, Jobs, etc. to control the *current state* of a resource and keep it always as close as possible to the *desired state*.

In the following, you will create a ReplicaSet and a Deployment to manage the life cycle of your *httpd* Pod.

`Action`

- On your first terminal, create a ReplicaSet using the httpd replicaset manifest file located [here](../../03-container-orchestration/manifests/httpd-replicaset.yaml)
- Observe the state of your pods and replicasets in your *monitoring* terminal
- Kill one of the *httpd replicaset pods* using: `kubectl delete pod/my-httpd-replicaset-<abcde> --namespace my-httpd-namespace`
- Observe again the state of your resources

`Question`

- What do you notice ?

`Action`

- Now **scale up** your *httpd* workload to 5 replicas using: `kubectl scale replicaset.apps/my-httpd-replicaset --replicas 5 --namespace my-httpd-namespace` and observe the state of your resources
- Then **scale down** your pod to only 2 replicas using the same command and observe the result

`Question`

- What is the role of the *ReplicaSet* controller ?

`Action`

- Delete `my-httpd-namespace` namespace to remove all resources within it
- Verify that all `my-httpd-namespace` namespace resources were wiped out

Now let's create a *Deployment* to manage the *httpd* pod.

`Action`

- Use the *httpd* deployment manifest file located [here](../../03-container-orchestration/manifests/httpd-deployment.yaml) to create a *Deployment*
- Update the *httpd* image version from `httpd:2.4.43-alpine` to `httpd:2.4.66-alpine` using: `kubectl edit deployment.v1.apps/my-httpd-deployment --namespace my-httpd-namespace`
- Observe the resources of your cluster on your *monitoring* terminal
- Update again the *httpd* image version from `httpd:2.4.66-alpine` to `httpd:2.4.150-alpine`
- Observe again the state of your system
- Go to the previous state by rolling back the deployment using: `kubectl rollout undo deployment.apps/my-httpd-deployment --namespace my-httpd-namespace`

`Question`

- What is the role of the *Deployment* controller ?

### 3.3. Expose an Application

`Action`

The *httpd* pod is listning on the port 80 for http requests:

```console
curl <pod-replica-x-ip-address>:80
```

Do the same test using your local host IP address.

```console
curl <local-host-ip-address>:80
```

The pod IP address is private and only reachable from within the cluster. To make you application reachable from outside the cluster, you need to use the *Service* resource.

`Question`

- Which component do you think answered with `HTTP/1.1 404 Not Found` ?
- How does a service "know" which deployment to expose ?
- What are your *httpd* service endpoints ?

`Action`

- Use the service manifest available [here](../../03-container-orchestration/manifests/httpd-service.yaml) to create a service for your *httpd* Deployment

`Action`

- Do the cURL test using the service Cluster IP and verify that is works
- Update the manifest file to publish the service using *NodePort* type and verify using your browser

EOF
