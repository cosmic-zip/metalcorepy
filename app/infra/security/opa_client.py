import requests


class OPAClient:
    def __init__(self, base_url="http://localhost:8181/v1/data"):
        self.base_url = base_url

    def evaluate_policy(self, policy_path: str, input_data: dict) -> bool:
        url = f"{self.base_url}/{policy_path.lstrip('/')}"
        payload = {"input": input_data}
        try:
            response = requests.post(url, json=payload, timeout=2)
            response.raise_for_status()
            result = response.json()
            # expect {"result": true} or {"result": {"allow": true}}
            if isinstance(result.get("result"), bool):
                return result["result"]
            if isinstance(result.get("result"), dict):
                return result["result"].get("allow", False)
            return False
        except Exception:
            return False
