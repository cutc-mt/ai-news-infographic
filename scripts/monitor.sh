#!/bin/bash
# YouTube チャンネル監視 → API POST スクリプト
# cron jobから実行される。新着動画を検知してAPIにPOSTする。
# stdoutがcronのプロンプトに注入される。

set -e

export YOUTUBE_API_KEY="$(cat /home/victo/.hermes/secrets/youtube_api_key 2>/dev/null || echo '')"
NEWS_API_URL="https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news"

if [ -z "$YOUTUBE_API_KEY" ]; then
  echo "ERROR: YouTube API key not found"
  exit 1
fi

cd /home/victo/work/ai-news-infographic/scripts

# 監視 + POST実行
/usr/bin/python3 post_news.py 2>&1
