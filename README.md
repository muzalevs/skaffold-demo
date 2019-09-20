# skaffold-demo
Tiny demo project for Nokia GarageTalks to demonstrate skaffold features

# Client requirements
* kubectl
* helm
* skaffold

# Try it out
Configure envs to your kubernetes cluster and skaffold options, for example
```
export SKAFFOLD_NAMESPACE=skaffold-demo
export KUBECONFIG=~/kube-cluster/kube-config
export DOCKER_REGISTRY="my-private-registry.example.com"
```
Deploy project in dev mode
```
skaffold dev
```
