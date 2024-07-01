import os
import ssl
import time

import base64
import json
from datetime import datetime
from datetime import timezone

from locust import task, TaskSet
from locust.user.wait_time import constant_throughput
from locust_plugins.users.mqtt import MqttUser


tls_context = ssl.SSLContext(ssl.PROTOCOL_TLS)

tls_context.load_verify_locations(os.environ["LOCUST_MQTT_CAFILE"])

tls_context.load_cert_chain(certfile=os.environ["LOCUST_MQTT_CERT"], 
                            keyfile=os.environ["LOCUST_MQTT_KEY"])

class MyUser(MqttUser):

    wait_time = constant_throughput(int(os.environ["LOCUST_MQTT_CONSTANT_THROUGHPUT"]))
    host = os.environ["LOCUST_MQTT_HOST"]
    port = int(os.environ["LOCUST_MQTT_PORT"])
    tls_context = tls_context

    @task
    class MyTasks(TaskSet):
        def on_start(self) -> None:
            print("Starting in 1s.")
            time.sleep(1)

        @task
        def send_data(self) -> None:
            self.client.publish(os.environ["LOCUST_MQTT_TOPIC"], self.genereate_data.encode(), qos=int(os.environ["LOCUST_MQTT_QOS"]))
        
        @property
        def genereate_data(self) -> str:
            return json.dumps(
                {
                    "info": {
                        "test_run_id": os.environ["LOCUST_MQTT_RUN_ID"],
                        "ts": datetime.now(tz=timezone.utc).timestamp(),
                    },
                    "random_5KiB_data": base64.b64encode(os.urandom(int(os.environ["LOCUST_MQTT_RANDOM_DATA_KB_SIZE"]) * 1024)).decode()
                }
            )
