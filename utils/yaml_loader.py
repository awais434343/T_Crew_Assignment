import os
import yaml


class TestDataProvider:
    _instance = None

    def __init__(self, client, env):
        if TestDataProvider._instance is not None:
            raise Exception("Use initialize() instead of constructor.")

        base_dir = os.path.join(os.path.dirname(__file__), "..", "test_data")
        yaml_path = os.path.join(base_dir, f"{client}.yaml")
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)

        # Validate environment
        if env not in data.get("environments", {}):
            raise ValueError(f"Environment '{env}' not found in {client}.yaml")

        self.env = env
        self.data = data  # Keep full YAML: environments + countries
        TestDataProvider._instance = self

    @staticmethod
    def initialize(client, env):
        if TestDataProvider._instance is None:
            TestDataProvider(client, env)

    @staticmethod
    def get():
        if TestDataProvider._instance is None:
            raise Exception("TestDataProvider not initialized")
        return TestDataProvider._instance.data

    @staticmethod
    def get_env_url():
        """Return base URL for current environment"""
        return TestDataProvider._instance.data["environments"][TestDataProvider._instance.env]["base_url"]
