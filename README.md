
# CogniGraph AI — Technorazz 2026 Prototype

## What this prototype demonstrates
1. Document ingestion (demo text or uploaded `.txt`)
2. Automatic concept extraction
3. Prerequisite knowledge graph
4. 5-question diagnostic micro-quiz
5. Learning-gap detection
6. Real-time graph highlighting
7. Dynamic 3-step remediation path

## Run in VS Code

### 1. Open terminal in this folder
```bash
cd CogniGraph_AI_Prototype
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the prototype
```bash
streamlit run app.py
```

Your browser will open the CogniGraph AI prototype.

## 2-minute hackathon demo
- Select **Python Basics**
- Click **Build Knowledge Graph**
- Show the graph
- Answer some quiz questions incorrectly
- Click **Diagnose Learning Gaps**
- Show red gap nodes
- Show the 3-step remediation path

## Important
This is a working MVP/demo prototype. The PPT describes LLM-based PDF parsing, NetworkX DAG validation, D3/Streamlit/React visualization and APIs. Those production integrations can be connected later; this version is designed for a fast live VS Code demonstration.
