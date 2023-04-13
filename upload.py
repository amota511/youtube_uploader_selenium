import argparse
from youtube_uploader_selenium import YouTubeUploader
from typing import Optional


def main(video_path: str,
         video_title: str):
    uploader = YouTubeUploader(video_path, video_title)
    was_video_uploaded, video_id = uploader.upload()
    assert was_video_uploaded


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video",
                        help='Path to the video file',
                        required=True)
    parser.add_argument("--title",
                        help='Title of the video',
                        required=True)
    # parser.add_argument("-t",
    #                     "--thumbnail",
    #                     help='Path to the thumbnail image')
    # # parser.add_argument("--meta", help='Path to the JSON file with metadata')
    # parser.add_argument("--profile", help='Path to the firefox profile')
    args = parser.parse_args()

    main(args.video, args.title) 
    #, None, args.thumbnail, profile_path=args.profile)
    # main(args.video, args.meta, args.thumbnail, profile_path=args.profile)

