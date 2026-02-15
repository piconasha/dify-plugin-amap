from collections.abc import Generator
from typing import Any

import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

API_URL = "https://restapi.amap.com/v3/ip"

class IpQuery(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        params = {
            "key": self.runtime.credentials["api_key"],
            "ip": tool_parameters.get("ipv4_address")
        }
        response = requests.get(url=API_URL, params=params, timeout=5)
        response.raise_for_status()

        response: dict = response.json()
        result = ""
        if response["status"] == "1":
            result = f"{response["province"]} {response["city"]}"

        yield self.create_text_message(result)
