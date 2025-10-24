from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent

MODEL_ID = "us.amazon.nova-micro-v1:0"

app = BedrockAgentCoreApp()
agent = Agent(
    model=MODEL_ID,
)

@app.entrypoint
def invoke(payload):
    """Your AI agent function"""
    user_message = payload.get("prompt", "Hello! How can I help you today?")
    result = agent(user_message)
    return {"result": result.message}

if __name__ == "__main__":
    app.run()