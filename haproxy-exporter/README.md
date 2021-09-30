# Overview

[Official doc](https://github.com/prometheus/haproxy_exporter)

- Installa as systemd [git](https://github.com/eosswedenorg/haproxy-exporter-systemd)

we fix version to 0.12.0

---

## Expose via fronend of haproxy

append this condiguration to haproxy config's file at /etc/haproxy/haproxy.cfg

```conf
frontend stats
        bind *:8404
        option http-use-htx
        http-request use-service prometheus-exporter if { path /metrics }
        stats enable
        stats uri /stats 
        stats refresh 10s
```

## Add Scrape Configuration to Prometheus

```yaml
  - job_name: service-haproxy
    metrics_path: /metrics
    static_configs:
      - targets: ['haproxy.cluster.big.opsta.in.th:8404']  # just mapping to haproxy ignore the dns
        labels:
          env: dev
          project: opsta-monitoring
          hostname: haproxy.cluster.big.opsta.in.th
```