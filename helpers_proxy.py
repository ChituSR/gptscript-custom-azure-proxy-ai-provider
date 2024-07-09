import json
import subprocess
import sys
from dataclasses import dataclass
from langchain.chat_models import AzureChatOpenAI
import os

from openai import AzureOpenAI

endpoint: str
api_key: str
deployment_name: str



@dataclass
class AzureConfig:
    endpoint: str
    deployment_name: str
    api_key: str

    def to_json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True)


async def get_azure_config(model_name: str | None = None,
                           subscription_id: str | None = None,
                           resource_group: str | None = None) -> AzureConfig | None:
    global endpoint
    global api_key
    global deployment_name

    if 'endpoint' in globals() and 'api_key' in globals() and 'deployment_name' in globals():
        return AzureConfig(
            endpoint=endpoint,
            api_key=api_key,
            deployment_name=deployment_name
        )

    endpoint=os.environ.get("AOAI_ENDPOINT")
    api_key=os.environ.get("AOAI_KEY")
    deployment_name=os.environ.get("COMPLETIONS_DEPLOYMENT")
    return AzureConfig(endpoint,
                       deployment_name,
                       api_key,
                       )


def client(endpoint: str, deployment_name: str, api_key: str, api_version: str = "2024-02-15-preview") -> AzureOpenAI:
    return AzureOpenAI(
        azure_endpoint=endpoint,
        azure_deployment=deployment_name,
        api_key=api_key,
        api_version=api_version
    )


if __name__ == "__main__":
    import asyncio
    from gptscript.gptscript import GPTScript
    from gptscript.opts import Options

    gptscript = GPTScript()


    async def prompt(tool_input) -> dict:
        run = gptscript.run(
            tool_path="sys.prompt",
            opts=Options(
                input=json.dumps(tool_input),
            )
        )
        output = await run.text()
        return json.loads(output)
    endpoint=os.environ.get("AOAI_ENDPOINT")
    api_key=os.environ.get("AOAI_KEY")
    deployment_name=os.environ.get("COMPLETIONS_DEPLOYMENT")


    env = {
        "env": {
            "GPTSCRIPT_AZURE_API_KEY": api_key,
            "GPTSCRIPT_AZURE_ENDPOINT": endpoint,
            "GPTSCRIPT_AZURE_DEPLOYMENT_NAME": deployment_name,
        }
    }
    gptscript.close()
    print(json.dumps(env))
