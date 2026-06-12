# building-ai-assignment-02-starter

* TODO: Check of completed boxes with an x like this - [x]
* TODO: Clone this repo - [x]
* TODO: Change Title in Readme - []
* TODO: Fill out the information below - []

Name: Please Enter Name

Student Number: Please Enter Student Number

Github Repo URL:  Please provide the github repo URL for THIS repo as sometimes github usernames can get mixed up and you will be zipping this directory to go up to moodle. 

----

# Getting Started

Requirements: You MUST use a .venv and a requirements.txt

TODO: How to get going, run and interact - []

This section should be followable by someone cloning your repo for the first time, marks will be lost for omitted instructions.


# Self Assessment

TODO: X the boxes you completed and include BRIEF clarification where asked - []



## Assignment 2a

1. **Specialised Agent Architecture: Build at least 3 specialised agents** 
   - Triage Agent: Classify urgency, route to appropriate handler - []
   - Information Agent: Uses advanced RAG with query decomposition - []
   - Action Agent: Executes operations via tool calling - []
   - Agents must communicate and coordinate - []

```mermaid
sequenceDiagram
    actor User
    participant main as main.py
    participant decomp as Triage.decompose()
    participant wf as LangGraph workflow
    participant triage as Triage node
    participant agent as Specialist agent
    participant llm as OpenAI LLM
    participant mcp as MCP server

    User->>main: types query
    main->>decomp: decompose(query)
    decomp->>llm: LLM call — detect complex query
    llm-->>decomp: {"complex": false}
    decomp-->>main: simple query

    main->>wf: workflow.invoke(state)
    wf->>triage: triage_node(state)
    triage->>llm: LLM call — is_safe + rewrite? + classify
    llm-->>triage: {"category": "technical", "route_to": "TechnicalAgent"}
    triage-->>wf: updated state

    wf->>agent: technical_node(state)
    agent->>llm: LLM call — handoff needed?
    llm-->>agent: no handoff
    agent->>llm: LLM call — generate hypothesis (HyDE)
    llm-->>agent: hypothetical document
    agent->>agent: HybridRetriever.retrieve(hypothesis)
    agent->>llm: LLM call — generate response
    llm-->>agent: response
    agent-->>wf: updated state

    wf-->>main: result
    main->>main: log_interaction()
    main-->>User: prints response
```

```mermaid
flowchart TD
    Q([User query]) --> T

    T[Triage agent\nclassify · rewrite · decompose]

    T -->|general / bulk| G[General agent\nRAG + HyDE]
    T -->|technical| TE[Technical agent\nRAG + HyDE + web search]
    T -->|returns| R[Returns agent\npolicy_001]
    T -->|warranty| W[Warranty agent\npolicy_002]
    T -->|delivery| D[Delivery agent\npolicy_003]
    T -->|loop detected| E[Escalation]

    G -->|handoff| T
    TE -->|handoff| T

    R -->|ready_for_action| A
    W -->|ready_for_action| A
    D -->|ready_for_action| A

    R -->|handoff| T
    W -->|handoff| T
    D -->|handoff| T

    A[Action agent\nMCP — orders · refunds · inventory]

    G --> END([Response])
    TE --> END
    A --> END
    E --> END

    style T fill:#7F77DD,color:#fff
    style G fill:#1D9E75,color:#fff
    style TE fill:#1D9E75,color:#fff
    style R fill:#185FA5,color:#fff
    style W fill:#185FA5,color:#fff
    style D fill:#185FA5,color:#fff
    style A fill:#D85A30,color:#fff
    style E fill:#888780,color:#fff
```

2. **Query Decomposition & Multi-Step Reasoning: Handle complex requests** 
   - Must break down into sub-problems - []
   - Execute multiple retrieval operations - []
   - Synthesise comprehensive response - []

3. **Tool Integration: Connect to simulated backend systems (you'll provide mock APIs)**
   - At least 1 API connected - []
   - MCP used - []

4. **Advanced Retrieval Strategies: Implement at least 2 advanced techniques**
   - Query expansion/rewriting - []
   - Hypothetical document embeddings (HyDE) - []
   - Parent-child document chunking - []
   - Temporal/metadata boosting - []
   - Students choose and justify their approaches - []


