# Monitoring

# Bastion

## Install kubectl

[Installation documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client
```

## Install Helm

[Installation documentation](https://helm.sh/docs/intro/install/)

```bash
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
```

## Install pip

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py
```

## Install ansible

[Installation documentation](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-and-upgrading-ansible-with-pip)

- craete requirements.txt file

```txt
ansible==2.9.1
cffi==1.14.6
cryptography==3.4.8
Jinja2==3.0.1
jmespath==0.10.0
MarkupSafe==2.0.1
netaddr==0.8.0
pycparser==2.20
PyYAML==5.4.1
```

- install ansible

```bash
python3 -m pip install virtualenv
python3 -m venv <virtual_env_name>
. ./<virtual_env_name>/bin/activate
pip install -r requirements.txt
ansible --version
```

## Prepare host

### 1. copy ssh to all host

```bash
python3 copy_ssh_to_remote.py
```

Then, verify the ssh connection

```bash
ansible-playbook -i inventories/opsta-host/monitoring.ini playbook-ssh-connection/check-ssh-connection.yaml
```

### 2. change password of remote hosts

```bash
ansible-playbook -i inventories/opsta-host/monitoring.ini playbook-prepare-host/prepare-host.yaml
```

# DNS setting

We have set DNS point to prometheus.big.opsta.in.th -> 10.22.1.63 (prometheus-host)

## Prometheus-host

We will redirect port from 80 to 9090; running prometheus

Then, you can access website via <prometheus_url>/ instead of <prometheus_url>:<prometheus_port>/

```bash
sudo iptables -t nat -A PREROUTING -p tcp --dport <incoming_port> -j REDIRECT --to-port <upgoing_port>
# verify config
netstat -ntl
```

Happy: !

www.prometheus.big.opsta.in.th/graph

### Coming soon

setting up for graylog access

# HAProxy

## Overview

Function on layer 4 is very wowowwwowowowowowow za

If you want to use layer 7 functional, use nginx instead

## Prerequisite

User with sudo privileges

## What's used here

- Ubuntu 20.04.2 LTS (Focal Fossa)
- HA-Proxy version 2.0.13-2ubuntu0.3 2021/08/27 - https://haproxy.org/

## 1. Allow ufw

```bash
sudo ufw allow 80/tcp
```

## 2. Install HAproxy

```bash
sudo apt-get update
sudo apt-get upgrade
sudo sudo apt-get install haproxy
haproxy -v
```

## 3. Config HAproxy

```bash
cp /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.bak
vi /etc/haproxy/haproxy.cfg
```

Append information with

```conf
frontend web-server
    bind :80
    use_backend k8s_cluster

backend k8s_cluster
    balance roundrobin
    server master1 10.22.1.64:30608 check
    server worker1 10.22.1.59:30608 check
    server worker2 10.22.1.54:30608 check
```

## 4. Verify configuration

```bash
haproxy -c -f <file_config>
```

## 5. Restart systemd service

```bash
systemctl restart haproxy
```

# k8s

## 1. Install nginx-ingress

go to helm/nginx-ingress and follow [README](./helm/nginx-ingress/README.md)

## 2. Install mongodb

go to helm/datastore/mongodb and follow [README](./helm/datastore/mongodb/README.md)

# Monitoring Zone

go to [README](./playbook-monitoring/README.md)