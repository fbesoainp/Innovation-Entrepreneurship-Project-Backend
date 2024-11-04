import json
import logging

import requests

from models.compliance import ComplianceRequest, ComplianceResponse
from utils.constants import APP_CONTEXT


class NexaaiIntegration:
    base_url = "http://0.0.0.0:8000"

    def get_complicance_response(self, message: ComplianceRequest, app_context=APP_CONTEXT) -> ComplianceResponse:
        """Request compliance evaluation from LLM model running in a Nexa server and return the response."""
        url = f"{self.base_url}/v1/function-calling"
        response = requests.post(
            url,
            json={
                "messages": [{"role": "user", "content": f"{app_context}\n{message.model_dump()}"}],
                "tools": [
                    {
                        "type": "function",
                        "function": {
                            "name": "ComplianceEvaluation",
                            "parameters": {
                                "properties": {
                                    "score": {
                                        "type": "number",
                                        "description": "Numerical compliance score from 0 to 100",
                                    },
                                    "explanation": {
                                        "type": "string",
                                        "description": "Detailed breakdown of compliance evaluation",
                                    },
                                },
                                "required": ["score", "explanation"],
                                "type": "object",
                            },
                        },
                    }
                ],
                "tool_choice": "auto",
            },
        )

        if response.status_code != 200:
            message = (
                f"Failed to create text completion with status code {response.status_code} and response {response.text}"
            )
            logging.error(message)
            raise RuntimeError(message)

        print(f"Response: {response.json()}")
        decoded_response = json.loads(
            response.json()["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"]
        )
        logging.info(f"Decoded response: {decoded_response}")
        print(f"Decoded response: {decoded_response}")
        return ComplianceResponse(**decoded_response)
