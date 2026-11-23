# GraphRAG vs Vector RAG: Credit Risk Analysis

## Project Overview

This Proof of Concept (PoC) compares traditional Vector Retrieval-Augmented Generation (Vector RAG) with a Knowledge Graph-based approach (GraphRAG) for credit risk analysis.

The objective is to demonstrate how relationships between customers, companies, and loans can reveal financial risks that may be missed when analyzing textual information alone.

The project uses synthetic banking data and Neo4j to explore relationship-aware decision support.

## Business Problem

Traditional credit risk assessments may focus primarily on individual customer information.

However, a customer who appears financially reliable may have indirect connections to companies with problematic loan histories.

This project investigates whether graph-based relationship analysis can identify these hidden risks.

## Technologies Used

- Python 3.13
- Neo4j Aura
- Knowledge Graphs
- Vector Embeddings and Cosine Similarity
- Hugging Face SentenceTransformers
- Pandas and Faker
- GraphRAG

## Knowledge Graph Structure

**Node Types**
- Customer
- Company
- Loan

**Relationship Types**
- HIDDEN_PARTNER
- FUNDER
- USED_LOAN

The graph connects customers to companies and loans, enabling the analysis of indirect financial relationships.

## Experimental Scenario

A synthetic customer appears eligible for credit based on their individual profile.

However, the knowledge graph reveals an indirect connection to a company associated with an overdue loan.

### Vector RAG Result

**LOAN CAN BE APPROVED**

The text-based retrieval approach does not identify the indirect financial risk in the tested scenario.

### GraphRAG Result

**LOAN MUST BE REJECTED**

The graph-based approach identifies the relationship between the customer, the connected company, and the overdue loan.

## Key Findings

This PoC illustrates that relationship-aware analysis can provide additional risk information beyond individual customer profiles.

The results represent a controlled synthetic test scenario, not a benchmark of all Vector RAG and GraphRAG implementations.

## Repository Structure

- `1_veri_uretici.py` — Synthetic banking data generation
- `2_neo4j_yukle.py` — Neo4j graph data loading
- `3_vector_rag_test.py` — Vector RAG testing
- `3b_vector_rag_sorgu.py` — Vector retrieval queries
- `4_graphrag_test.py` — Graph-based credit risk analysis
- `requirements.txt` — Python dependencies

## Data and Security

This project uses synthetic data for demonstration and experimentation.

Database credentials are managed through environment variables and are not included in the repository.

The generated Excel datasets are not currently included in the public repository.

## Potential Applications

- Banking and financial risk assessment
- Fraud detection
- Relationship-based risk analysis
- Knowledge Graph-powered decision support
- Explainable financial analysis

## Conclusion

This Proof of Concept demonstrates how Knowledge Graphs can complement traditional retrieval approaches by exposing indirect relationships relevant to credit risk assessment.

The findings highlight the potential value of GraphRAG for relationship-aware financial decision support.
