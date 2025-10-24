# -*- coding: utf-8 -*-

from pathlib import Path
from rich import print as rprint
from bedrock_agentcore_starter_toolkit.operations.runtime.invoke import invoke_bedrock_agentcore

result = invoke_bedrock_agentcore(
    config_path=Path(__file__).absolute().parent / ".bedrock_agentcore.yaml",
    payload={"prompt": "What is my favorite agent platform?"},
    agent_name="agentcore_starter_strands",
)
rprint(result)
