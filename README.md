# kim-youtube-ingest

Extract structured knowledge from YouTube videos using Claude.

YouTube URL in → transcript fetched → Claude distills discrete insights → appended to a markdown log you can read, edit, and build on.

Not a summarizer. A knowledge extractor. The difference: summaries compress what was said. This extracts claims worth keeping — with mechanisms, implications, and open questions.

---

## How it works (two modes)

**Primary — VS Code + Claude Code extension (no API key needed)**
Claude Code fetches the transcript and does the distillation using your existing Claude subscription. You tell it what to do; it reads the prompt file and writes the output.

**Secondary — API script (requires Anthropic API key)**
A standalone Python script that calls the Claude API directly. Useful for automation or running without Claude Code open.

---

## Setup

```bash
git clone https://github.com/djterry15-afk/kim-youtube-ingest.git
cd kim-youtube-ingest
pip install -r requirements.txt
```

That's it for the primary workflow. No API key needed.

---

## Primary usage — VS Code + Claude Code

1. Open the `kim-youtube-ingest` folder in VS Code
2. Open Claude Code (the extension)
3. Say: **"ingest this URL: `https://www.youtube.com/watch?v=VIDEO_ID`"**

Claude Code reads `CONTEXT.md`, runs `fetch_transcript.py` to get the transcript, applies the extraction prompt from `prompts/extract-default.md`, and writes the structured output to `logs/ingestion_log.md`.

Your output accumulates in `logs/ingestion_log.md` — gitignored, stays local.

---

## Secondary usage — API script

Requires an Anthropic API key ([console.anthropic.com](https://console.anthropic.com)).

```bash
cp .env.example .env
# add your key to .env
pip install anthropic python-dotenv

python ingest.py https://www.youtube.com/watch?v=VIDEO_ID
python ingest.py <url> --prompt prompts/extract-custom-example.md
```

---

## Example output

```
---
## Why Structured Context Changes AI Output Quality
Source: https://www.youtube.com/watch?v=...
Ingested: 2026-05-30

- **Concept:** AI output quality is determined more by context architecture than by prompt length.
- **Mechanism:** Language models predict the next token based on all prior tokens — so poorly organized context produces poorly organized output. Structure in equals structure out.
- **So what:** Investing time in how you organize context files pays back more than investing time in writing longer prompts.
- **Open questions:** At what context window size does architectural organization matter less?
```

---

## How to customize

**The prompt file is the thing to edit.** `prompts/extract-default.md` controls what Claude looks for and how it formats output. Edit it to change extraction behavior — you never need to touch the scripts.

Two prompt files included:
- `extract-default.md` — AI systems & workflow architecture extraction (default)
- `extract-custom-example.md` — analyst variant: evaluating and comparing AI tools and approaches

To build a domain-specific version:
1. Copy `extract-custom-example.md`
2. Rename it (`extract-health.md`, `extract-strategy.md`, etc.)
3. Edit the "what you are looking for" section
4. Tell Claude Code to use it: *"ingest `<url>` using `prompts/extract-health.md`"*

---

## How it works

Three components, each with one job:

| Component | Job |
|-----------|-----|
| `fetch_transcript.py` | Fetch the transcript. No API key. One dependency. |
| `prompts/extract-default.md` | Tell Claude what to look for and how to format it. |
| `CONTEXT.md` | Tell Claude Code how to run the workflow when you ask it to ingest a URL. |

The `prompts/` folder is **Layer 3 configuration** — change what gets extracted without changing code. The `logs/` folder is **Layer 4 working artifacts** — your accumulated knowledge, gitignored and local.

This is an ICM-native architecture: the folder structure is the system. If you've taken the Clief Notes course, you've seen this pattern before — this is it running as a real tool.

---

## Folder structure

```
kim-youtube-ingest/
├── CLAUDE.md                      ← Agent context map
├── CONTEXT.md                     ← Workflow instructions for Claude Code
├── README.md
├── fetch_transcript.py            ← Transcript fetcher (no API key)
├── ingest.py                      ← API script (optional, requires key)
├── requirements.txt
├── .env.example                   ← API key template (only needed for ingest.py)
├── prompts/                       ← Layer 3: factory configuration — edit to customize
│   ├── extract-default.md         ← AI systems extraction (default)
│   └── extract-custom-example.md  ← Analyst variant example
└── logs/                          ← Layer 4: working artifacts — your output, stays local
    └── ingestion_log.md
```

---

## Requirements

- Python 3.8+
- VS Code + Claude Code extension (for primary workflow)
- Videos must have captions enabled — auto-generated captions work fine

---

## Part of KIM

This tool is Phase 1 of the Knowledge Ingestion Machine — a broader pipeline for structured knowledge capture across YouTube, articles, books, and research. Phase 1 is standalone and useful on its own.
