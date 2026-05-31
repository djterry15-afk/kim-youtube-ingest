import os
import sys
from datetime import date

import anthropic
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi

from fetch_transcript import get_video_id

load_dotenv()

DEFAULT_PROMPT = "prompts/extract-default.md"
LOG_FILE = "logs/ingestion_log.md"
MODEL = "claude-sonnet-4-6"


def get_transcript(video_id):
    api = YouTubeTranscriptApi()
    entries = api.fetch(video_id)
    return " ".join(entry.text for entry in entries)


def distill(transcript, prompt_text, url):
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    today = date.today().isoformat()

    user_message = f"""{prompt_text}

---

METADATA
URL: {url}
Date: {today}

TRANSCRIPT
{transcript}"""

    response = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        messages=[{"role": "user", "content": user_message}],
    )
    return response.content[0].text


def append_to_log(output):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("\n" + output + "\n")


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python ingest.py <youtube_url> [--prompt prompts/my-prompt.md]")
        sys.exit(1)

    url = args[0]
    prompt_file = DEFAULT_PROMPT

    if "--prompt" in args:
        idx = args.index("--prompt")
        if idx + 1 < len(args):
            prompt_file = args[idx + 1]

    video_id = get_video_id(url)
    if not video_id:
        print(f"Error: could not parse video ID from: {url}")
        sys.exit(1)

    print(f"Fetching transcript ({video_id})...")
    transcript = get_transcript(video_id)
    print(f"Transcript: {len(transcript.split())} words")

    with open(prompt_file, "r", encoding="utf-8") as f:
        prompt_text = f.read()

    print("Distilling with Claude...")
    output = distill(transcript, prompt_text, url)

    append_to_log(output)
    print(f"Done — logged to {LOG_FILE}")
    print("\n" + "=" * 60)
    print(output)


if __name__ == "__main__":
    main()
