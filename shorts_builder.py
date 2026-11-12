"""Assemble a vertical YouTube Short from supplied narration and background video.

Requires FFmpeg and FFprobe on PATH. No API keys are needed.
Example:
  python shorts_builder.py --audio narration.mp3 --video background.mp4 --output output/short.mp4
"""
import argparse
import shutil
import subprocess
from pathlib import Path

def run(command):
    subprocess.run(command, check=True)

def main():
    parser = argparse.ArgumentParser(description="Build a 9:16 Short from voiceover + background footage.")
    parser.add_argument("--audio", required=True, help="Narration audio file (MP3/WAV/M4A)")
    parser.add_argument("--video", required=True, help="Background video file")
    parser.add_argument("--output", default="output/short.mp4", help="Output MP4 path")
    parser.add_argument("--width", type=int, default=1080)
    parser.add_argument("--height", type=int, default=1920)
    parser.add_argument("--fps", type=int, default=30)
    args = parser.parse_args()

    ffmpeg, ffprobe = shutil.which("ffmpeg"), shutil.which("ffprobe")
    if not ffmpeg or not ffprobe:
        raise SystemExit("FFmpeg and FFprobe are required. Install FFmpeg and ensure both are on PATH.")
    audio, video, output = Path(args.audio), Path(args.video), Path(args.output)
    if not audio.is_file() or not video.is_file():
        raise SystemExit("Input file not found. Check --audio and --video paths.")
    output.parent.mkdir(parents=True, exist_ok=True)

    probe = subprocess.run(
        [ffprobe, "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(audio)],
        check=True, capture_output=True, text=True
    )
    duration = float(probe.stdout.strip())
    if duration <= 0:
        raise SystemExit("Could not determine a valid narration duration.")

    video_filter = (
        f"scale={args.width}:{args.height}:force_original_aspect_ratio=increase,"
        f"crop={args.width}:{args.height},fps={args.fps},setsar=1"
    )
    command = [
        ffmpeg, "-y", "-stream_loop", "-1", "-i", str(video), "-i", str(audio),
        "-map", "0:v:0", "-map", "1:a:0", "-vf", video_filter,
        "-t", f"{duration:.3f}", "-c:v", "libx264", "-preset", "medium",
        "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart", "-shortest", str(output)
    ]
    print("Rendering vertical video…")
    run(command)
    print(f"Created: {output.resolve()} ({duration:.1f} seconds)")

if __name__ == "__main__":
    main()
