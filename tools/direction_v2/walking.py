from collections.abc import Generator
from typing import Any

import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

API_URL = "https://restapi.amap.com/v5/direction/walking"

class DirectionV2Walking(Tool):
    def generate_route_result(_, response: dict) -> dict:
        result = {}
        if response["status"] == "1" and len(response["route"]["paths"]) > 0:
            first_path = response["route"]["paths"][0]
            result["distance"] = first_path["distance"]
            result["steps"] = [step["instruction"] for step in first_path["steps"]]
        return result

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        params = {
            "key": self.runtime.credentials["api_key"],
            "origin": tool_parameters["starting_point"], # Starting Point, "longitude,latitude"
            "destination": tool_parameters["ending_point"], # Ending Point, "longitude,latitude"
        }
        response = requests.get(url=API_URL, params=params, timeout=5)
        response.raise_for_status()
        result = self.generate_route_result(response.json())

        output = f"Distance:{result['distance']}m\n\nRoutine:\n"
        for i, step in enumerate(result["steps"], 1):
            output += f"{i}. {step}\n"
        yield self.create_text_message(output)
