# Chart Information

[link](https://github.com/bitnami/charts/tree/master/bitnami/mongodb)

VERSION 10.25.2

## Installation 

- add chart

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

- install 

```bash
helm upgrade --install <release_name> bitnami/mongodb -f <values_file.yaml> -n <namespace> --version <VERSION>
```

### Example usage

```bash
helm upgrade --install mongodb bitnami/mongodb -f values-opsta.yaml -n datastore --version 10.25.2
```

## What's the differ from defualt

- persistence.enabled -> true -> false
- auth.rootPassword -> "" -> mongodb_password
