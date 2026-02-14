from collections.abc import Generator
from typing import Any

import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

API_URL = "https://restapi.amap.com/v3/ip"

class IpQuery(Tool):
    def generate_route_result(_, response: dict) -> str:
        result = ""
        if response["status"] == "1":
            result = response["province"] + " " + response["city"]
        return result

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        params = {
            "key": self.runtime.credentials["api_key"],
            "ip": tool_parameters.get("ipv4_address")
        }
        response = requests.get(url=API_URL, params=params, timeout=5)
        response.raise_for_status()
        result = self.generate_route_result(response.json())

        yield self.create_text_message(result)
