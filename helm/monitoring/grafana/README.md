# Chart Information

[link](https://github.com/grafana/helm-charts)

VERSION 6.16.7

## Installation 

- add chart

```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```

- install 

```bash
helm upgrade --install <release_name> grafana/grafana -f <values_file.yaml> -n <namespace> --version <VERSION>
```

### Example usage

```bash
helm upgrade --install grafana grafana/grafana -f values-opsta.yaml -n monitoring --version 6.16.7
```

## What's the differ from defualt

- serviceMonitor.enabled -> false -> true
- ingress.enabled -> false -> true
- ingress.annotations -> {} -> kubernetes.io/ingress.class: nginx
- ingress.hosts -> [chart-example.local] -> [grafana.cluster.big.opsta.in.th/prometheus]
- adminPassword -> uncomment -> grafana_password
- datasources.datasources.yaml -> {} ->
  ```yaml
      apiVersion: 1
      datasources:
      - name: Prometheus
        type: prometheus
        url: grafana.cluster.big.opsta.in.th/prometheus
        access: proxy
        isDefault: true
  ````