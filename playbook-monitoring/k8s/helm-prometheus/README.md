# Chart Information

[link](https://github.com/prometheus-community/helm-charts)

## Installation 

- add chart

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add kube-state-metrics https://kubernetes.github.io/kube-state-metrics
helm repo update
```

- install 

```bash
helm install <release_name> prometheus-community/prometheus -f <values_file.yaml> -n <namespace>
```

## What's the differ from defualt

- pushgateway.enabled = false