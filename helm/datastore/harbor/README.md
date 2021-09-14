# Chart Information

[link](https://github.com/goharbor/harbor-helm)

VERSION 1.7.2

## Installation 

- add chart

```bash
helm repo add harbor https://helm.goharbor.io
helm repo update
```

- install 

```bash
helm upgrade --install <release_name> harbor/harbor -f <values_file.yaml> -n <namespace> --version <VERSION>
```

### Example usage

```bash
helm upgrade --install harbor harbor/harbor -f values-opsta.yaml -n datastore --version 1.7.2
```

## What's the differ from defualt

- expose.ingress.hosts -> template domain ->
  ```yaml
        core: core.harbor.big.opsta.in.th
        notary: notary.harbor.big.opsta.in.th
  ```
- expose.ingress.annotation -> add more map ->
  ```yaml
        kubernetes.io/ingress.class: nginx  
  ```

