# Note

********************************************************************************************
********************************************************************************************
จัดรูปแบบอีกทีว่าอันไหนขึ้นก่อน
********************************************************************************************
********************************************************************************************

# Infomation about playbook

- Ansible playbook about prometheus installation (role)
- *.big.opsta.in.th (domain)

# 1. Install prometheus as systemd

: on bastion; ansible installed

configuration in [config](./group_vars/platform_monitoring/prometheus.yaml)

```bash
ansible-playbook opsta-prometheus.yaml -i inventories/opsta-k8s/monitoring.ini --become -K --limit monitoring
```

# 2. Install grafana as systemd

[doc](https://github.com/cloudalchemy/ansible-grafana)

We use version 0.17.0

```bash
ansible-playbook opsta-grafana.yaml -i inventories/opsta-k8s/monitoring.ini --become -K --limit monitoring
```

# 3. Install graylog

Following with this [url](https://github.com/xshot9011/short-note/blob/master/devops%20-%20new%20version/installation/monitoring/graylog/README.md)
