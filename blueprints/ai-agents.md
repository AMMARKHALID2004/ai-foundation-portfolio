# AI Agents specialization blueprint

Entry: common foundation and PyTorch, followed by **HF LLM chapters 1–5 and 9** before agent specialization. Agent frameworks do not replace model/retrieval/evaluation understanding. Guide estimate: 10–14 weeks after LLM prerequisites.

## Required course sequence

1. [HF Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction): fundamentals, tools/actions/observations/messages, smolagents/LlamaIndex/LangGraph, agentic RAG and final project; 4–5 weeks. Include observability/evaluation bonus material.
2. [HF MCP Course](https://huggingface.co/learn/mcp-course/unit0/introduction): architecture, end-to-end app, custom server, external tools/data, deployment/evaluation; approximately 3 weeks.
3. [Microsoft AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners): selected design patterns, tools, agentic RAG, trust, planning, multi-agent design, production, protocols, context engineering, memory, scaling and security; 3–4 weeks selectively.

## Repository modules

`00-llm-prerequisite/`, `01-agent-tools-loops/`, `02-agentic-rag/`, `03-mcp-client-server/`, `04-memory-planning/`, `05-evaluation-security/`. Include tool schemas, traces/tests, at least two approaches compared, a working MCP client/server and documented setup/security.

## Separate capstone gates

- [ ] At least three defined tools and retrieval from an external knowledge source.
- [ ] MCP or another documented interface, and human approval before consequential actions.
- [ ] Structured logs/traces, normal and adversarial evaluation tasks.
- [ ] Task success, tool-selection accuracy and hallucination evaluation.
- [ ] Token, latency and cost analysis; injection/unauthorized-tool protections.
- [ ] Graceful failure/recovery; reproducible repo, report and demo.

Start with a single-agent baseline. Add multiple agents only if experiments demonstrate a measurable advantage. Discuss a research assistant, proposal-review agent, folder-audit assistant or secure knowledge workflow; no topic is selected here.
