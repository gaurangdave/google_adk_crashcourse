# Agent with other agents



## Thoughts
* Here is my understanding of different kinds of tools,
    * For simple `tool` like task that extends the capabilities of a Agent use `function tools`, e.g. performing RAG, calling API etc.
    * For simple `tool` like task that needs some intelligence use `agent as a tool`, so here the agent can use function tools, session state, memory etc to make intelligent decisions and return a response to the parent agent.
    * For complex tasks that involves multiple steps, intelligence and user input using sub agents where we can delegate the task to a the agent, the agent interacts with the user, has other sub agents, completes the tasks and gives the control back to the coordinator. 