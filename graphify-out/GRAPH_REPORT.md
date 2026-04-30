# Graph Report - .  (2026-04-30)

## Corpus Check
- 11 files · ~38,607 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 35 nodes · 26 edges · 10 communities detected
- Extraction: 46% EXTRACTED · 54% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_AI Agent Frameworks|AI Agent Frameworks]]
- [[_COMMUNITY_Infographic Design Spec|Infographic Design Spec]]
- [[_COMMUNITY_Project Workflow Config|Project Workflow Config]]
- [[_COMMUNITY_Multimodal AI Analysis|Multimodal AI Analysis]]
- [[_COMMUNITY_Git Automation|Git Automation]]
- [[_COMMUNITY_Cloud Load Balancing|Cloud Load Balancing]]
- [[_COMMUNITY_Gemma4 Agent|Gemma4 Agent]]
- [[_COMMUNITY_Prometheus Monitoring|Prometheus Monitoring]]
- [[_COMMUNITY_A2A Protocol|A2A Protocol]]
- [[_COMMUNITY_Empty Output|Empty Output]]

## God Nodes (most connected - your core abstractions)
1. `Graphic Recording HTML Design Specification` - 6 edges
2. `18-Card HTML Infographic Template` - 4 edges
3. `Agency Agents - Multi-Agent Coding System with 146 Expert Agents` - 4 edges
4. `OpenClaw Security Issues and Self-Built Second Brain` - 3 edges
5. `AI News Infographic Generator Workflow` - 2 edges
6. `Gemini Project Rules for Infographic Generation` - 2 edges
7. `OpenClaw Markdown-Driven Memory System` - 2 edges
8. `OpenClaw Heartbeat Proactive Agent System` - 2 edges
9. `OpenClaw Multi-Platform Channel Adapters` - 2 edges
10. `Kilo Platform - KiloCLI, KiloCrow, KiloPath Integration` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Agency Agents - Multi-Agent Coding System with 146 Expert Agents` --semantically_similar_to--> `Multi-Agent Parallel Processing for Complex Tasks`  [INFERRED] [semantically similar]
  transcript_5Xky0iyiInc.txt → transcript_clean.txt
- `Gemini Project Rules for Infographic Generation` --semantically_similar_to--> `AI News Infographic Generator Workflow`  [INFERRED] [semantically similar]
  GEMINI.md → CLAUDE.md
- `OpenClaw Heartbeat Proactive Agent System` --semantically_similar_to--> `Agency Agents - Multi-Agent Coding System with 146 Expert Agents`  [INFERRED] [semantically similar]
  transcript_7wENq-LMHgQ.txt → transcript_5Xky0iyiInc.txt
- `OpenClaw Multi-Platform Channel Adapters` --semantically_similar_to--> `Kilo Platform - KiloCLI, KiloCrow, KiloPath Integration`  [INFERRED] [semantically similar]
  transcript_7wENq-LMHgQ.txt → transcript_5Xky0iyiInc.txt
- `AI News Infographic Generator Workflow` --references--> `Graphic Recording HTML Design Specification`  [EXTRACTED]
  CLAUDE.md → info-graphic-prompt.md

## Hyperedges (group relationships)
- **OpenClaw Four-Component Personal AI Architecture** — transcript_7wENq_memory_system, transcript_7wENq_heartbeat_system, transcript_7wENq_channel_adapters, transcript_7wENq_skills_registry [EXTRACTED 1.00]
- **Google Cloud Secure Agent Deployment Pipeline** — transcript_e8b_load_balancer_architecture, transcript_e8b_model_armor, transcript_e8b_adk_lite_llm, transcript_e8b_prometheus_sidecar, transcript_e8b_a2a_protocol [INFERRED 0.90]
- **YouTube-to-Infographic Generation Pipeline** — claude_md_youtube_workflow, info_graphic_prompt_design_spec, claude_md_18_card_template, claude_md_git_workflow, index_html_article_listing [EXTRACTED 1.00]

## Communities

### Community 0 - "AI Agent Frameworks"
Cohesion: 0.25
Nodes (9): Agency Agents - Multi-Agent Coding System with 146 Expert Agents, Kilo Platform - KiloCLI, KiloCrow, KiloPath Integration, AI Model Coding Benchmark: Opus 4.6 vs GLM5 vs GPT 5.4, OpenClaw Security Issues and Self-Built Second Brain, OpenClaw Multi-Platform Channel Adapters, OpenClaw Heartbeat Proactive Agent System, OpenClaw Markdown-Driven Memory System, OpenClaw Skills Registry (+1 more)

### Community 1 - "Infographic Design Spec"
Cohesion: 0.33
Nodes (7): AI News Infographic Generator Workflow, Gemini Project Rules for Infographic Generation, Card Animation Effects, Graphic Recording HTML Design Specification, Keyword Tag Highlight Component, 4-Column Responsive Layout, Handwritten Speech Bubble Component

### Community 2 - "Project Workflow Config"
Cohesion: 0.4
Nodes (5): 18-Card HTML Infographic Template, Per-Video Color Theme System, Font Awesome Icon Selection Guide, Japanese Natural Language Style Guide, YouTube-to-HTML Infographic Pipeline

### Community 3 - "Multimodal AI Analysis"
Cohesion: 0.67
Nodes (3): Meta AI Muse Spark - Multimodal Manga Analysis, Multi-Agent Parallel Processing for Complex Tasks, Visual Grounding Technique for AI Image Analysis

### Community 5 - "Git Automation"
Cohesion: 1.0
Nodes (2): Git Commit and Push Automation, AI News Infographics Article Index

### Community 6 - "Cloud Load Balancing"
Cohesion: 1.0
Nodes (2): Load Balancer with URL Map for Multi-Service Routing, Google Cloud Model Armor Security Service

### Community 8 - "Gemma4 Agent"
Cohesion: 1.0
Nodes (1): Secure Gemma 4 AI Agent Deployment on Google Cloud

### Community 9 - "Prometheus Monitoring"
Cohesion: 1.0
Nodes (1): Prometheus Sidecar for Custom LLM Metrics

### Community 10 - "A2A Protocol"
Cohesion: 1.0
Nodes (1): Agent-to-Agent (A2A) Protocol for Remote Agent Communication

### Community 11 - "Empty Output"
Cohesion: 1.0
Nodes (1): Empty Output File

## Knowledge Gaps
- **19 isolated node(s):** `YouTube-to-HTML Infographic Pipeline`, `Per-Video Color Theme System`, `Japanese Natural Language Style Guide`, `Git Commit and Push Automation`, `Font Awesome Icon Selection Guide` (+14 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Git Automation`** (2 nodes): `Git Commit and Push Automation`, `AI News Infographics Article Index`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Cloud Load Balancing`** (2 nodes): `Load Balancer with URL Map for Multi-Service Routing`, `Google Cloud Model Armor Security Service`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Gemma4 Agent`** (1 nodes): `Secure Gemma 4 AI Agent Deployment on Google Cloud`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Prometheus Monitoring`** (1 nodes): `Prometheus Sidecar for Custom LLM Metrics`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `A2A Protocol`** (1 nodes): `Agent-to-Agent (A2A) Protocol for Remote Agent Communication`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Empty Output`** (1 nodes): `Empty Output File`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Agency Agents - Multi-Agent Coding System with 146 Expert Agents` connect `AI Agent Frameworks` to `Multimodal AI Analysis`?**
  _High betweenness centrality (0.068) - this node is a cross-community bridge._
- **Why does `Multi-Agent Parallel Processing for Complex Tasks` connect `Multimodal AI Analysis` to `AI Agent Frameworks`?**
  _High betweenness centrality (0.032) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Agency Agents - Multi-Agent Coding System with 146 Expert Agents` (e.g. with `OpenClaw Heartbeat Proactive Agent System` and `Kilo Platform - KiloCLI, KiloCrow, KiloPath Integration`) actually correct?**
  _`Agency Agents - Multi-Agent Coding System with 146 Expert Agents` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `OpenClaw Security Issues and Self-Built Second Brain` (e.g. with `OpenClaw Markdown-Driven Memory System` and `OpenClaw Multi-Platform Channel Adapters`) actually correct?**
  _`OpenClaw Security Issues and Self-Built Second Brain` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `YouTube-to-HTML Infographic Pipeline`, `Per-Video Color Theme System`, `Japanese Natural Language Style Guide` to the rest of the system?**
  _19 weakly-connected nodes found - possible documentation gaps or missing edges._