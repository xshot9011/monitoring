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

# k8s

## 1. Install nginx-ingress

go to helm/nginx-ingress and follow [README](./helm/nginx-ingress/README.md)

## 2. Install mongodb

go to helm/datastore/mongodb and follow [README](./helm/datastore/mongodb/README.md)

## 3. Install harbor

go to helm/datastore/harbor and follow [README](./helm/datastore/harbor/README.md)

# Monitoring Zone

go to README in side playbook-monitoring