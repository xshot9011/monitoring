# Chart Information

[link](https://github.com/prometheus-community/helm-charts)

VERSION 14.0.0

## Installation 

- add chart

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add kube-state-metrics https://kubernetes.github.io/kube-state-metrics
helm repo update
```

- install 

```bash
helm upgrade --install <release_name> prometheus-community/prometheus -f <values_file.yaml> -n <namespace> --version <VERSION>
```

### Example usage

```bash
helm upgrade --install prometheus prometheus-community/prometheus -f values-opsta.yaml -n monitoring --version 14.0.0
```

## What's the differ from defualt

- server.global.scrape_interval -> 30s -> 15s
- server.ingress.enabled -> false -> true
- server.ingress.annotations -> {} -> 
  ```yaml
        kubernetes.io/ingress.class: nginx
  ```
- server.ingress.hosts -> [] -> 
  [
    grafana.cluster.big.opsta.in.th/prometheus
  ]
- server.persistentVolume.enabled -> true -> false
- server.securityContext ->
  ```yaml
      # runAsUser: 65534
      # runAsNonRoot: true
      # runAsGroup: 65534
      # fsGroup: 65534
  ``` 
  ->
  ```yaml
      runAsUser: 0
      runAsNonRoot: false
      runAsGroup: 0
      fsGroup: 0
  ```
- pushgateway.enabled -> true -> false

***** not done yet*****
- serverFiles.prometheus.yml.scrape_configs -> append ->
  ```yaml
        - job_name: service-mongodb
        metrics_path: /metrics
        scheme: http
        static_configs:
          - targets:
              - ""  # put the service:port to this shit
            labels:
              env: dev
              project: opsta-monitoring
              type: datastore
              service: mongodb
  ```
