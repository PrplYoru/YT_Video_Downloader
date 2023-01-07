import yt_dlp, time, os

def download(filetp, link, qual, path, filename, priv):
    
    current_time = time.time()
    info_dict = yt_dlp.YoutubeDL().extract_info(link, download=False)

    quality_map = {
    '144p': '160',
    '240p': '133',
    '360p': '134',
    '480p': '135',
    '720p': '136',
    '1080p': '137',
    '1440p': '400',
    '2160p': '401',
    '4320p': '571'
    }

    qual = quality_map.get(qual, qual)

    if filename == '':
        with yt_dlp.YoutubeDL() as ydl:
            filename = info_dict.get('title', None)
    if filetp == 'Audio':
        try:
            if priv:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': f'{path}/{filename}.mp3',
                    'cookiefile': 'cookies.txt',
                }
            else:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': f'{path}/{filename}.mp3',
                }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                os.utime(f'{path}/{filename}.mp3', (current_time, current_time))
        except yt_dlp.utils.ExtractorError as e: 
            print(f'Error: {e}')
    elif filetp == 'Video':
        try:
            if priv:
                ydl_opts = {
                    'format': f'{qual}',
                    'outtmpl': f'{path}/{filename}.mp4',
                    'extract_audio': False,
                    'cookiefile': 'cookies.txt',
                }
            else:
                ydl_opts = {
                    'format': f'{qual}',
                    'outtmpl': f'{path}/{filename}.mp4',
                    'extract_audio': False,
                }
            if qual == '137':
                if ydl_opts['format'] in info_dict['formats']:
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([link])
                        os.utime(f'{path}/{filename}.mp4', (current_time, current_time))
                else:
                    print(f"ERROR: The format '{ydl_opts['format']}' is not available for this video, attempting to download with different framerate...")
                    ydl_opts['format'] = '299'
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([link])
                        os.utime(f'{path}/{filename}.mp4', (current_time, current_time))
            else:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
                    os.utime(f'{path}/{filename}.mp4', (current_time, current_time))
        except yt_dlp.utils.ExtractorError as e: 
            print(f'Error: {e}')
    elif filetp == 'Both':
        try:
            if priv:
                ydl_opts = {
                    'format': f'{qual}',
                    'outtmpl': f'{path}/{filename}.%(ext)s',
                    'merge_output_format': 'mp4',
                    'cookiefile': 'cookies.txt',
                }
            else:
                ydl_opts = {
                    'format': f'{qual}',
                    'outtmpl': f'{path}/{filename}.%(ext)s',
                    'merge_output_format': 'mp4',
                }
            if qual == '137':
                if ydl_opts['format'] in info_dict['formats']:
                    ydl_opts['format'] = f'{qual}+bestaudio/best'
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([link])
                        os.utime(f'{path}/{filename}.mp4', (current_time, current_time))
                else:
                    print(f"ERROR: The format '{ydl_opts['format']}' is not available for this video, attempting to download with different framerate...")
                    ydl_opts['format'] = '299+bestaudio/best'
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([link])
                        os.utime(f'{path}/{filename}.mp4', (current_time, current_time))
            else:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
                    os.utime(f'{path}/{filename}.mp4', (current_time, current_time))
        except yt_dlp.utils.ExtractorError as e: 
            print(f'Error: {e}')
    else:
        print('Invalid File Type')
