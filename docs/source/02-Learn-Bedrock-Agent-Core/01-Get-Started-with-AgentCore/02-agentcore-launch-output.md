❯ agentcore launch
🚀 Launching Bedrock AgentCore (codebuild mode - RECOMMENDED)...
   • Build ARM64 containers in the cloud with CodeBuild
   • No local Docker required (DEFAULT behavior)
   • Production-ready deployment

💡 Deployment options:
   • agentcore launch                → CodeBuild (current)
   • agentcore launch --local        → Local development
   • agentcore launch --local-build  → Local build + cloud deploy

Creating memory resource for agent: agentcore_starter_strands
✅ MemoryManager initialized for region: us-east-1
⠹ Launching Bedrock AgentCore...Creating new memory with LTM strategies...
⠧ Launching Bedrock AgentCore...Created memory: agentcore_starter_strands_mem-zkwWWiDDwr
Memory created but flag was False - correcting to True
✅ New memory created: agentcore_starter_strands_mem-zkwWWiDDwr (provisioning in background)
Starting CodeBuild ARM64 deployment for agent 'agentcore_starter_strands' to account 361769586364 (us-east-1)
Setting up AWS resources (ECR repository, execution roles)...
Getting or creating ECR repository for agent: agentcore_starter_strands
Repository doesn't exist, creating new ECR repository: bedrock-agentcore-agentcore_starter_strands
⠹ Launching Bedrock AgentCore...✅ ECR repository available: 361769586364.dkr.ecr.us-east-1.amazonaws.com/bedrock-agentcore-agentcore_starter_strands
Getting or creating execution role for agent: agentcore_starter_strands
Using AWS region: us-east-1, account ID: 361769586364
Role name: AmazonBedrockAgentCoreSDKRuntime-us-east-1-9c0804ec0c
⠸ Launching Bedrock AgentCore...Role doesn't exist, creating new execution role: AmazonBedrockAgentCoreSDKRuntime-us-east-1-9c0804ec0c
Starting execution role creation process for agent: agentcore_starter_strands
✓ Role creating: AmazonBedrockAgentCoreSDKRuntime-us-east-1-9c0804ec0c
⠴ Launching Bedrock AgentCore...Creating IAM role: AmazonBedrockAgentCoreSDKRuntime-us-east-1-9c0804ec0c
✓ Role created: arn:aws:iam::361769586364:role/AmazonBedrockAgentCoreSDKRuntime-us-east-1-9c0804ec0c
⠦ Launching Bedrock AgentCore...✓ Execution policy attached: BedrockAgentCoreRuntimeExecutionPolicy-agentcore_starter_strands
Role creation complete and ready for use with Bedrock AgentCore
✅ Execution role available: arn:aws:iam::361769586364:role/AmazonBedrockAgentCoreSDKRuntime-us-east-1-9c0804ec0c
Preparing CodeBuild project and uploading source...
⠸ Launching Bedrock AgentCore...Getting or creating CodeBuild execution role for agent: agentcore_starter_strands
Role name: AmazonBedrockAgentCoreSDKCodeBuild-us-east-1-9c0804ec0c
⠼ Launching Bedrock AgentCore...CodeBuild role doesn't exist, creating new role: AmazonBedrockAgentCoreSDKCodeBuild-us-east-1-9c0804ec0c
Creating IAM role: AmazonBedrockAgentCoreSDKCodeBuild-us-east-1-9c0804ec0c
⠧ Launching Bedrock AgentCore...✓ Role created: arn:aws:iam::361769586364:role/AmazonBedrockAgentCoreSDKCodeBuild-us-east-1-9c0804ec0c
Attaching inline policy: CodeBuildExecutionPolicy to role: AmazonBedrockAgentCoreSDKCodeBuild-us-east-1-9c0804ec0c
⠇ Launching Bedrock AgentCore...✓ Policy attached: CodeBuildExecutionPolicy
Waiting for IAM role propagation...
⠹ Launching Bedrock AgentCore...CodeBuild execution role creation complete: arn:aws:iam::361769586364:role/AmazonBedrockAgentCoreSDKCodeBuild-us-east-1-9c0804ec0c
⠏ Launching Bedrock AgentCore...Created S3 bucket: bedrock-agentcore-codebuild-sources-361769586364-us-east-1
Using dockerignore.template with 45 patterns for zip filtering
Including Dockerfile from /Users/sanhehu/Documents/GitHub/aws_bedrock_agent_core_poc-project/docs/source/02-Learn-Bedrock-Agent-Core/.bedrock_agentcore/agentcore_starter_strands in source.zip
Uploaded source to S3: agentcore_starter_strands/source.zip
⠸ Launching Bedrock AgentCore...Created CodeBuild project: bedrock-agentcore-agentcore_starter_strands-builder
Starting CodeBuild build (this may take several minutes)...
⠴ Launching Bedrock AgentCore...Starting CodeBuild monitoring...
⠦ Launching Bedrock AgentCore...🔄 QUEUED started (total: 0s)
⠏ Launching Bedrock AgentCore...✅ QUEUED completed in 1.0s
🔄 PROVISIONING started (total: 1s)
⠸ Launching Bedrock AgentCore...✅ PROVISIONING completed in 8.4s
🔄 DOWNLOAD_SOURCE started (total: 9s)
⠋ Launching Bedrock AgentCore...✅ DOWNLOAD_SOURCE completed in 2.1s
🔄 BUILD started (total: 12s)
⠼ Launching Bedrock AgentCore...✅ BUILD completed in 11.5s
🔄 POST_BUILD started (total: 23s)
⠹ Launching Bedrock AgentCore...✅ POST_BUILD completed in 6.3s
🔄 COMPLETED started (total: 29s)
⠦ Launching Bedrock AgentCore...✅ COMPLETED completed in 1.0s
🎉 CodeBuild completed successfully in 0m 30s
CodeBuild completed successfully
✅ CodeBuild project configuration saved
Deploying to Bedrock AgentCore...
Passing memory configuration to agent: agentcore_starter_strands_mem-zkwWWiDDwr
⠋ Launching Bedrock AgentCore...✅ Agent created/updated: arn:aws:bedrock-agentcore:us-east-1:361769586364:runtime/agentcore_starter_strands-TOMXiiF4vl
Observability is enabled, configuring Transaction Search...
⠹ Launching Bedrock AgentCore...Created/updated CloudWatch Logs resource policy
⠸ Launching Bedrock AgentCore...Configured X-Ray trace segment destination to CloudWatch Logs
X-Ray indexing rule already configured
✅ Transaction Search configured: resource_policy, trace_destination
🔍 GenAI Observability Dashboard:
   https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#gen-ai-observability/agent-core
