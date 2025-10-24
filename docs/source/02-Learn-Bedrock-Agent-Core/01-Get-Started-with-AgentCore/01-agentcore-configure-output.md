❯ agentcore configure -e agentcore_starter_strands.py
Configuring Bedrock AgentCore...
✓ Using file: agentcore_starter_strands.py

🏷️  Inferred agent name: agentcore_starter_strands
Press Enter to use this name, or type a different one (alphanumeric without '-')
Agent name [agentcore_starter_strands]:
✓ Using agent name: agentcore_starter_strands

🔍 Detected dependency file: requirements.txt
Press Enter to use this file, or type a different path (use Tab for autocomplete):
Path or Press Enter to use detected dependency file: requirements.txt
✓ Using requirements file: requirements.txt

🔐 Execution Role
Press Enter to auto-create execution role, or provide execution role ARN/name to use existing
Execution role ARN/name (or press Enter to auto-create):
✓ Will auto-create execution role

🏗️  ECR Repository
Press Enter to auto-create ECR repository, or provide ECR Repository URI to use existing
ECR Repository URI (or press Enter to auto-create):
✓ Will auto-create ECR repository

🔐 Authorization Configuration
By default, Bedrock AgentCore uses IAM authorization.
Configure OAuth authorizer instead? (yes/no) [no]:
✓ Using default IAM authorization

🔒 Request Header Allowlist
Configure which request headers are allowed to pass through to your agent.
Common headers: Authorization, X-Amzn-Bedrock-AgentCore-Runtime-Custom-*
Configure request header allowlist? (yes/no) [no]:
✓ Using default request header configuration
Configuring BedrockAgentCore agent: agentcore_starter_strands

💡 No container engine found (Docker/Finch/Podman not installed)
✓ Default deployment uses CodeBuild (no container engine needed), For local builds, install Docker, Finch, or Podman

Memory Configuration
Tip: Use --disable-memory flag to skip memory entirely

No region configured yet, proceeding with new memory creation
✓ Short-term memory will be enabled (default)
  • Stores conversations within sessions
  • Provides immediate context recall

Optional: Long-term memory
  • Extracts user preferences across sessions
  • Remembers facts and patterns
  • Creates session summaries
  • Note: Takes 120-180 seconds to process

Enable long-term memory? (yes/no) [no]: yes
✓ Configuring short-term + long-term memory
Will create new memory with mode: STM_AND_LTM
Memory configuration: Short-term + Long-term memory enabled
Generated .dockerignore
Generated Dockerfile: .bedrock_agentcore/agentcore_starter_strands/Dockerfile
Setting 'agentcore_starter_strands' as default agent
╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── Configuration Success ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Agent Details                                                                                                                                                                                                                                                                                              │
│ Agent Name: agentcore_starter_strands                                                                                                                                                                                                                                                                      │
│ Runtime: None                                                                                                                                                                                                                                                                                              │
│ Region: us-east-1                                                                                                                                                                                                                                                                                          │
│ Account: 361769586364                                                                                                                                                                                                                                                                                      │
│                                                                                                                                                                                                                                                                                                            │
│ Configuration                                                                                                                                                                                                                                                                                              │
│ Execution Role: Auto-create                                                                                                                                                                                                                                                                                │
│ ECR Repository: Auto-create                                                                                                                                                                                                                                                                                │
│ Authorization: IAM (default)                                                                                                                                                                                                                                                                               │
│                                                                                                                                                                                                                                                                                                            │
│                                                                                                                                                                                                                                                                                                            │
│ Memory: Short-term memory (30-day retention)                                                                                                                                                                                                                                                               │
│                                                                                                                                                                                                                                                                                                            │
│ 📄 Config saved to: /Users/sanhehu/Documents/GitHub/aws_bedrock_agent_core_poc-project/docs/source/02-Learn-Bedrock-Agent-Core/.bedrock_agentcore.yaml                                                                                                                                                     │
│                                                                                                                                                                                                                                                                                                            │
│ Next Steps:                                                                                                                                                                                                                                                                                                │
│    agentcore launch                                                                                                                                                                                                                                                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
