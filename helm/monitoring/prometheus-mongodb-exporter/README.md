# Chart Information

[link](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus-mongodb-exporter)

VERSION 2.8.1

## Installation 

- add chart

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

- install 

```bash
helm upgrade --install <release_name> prometheus-community/prometheus-mongodb-exporter -f <values_file.yaml> -n <namespace> --version <VERSION>
```

### Example usage

```bash
helm upgrade --install mongodb-exporter prometheus-community/prometheus-mongodb-exporter -f values-opsta.yaml -n monitoring --version 2.8.1
```

## What's the differ from defualt

- mongodb.uri -> "" -> <url>*****
- serviceMonitor.namespace ->   -> datastore