Polling for endpoint to be ready...
⠹ Launching Bedrock AgentCore...Agent endpoint: arn:aws:bedrock-agentcore:us-east-1:361769586364:runtime/agentcore_starter_strands-TOMXiiF4vl/runtime-endpoint/DEFAULT
Deployment completed successfully - Agent: arn:aws:bedrock-agentcore:us-east-1:361769586364:runtime/agentcore_starter_strands-TOMXiiF4vl
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── Deployment Success ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Agent Details:                                                                                                                                                                                                                                                                                             │
│ Agent Name: agentcore_starter_strands                                                                                                                                                                                                                                                                      │
│ Agent ARN: arn:aws:bedrock-agentcore:us-east-1:361769586364:runtime/agentcore_starter_strands-TOMXiiF4vl                                                                                                                                                                                                   │
│ ECR URI: 361769586364.dkr.ecr.us-east-1.amazonaws.com/bedrock-agentcore-agentcore_starter_strands:latest                                                                                                                                                                                                   │
│ CodeBuild ID: bedrock-agentcore-agentcore_starter_strands-builder:0bc9a9ba-66f5-4f9f-bf8f-7d1bf43e441e                                                                                                                                                                                                     │
│                                                                                                                                                                                                                                                                                                            │
│ 🚀 ARM64 container deployed to Bedrock AgentCore                                                                                                                                                                                                                                                           │
│                                                                                                                                                                                                                                                                                                            │
│ Next Steps:                                                                                                                                                                                                                                                                                                │
│    agentcore status                                                                                                                                                                                                                                                                                        │
│    agentcore invoke '{"prompt": "Hello"}'                                                                                                                                                                                                                                                                  │
│                                                                                                                                                                                                                                                                                                            │
│ 📋 CloudWatch Logs:                                                                                                                                                                                                                                                                                        │
│    /aws/bedrock-agentcore/runtimes/agentcore_starter_strands-TOMXiiF4vl-DEFAULT --log-stream-name-prefix "2025/10/23/[runtime-logs]"                                                                                                                                                                       │
│    /aws/bedrock-agentcore/runtimes/agentcore_starter_strands-TOMXiiF4vl-DEFAULT --log-stream-names "otel-rt-logs"                                                                                                                                                                                          │
│                                                                                                                                                                                                                                                                                                            │
│ 🔍 GenAI Observability Dashboard:                                                                                                                                                                                                                                                                          │
│    https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#gen-ai-observability/agent-core                                                                                                                                                                                                         │
│                                                                                                                                                                                                                                                                                                            │
│ ⏱️  Note: Observability data may take up to 10 minutes to appear after first launch                                                                                                                                                                                                                         │
│                                                                                                                                                                                                                                                                                                            │
│ 💡 Tail logs with:                                                                                                                                                                                                                                                                                         │
│    aws logs tail /aws/bedrock-agentcore/runtimes/agentcore_starter_strands-TOMXiiF4vl-DEFAULT --log-stream-name-prefix "2025/10/23/[runtime-logs]" --follow                                                                                                                                                │
│    aws logs tail /aws/bedrock-agentcore/runtimes/agentcore_starter_strands-TOMXiiF4vl-DEFAULT --log-stream-name-prefix "2025/10/23/[runtime-logs]" --since 1h                                                                                                                                              │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
