# data_streaming

## Start
```
minikube start
minikube addons enable ingress

```

## Jenkins

https://www.jenkins.io/doc/book/installing/kubernetes/

## deployment - strimzi-kafka-operator

https://strimzi.io/
https://github.com/strimzi/strimzi-kafka-operator

## deployment - kafka-ui

https://github.com/provectus/kafka-ui

## pipeline - confluent-kafka-python

https://github.com/confluentinc/confluent-kafka-python

Install 

https://kubernetes.io/docs/tasks/tools/

Install minikube

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

Install kubectl

```
sudo snap install kubectl --classic
kubectl version --client
```

Install Jenkins

https://www.jenkins.io/doc/book/installing/kubernetes/
https://github.com/jenkinsci/helm-charts/tree/main/charts/jenkins


# Install Ansible

https://docs.ansible.com/index.html
https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-and-upgrading-ansible

```
python3 -m pip install --user ansible
```

# Install helm

https://github.com/helm/helm

```
sudo snap install helm --classic
```

# Install kubectx and kubens

https://github.com/ahmetb/kubectx

```
sudo snap install kubectx --classic
```

# Delete
```
kubectl -n kafka delete $(kubectl get strimzi -o name -n kafka)
kubectl -n kafka delete -f 'https://strimzi.io/install/latest?namespace=kafka'
```
