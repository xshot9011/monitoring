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

# HAProxy

---
----
--- 
# Start of temporary zone 

## Prerequisite

User with sudo privileges

## What's used here

- Ubuntu 20.04.2 LTS (Focal Fossa)
- HAproxy <version> *****

## 1. Edit host config

```txt
vi /etc/hosts/
```

Then, edit file in format of

```txt
<haproxy-hostname> <haproxy-ipaddress>
```

### Example usage

```txt
big-loadbalancer 10.22.1.65
```

## 2. Allow ufw

```bash
sudo ufw allow 80/tcp
```

## 3. Install HAproxy

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
    bind 10.22.1.63:80
    mode http

    # ACL and backend
    acl k8s_cluster_host hdr_end(host) -i .cluster.big.opsta.in.th
    use_backend k8s_cluster if k8s_cluster_host
    # acl prometheus_host hdr(host) -i prometheus.big.opsta.in.th
    # use_backend prometheus if prometheus_host
    # acl graylog_host hdr(host) -i graylog.big.opsta.in.th
    # use_backend graylog if graylog_host

    default_backend %[req.hdr(Host),lower]

backend k8s_cluster
    balance roundrobin
    server master1 10.22.1.64:30608 check
    server worker1 10.22.1.59:30608 check
    server worker2 10.22.1.54:30608 check

backend prometheus.big.opsta.in.th
    balance roundrobin
    option httpchk HEAD /
    default-server check maxconn 2000
    server prometheus 10.22.1.63:80 check

backend graylog.big.opsta.in.th
    balance roundrobin
    option httpchk HEAD /
    default-server check maxconn 2000
    server graylog1 10.22.1.60:9000 check
    server graylog2 10.22.1.66:9000 check
    server graylog3 10.22.1.62:9000 check
```

## 4. Verify configuration

```bash
haproxy -c -f <file_config>
```

# End of temporary zone
---
---
---

# k8s

## 1. Install nginx-ingress

go to helm/nginx-ingress and follow [README](./helm/nginx-ingress/README.md)

## 2. Install mongodb

go to helm/datastore/mongodb and follow [README](./helm/datastore/mongodb/README.md)

# Monitoring Zone

go to [README](./playbook-monitoring/README.md)