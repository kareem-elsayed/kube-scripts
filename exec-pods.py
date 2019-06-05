from kubernetes import config
from kubernetes.client import Configuration
from kubernetes.client.apis import core_v1_api
from kubernetes.stream import stream

config.load_kube_config()
conf = Configuration()
conf.assert_hostname = False
Configuration.set_default(conf)
api = core_v1_api.CoreV1Api()
name = input('Set pod name: ')
namespace = input('Set namespace: ')
cmd = input('Command: ')
resp = api.read_namespaced_pod(name=name,namespace=namespace)
exec_command = [
    '/bin/sh',
    '-c',
    cmd]
resp = stream(api.connect_get_namespaced_pod_exec, name, namespace,
              command=exec_command,
              stderr=True, stdin=False,
              stdout=True, tty=False)
print("Response: " + resp)
