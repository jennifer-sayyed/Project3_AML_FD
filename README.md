<<<<<<< HEAD
# Project3_AML_FD
AI-powered AML &amp; Fraud Detection Co-Pilot using RAG, FAISS, FastAPI, Streamlit, and OpenAI to support banking compliance, sanctions screening, SAR/STR investigations, and regulatory knowledge retrieval.
=======
# AML & Fraud Detection Co-Pilot

## Overview

AML & Fraud Detection Co-Pilot is an AI-powered Banking Compliance Assistant that helps AML Analysts, Compliance Officers, Fraud Investigators, Risk Teams, and Operations personnel quickly access regulatory guidance, sanctions procedures, AML typologies, and historical suspicious activity reports through a Retrieval-Augmented Generation (RAG) architecture.

The system combines:

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Vector Search (ChromaDB)
- Regulatory Knowledge Bases
- Rule-Based Compliance Logic
- Citation-Based Responses

The solution is designed to reduce investigation time, improve consistency in compliance decisions, and provide explainable responses grounded in approved regulatory documents.

---

## Business Problem

Financial institutions deal with large volumes of:

- AML investigations
- Fraud alerts
- KYC reviews
- Sanctions screening
- PEP onboarding reviews
- STR/SAR filing decisions

Compliance officers must search across multiple sources such as:

- FATF Guidance
- RBI Master Directions
- FIU-IND Circulars
- OFAC Sanctions Lists
- Internal Policies
- Historical SAR Narratives

The AML & Fraud Detection Co-Pilot provides a single AI interface to retrieve, analyze, and explain regulatory information with proper source citations.

---

## Key Features

### 1. FATF Typology Search

Example:

> Describe the typical structuring pattern in cash-intensive businesses per FATF guidance.

Capabilities:

- Retrieve FATF typology reports
- Explain money laundering patterns
- Highlight risk indicators

---

### 2. Regulatory Guidance Search

Example:

> What is the deadline for filing an STR to FIU-IND after detection?

Capabilities:

- Search RBI directions
- Search FIU guidance
- Provide source references

---

### 3. Sanctions Screening Assistance

Example:

> What action is required when an OFAC SDN match is detected above 90% confidence?

Capabilities:

- Rule-based recommendations
- Escalation workflows
- Risk classification

---

### 4. Historical SAR Recall

Example:

> Find SARs involving structuring patterns across multiple branches.

Capabilities:

- Semantic search
- Similar case retrieval
- Pattern comparison

---

### 5. PEP Workflow Assistance

Example:

> What is the escalation process for onboarding a PEP?

Capabilities:

- EDD guidance
- Approval workflow retrieval
- Internal procedure lookup

---

### 6. Jurisdiction Risk Assessment

Example:

> Which jurisdictions are on the FATF grey list?

Capabilities:

- High-risk jurisdiction lookup
- Screening recommendations

---

### 7. Multi-Document Analysis

Example:

> Combining FATF guidance and RBI directions, what are best practices for monitoring shell company indicators?

Capabilities:

- Cross-document reasoning
- Evidence synthesis

---

### 8. Risk Assessment Support

Example:

> Customer transaction velocity tripled. Does this require an STR?

Capabilities:

- Pattern reasoning
- Policy-based interpretation
- Risk recommendation

---

### 9. Hallucination Prevention

Example:

> What is our DeFi policy?

If no policy exists in the corpus:
>>>>>>> 40797fa8 (Project3_AML_FD)
