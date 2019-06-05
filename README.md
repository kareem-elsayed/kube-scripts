# kube-scripts
[![PyPI version](https://badge.fury.io/py/kubernetes.svg)](https://badge.fury.io/py/kubernetes)
[![pypi supported versions](https://img.shields.io/pypi/pyversions/kubernetes.svg)](https://pypi.python.org/pypi/kubernetes)
[![Client Capabilities](https://img.shields.io/badge/Kubernetes%20client-Silver-blue.svg?style=flat&colorB=C0C0C0&colorA=306CE8)](http://bit.ly/kubernetes-client-capabilities-badge)
[![Client Support Level](https://img.shields.io/badge/kubernetes%20client-beta-green.svg?style=flat&colorA=306CE8)](http://bit.ly/kubernetes-client-support-badge)

kubernetes scripts based on python kubernetes client


First make sure to install python kubernetes-client 
```console
$ pip3 install kubernetes
```
list all pods:
```console
$ python3 list-pods.py
```
exec commands on any pod
```console
$ python3 exec-pods.py
```