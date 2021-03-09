import argparse
import os
from youtube_uploader_selenium import YouTubeUploader
from selenium_firefox.firefox import Firefox
from pathlib import Path
from typing import Optional


def main(video_path: str, metadata_path: Optional[str] = None):
    current_working_dir = str(Path.cwd())
    browser = Firefox(current_working_dir, current_working_dir)
    uploader = YouTubeUploader(video_path, metadata_path, browser)
    was_video_uploaded, video_id = uploader.upload()
    assert was_video_uploaded


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video",
                        help='Path to the video file',
                        required=True)
    parser.add_argument("--meta", help='Path to the JSON file with metadata')
    args = parser.parse_args()
    main(args.video, args.meta)
