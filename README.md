# NOBODY ASKED — YouTube Shorts Production Toolkit

A Python + FFmpeg helper for assembling vertical short-form videos from narration and background footage. The channel concept documented here is a faceless English-language channel for a US audience, focused on humorous, weird, and unexpected facts. The publishing plan discussed for the concept is three Shorts per day.

## Included tool
`shorts_builder.py` combines a narration audio file with looping background footage, crops it to a vertical 9:16 frame, matches the video length to the narration, and exports an MP4.

### Requirements
- Python 3.9+
- FFmpeg and FFprobe installed and available on PATH
- A narration file you have rights to use
- Background footage you have rights to use

No Python packages or API keys are required for the video assembly helper.

### Usage
```bash
python shorts_builder.py --audio assets/narration.mp3 --video assets/background.mp4 --output output/short.mp4
```

Optional output settings:
```bash
python shorts_builder.py --audio narration.wav --video footage.mp4 --output output/short.mp4 --width 1080 --height 1920 --fps 30
```

The tool writes H.264 video with AAC audio. Check the exported video before publishing.

## Narration workflow
The channel concept previously selected uses ElevenLabs' **Roger — Laid-Back, Casual, Resonant** voice with the **Eleven v4** model. Generate or export narration from your authorized ElevenLabs account, then pass the audio file to this tool. Do not put API keys or account credentials in this repository.

## Suggested production checklist
1. Research and fact-check a short, surprising fact.
2. Write an original concise script and verify factual claims.
3. Generate narration using a voice you are licensed to use.
4. Select licensed/owned background footage.
5. Run `shorts_builder.py`.
6. Review captions, pacing, audio levels, factual accuracy, and platform requirements.
7. Publish manually or through an approved YouTube API workflow.

## Project status and scope
This repository contains a working local video-assembly utility and a documented production workflow. It does **not** claim that cloud scheduling, script research, ElevenLabs API calls, or automatic YouTube publishing are implemented here. Those integrations require account credentials, permissions, and additional implementation/testing.

## Safety
Never commit API keys, OAuth tokens, cookies, or private channel credentials. Respect copyright and YouTube policies. Do not publish unverified facts.

## License
MIT
