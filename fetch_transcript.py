import re
import sys

from youtube_transcript_api import YouTubeTranscriptApi


def get_video_id(url):
    patterns = [
        r"(?:v=)([0-9A-Za-z_-]{11})",
        r"(?:youtu\.be\/)([0-9A-Za-z_-]{11})",
        r"(?:embed\/)([0-9A-Za-z_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_transcript.py <youtube_url>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    video_id = get_video_id(url)

    if not video_id:
        print(f"Error: could not parse video ID from: {url}", file=sys.stderr)
        sys.exit(1)

    api = YouTubeTranscriptApi()
    entries = api.fetch(video_id)
    transcript = " ".join(entry.text for entry in entries)
    print(transcript)


if __name__ == "__main__":
    main()
