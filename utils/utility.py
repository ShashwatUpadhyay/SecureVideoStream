import os
import subprocess
from django.conf import settings


def convert_to_hls(video):
    """
    Convert MP4 video to HLS format (.m3u8 + .ts files)
    :param input_video_path: full path to the .mp4 file
    :param output_dir: directory where the HLS files will be saved
    :return: path to the generated .m3u8 playlist
    """
    # if not os.path.exists(output_dir):
    #     os.makedirs(output_dir)


    input_path = os.path.join(settings.MEDIA_ROOT,video.video.name)
    output_dir = os.path.join(settings.MEDIA_ROOT, 'hls_video', str(video.uid))
    # Output playlist path
    # output_playlist = os.path.join(output_dir,'playlist.m3u8')

    print('-----------------------------------------')
    print(input_path)
    print(output_dir)
    print('-----------------------------------------')
    command = [
            'ffmpeg',
            '-i', input_path,
            '-codec:', 'copy',
            '-start_number', '0',
            '-hls_time', '10',
            '-hls_list_size', '0',
            '-f', 'hls',
            output_dir
        ]


    try:
        subprocess.run(command, check=True)
        return output_dir
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg failed: {e}")
        return None
