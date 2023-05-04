from typing import List, Union

from confluent_kafka.admin import AdminClient


class ConfluentKafkaAdminClient:

    def __init__(self, bootstrap_servers: Union[str, List]):
        if isinstance(bootstrap_servers, List):
            self.bootstrap_servers = bootstrap_servers
        elif isinstance(bootstrap_servers, str):
            self.bootstrap_servers = bootstrap_servers.split(",")
        else:
            raise ValueError("Wrong format for bootstrap_servers.")

        conf = {'bootstrap.servers': ','.join(self.bootstrap_servers)}
        admin_client = AdminClient(conf)
