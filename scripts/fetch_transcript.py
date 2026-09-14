#!/usr/bin/env python3
"""
YouTube動画の文字起こしを取得するスクリプト。

使い方:
    /usr/bin/python3 scripts/fetch_transcript.py VIDEO_ID --language ja,en

失敗時は YouTube Data API で説明欄（description）を取得してフォールバックする。
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request

from youtube_transcript_api import YouTubeTranscriptApi

KEY_PATH = '/home/victo/.hermes/secrets/youtube_api_key'


def fetch_description(video_id: str) -> str:
    """YouTube Data API で動画の説明欄・タイトルを取得"""
    key = open(KEY_PATH).read().strip()
    params = urllib.parse.urlencode(
        {'part': 'snippet', 'id': video_id, 'key': key})
    url = f'https://www.googleapis.com/youtube/v3/videos?{params}'
    with urllib.request.urlopen(url, timeout=20) as r:
        data = json.loads(r.read())
    items = data.get('items', [])
    if not items:
        return ''
    sn = items[0]['snippet']
    return f"# title: {sn.get('title','')}\n# channel: {sn.get('channelTitle','')}\n\n{sn.get('description','')}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('video_id')
    ap.add_argument('--language', default='ja,en',
                    help='カンマ区切りの優先言語')
    args = ap.parse_args()

    langs = [l.strip() for l in args.language.split(',') if l.strip()]
    api = YouTubeTranscriptApi()

    transcript = None
    try:
        transcript = api.fetch(args.video_id, languages=langs)
    except Exception as e:
        print(f"# transcript fetch failed: {e}", file=sys.stderr)
        # 利用可能な言語を確認して再試行
        try:
            listed = api.list(args.video_id)
            codes = [t.language_code for t in listed]
            print(f"# available languages: {codes}", file=sys.stderr)
            for code in codes:
                try:
                    transcript = api.fetch(args.video_id, languages=[code])
                    break
                except Exception:
                    continue
        except Exception as e2:
            print(f"# list failed: {e2}", file=sys.stderr)

    if transcript is not None:
        found = getattr(transcript, 'language_code', '')
        print(f"# language: {found}", file=sys.stderr)
        for snip in transcript:
            text = snip.text.replace('\n', ' ')
            print(text)
        sys.exit(0)

    # フォールバック: 説明欄
    print("# FALLBACK: description via YouTube Data API", file=sys.stderr)
    desc = fetch_description(args.video_id)
    if desc:
        print(desc)
        sys.exit(0)

    print("ERROR: no transcript and no description available", file=sys.stderr)
    sys.exit(1)


if __name__ == '__main__':
    main()
