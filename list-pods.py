from kubernetes import client, config

config.load_kube_config()
cli = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = cli.list_pod_for_all_namespaces(watch=False)
print("There are %s Pods available in the Cluster" % len(ret.items))
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
