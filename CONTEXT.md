# CONTEXT.md
*Project: kim-youtube-ingest*

## What this is

A knowledge extraction pipeline for YouTube videos. Two modes:

- **Primary:** Claude Code in VS Code reads the transcript and applies the extraction prompt. No API key needed — uses your existing Claude subscription.
- **Secondary:** `ingest.py` calls the Claude API directly. Requires an API key. For automation or running without Claude Code open.

---

## Primary workflow — Claude Code in VS Code

When asked to ingest a YouTube URL:

1. Run `python fetch_transcript.py <url>` — prints the raw transcript to stdout
2. Read `prompts/extract-default.md` — these are your extraction instructions
3. Apply those instructions to the transcript
4. Write the structured output to `logs/ingestion_log.md`
5. Confirm the entry was added and print it to the chat

To use a domain-specific prompt instead of the default:
- Same steps, but read the relevant file from `prompts/` instead
- Example: `prompts/extract-custom-example.md` for macro/investing content

---

## Secondary workflow — API script

```bash
python ingest.py <url>
python ingest.py <url> --prompt prompts/extract-custom-example.md
```

Requires `ANTHROPIC_API_KEY` in `.env`. See `.env.example`.

---

## Task routing

| Task | Action |
|------|--------|
| Ingest a video (Claude Code) | Ask Claude Code: "ingest this URL: `<url>`" |
| Ingest a video (API) | `python ingest.py <url>` |
| Change what gets extracted | Edit `prompts/extract-default.md` |
| Add a domain-specific prompt | Copy `extract-custom-example.md`, edit, save as `extract-[domain].md` |
| Review extracted knowledge | Open `logs/ingestion_log.md` |
