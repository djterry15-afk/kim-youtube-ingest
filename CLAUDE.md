# kim-youtube-ingest

YouTube URL in → transcript extracted → Claude distills structured insights → appended to a markdown log.

## Folder structure

```
kim-youtube-ingest/
├── prompts/                       ← Layer 3: reference material — edit to customize
│   ├── extract-default.md         ← Default extraction prompt (Clief Notes format)
│   └── extract-custom-example.md  ← How to adapt for a specific domain
├── logs/                          ← Layer 4: working artifacts — your output, gitignored
├── ingest.py                      ← The pipeline (~60 lines, rarely needs editing)
├── .env                           ← Your API key (create from .env.example)
└── requirements.txt
```

The prompt file is the thing to edit. `ingest.py` is plumbing.

## Navigation

| Task | Go here |
|------|---------|
| Change what gets extracted | `prompts/extract-default.md` |
| Build a domain-specific version | Copy and edit `extract-custom-example.md` |
| Review output | `logs/ingestion_log.md` |
| Install and run | `README.md` |
