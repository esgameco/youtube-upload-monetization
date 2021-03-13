import os
from youtube_upload_monetization import YouTubeUploader
from selenium_firefox.firefox import Firefox
from pathlib import Path


def test_upload(video_path: str, metadata: dict):
    current_working_dir = str(Path.cwd())
    browser = Firefox(current_working_dir, current_working_dir)
    uploader = YouTubeUploader(video_path, metadata, browser)
    # if not using monetization, use:
    # was_video_uploaded, video_id = uploader.upload(False)
    was_video_uploaded, video_id = uploader.upload()
    assert was_video_uploaded

# export T_VIDEO_PATH={video_path}
test_upload(os.getenv('T_VIDEO_PATH'), {
    'title': 'test',
    'description': 'test',
    'tags': 'test'
})