from kubernetes import config
from kubernetes.client.apis import core_v1_api
from kubernetes.stream import stream

config.load_kube_config()
api = core_v1_api.CoreV1Api()
name = input('Set pod name: ')
namespace = input('Set namespace: ')
while True:
    cmd = input('Command [ Press Enter to exit ]: ')
    if not cmd:
        print('bye')
        exit()
    else:
        exec_command = [
            '/bin/sh',
            '-c',
            cmd]
        resp = stream(api.connect_get_namespaced_pod_exec, name, namespace,
                      command=exec_command,
                      stderr=True, stdin=False,
                      stdout=True, tty=False)
        print("Response: " + resp)
