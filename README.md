# Hiring Compliance App Backend

This repository contains the backend for a Hiring Compliance application. The app is designed to evaluate adherence to hiring policies, including alignment with job descriptions, equal opportunity compliance, consistency with company policies, and thoroughness in decision-making.

# Description

The Hiring Compliance App leverages a Language Model (LLM) to assess compliance based on information such as interview transcripts, resumes, job descriptions, and hiring decisions. The backend handles queries to the LLM, structuring and formatting responses for the frontend to display in a predefined format.

# Requirements

- Python: Version 3.11 or higher (3.11 is recommended)
- NexaAI Compatibility: For local model execution, compatibility with NexaAI is required. [More information here](https://github.com/NexaAI/nexa-sdk).

# Installation

1. Set up a virtual environment (recommended to isolate dependencies):

```
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the Nexa server (if using a local model):

```
nexa server model_path
```

For additional details, refer to [NexaAI documentation](https://github.com/NexaAI/nexa-sdk/blob/main/SERVER.md).

4. Start the backend server:

```
uvicorn app:app --reload --port=8080
```


The backend server will now be running locally on port 8080, ready to process compliance queries for the Hiring Compliance App frontend.