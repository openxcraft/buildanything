#!/usr/bin/env bash
set -euo pipefail
# Preferred generator when espeak-ng is installed:
# espeak-ng -f media/audio/overview-transcript.txt -w /tmp/overview.wav
# ffmpeg -y -i /tmp/overview.wav -codec:a libmp3lame -q:a 4 media/audio/overview-tts.mp3
# This package includes a deterministic fallback MP3 cue when offline TTS is unavailable.
