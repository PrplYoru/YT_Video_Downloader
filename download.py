import yt_dlp

def download(filetp, link, qual, path, filename):
    if filename == '':
        with yt_dlp.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(link, download=False)
            filename = info_dict.get('title', None)
    if filetp == 'Audio':
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{path}/{filename}.mp3',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
        except:
            print('Connection Error')
    elif filetp == 'Video':
        try:
            ydl_opts = {
                'format': f'bestvideo[ext=mp4][height={qual}]',
                'outtmpl': f'{path}/{filename}.mp4',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
        except:
            print('Connection Error')
    elif filetp == 'Both':
        try:
            ydl_opts = {
                'format': f'bestvideo[height={qual}]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': f'{path}/{filename}.mp4',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
        except:
            print('Connection Error')
    else:
        print('Invalid File Type')
