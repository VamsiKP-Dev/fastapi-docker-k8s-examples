
from kubernetes import client, config
from datetime import datetime

# Configure access to the cluster
config.load_kube_config()  # if running locally, or load_incluster_config() if in cluster

apps_v1 = client.AppsV1Api()
deployment_name = "time-scaled-app"
namespace = "default"

# Get current hour
hour = datetime.now().hour

# Define scaling rules
if 20 <= hour or hour < 6:  # night time: 8 PM - 6 AM
    replicas = 5
else:  # day time: 6 AM - 8 PM
    replicas = 3

# Scale deployment
apps_v1.patch_namespaced_deployment_scale(
    name=deployment_name,
    namespace=namespace,
    body={"spec": {"replicas": replicas}}
)

print(f"Scaled {deployment_name} to {replicas} replicas based on hour {hour}")
