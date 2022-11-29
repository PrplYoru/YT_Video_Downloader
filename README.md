<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">YTVideoDownloader</h3>

  <p align="center">
    GUI Youtube Video Downloader
    <br>
    <a href="https://github.com/Edoardo-Morosanu/YT_Video_Downloader/issues">Report Bug</a>
    ·
    <a href="https://github.com/Edoardo-Morosanu/YT_Video_Downloader/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#download-private-videos">Download private/members-only videos</li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A simple gui youtube video downloader built with python, pytube, ffmpeg, tkinter and yt-dlp. 

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Pytube](https://pytube.io/)
* [TKinter](http://tkdocs.com/)
* [Yt-dlp](https://github.com/yt-dlp/yt-dlp)
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started
This will guide you through the installation of the program.

### Installation

1. Clone the repo
   ```sh
   $ git clone https://github.com/Edoardo-Morosanu/YT_Video_Downloader.git
   ```
2. Install various requirements if not already installed
   ```sh
   $ pip install -r requirements.txt
   ```
3. Start the program
    ```sh
    $ python main.py
   ```

<p>PROGRAM NOT RESPONDING IS NORMAL.</p>


<p align="right">(<a href="#top">back to top</a>)</p>

## Download private videos

This will guide you through the process of downloading private and members-only videos.

First of all download an extension to export the cookies from youtube to a txt file, like:
* [Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid?hl=en)

After doing so, go to any members-only video you have access to, and search for the extension icon(Half-eaten cookie), click on it and then click export.<br/>
Save the txt file as "**cookies.txt**" in the program folder. After you've done all of this, open the program, and select yes in the members-only/private video dropdown menu, the video will be automatically downloaded. <br/>
There's no need to export the cookie file again, unless it gives you any access problems.

<!-- ROADMAP -->
## Roadmap

- [2022/06/21] Complete remake of the UI with TKinter
- [2022/06/21] Custom destination folder
- [2022/06/21] Option to choose quality of video
  - [2022/06/21] Up to 4k
- [2022/07/18] Added option to download members-only and private videos
- [2022/11/29] Modernized UI using CustomTkinter
- [??/??/??] Reorganize UI

See the [open issues](https://github.com/Edoardo-Morosanu/YT_Video_Downloader/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Any contributions are **greatly appreciated**.

If you have a suggestion that would make the program better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Edoardo Morosanu - [@Twitter](https://twitter.com/EdoardoMorosanu) - o8qq@proton.me

Project Link: [https://github.com/Edoardo-Morosanu/YT_Video_Downloader](https://github.com/Edoardo-Morosanu/YT_Video_Downloader)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Edoardo-Morosanu/YT_Video_Downloader.svg?style=for-the-badge
[contributors-url]: https://github.com/Edoardo-Morosanu/YT_Video_Downloader/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Edoardo-Morosanu/YT_Video_Downloader.svg?style=for-the-badge
[forks-url]: https://github.com/Edoardo-Morosanu/YT_Video_Downloader/network/members
[stars-shield]: https://img.shields.io/github/stars/Edoardo-Morosanu/YT_Video_Downloader.svg?style=for-the-badge
[stars-url]: https://github.com/Edoardo-Morosanu/YT_Video_Downloader/stargazers
[issues-shield]: https://img.shields.io/github/issues/Edoardo-Morosanu/YT_Video_Downloader.svg?style=for-the-badge
[issues-url]: https://github.com/Edoardo-Morosanu/YT_Video_Downloader/issues
[license-shield]: https://img.shields.io/github/license/Edoardo-Morosanu/YT_Video_Downloader.svg?style=for-the-badge
[license-url]: https://github.com/Edoardo-Morosanu/YT_Video_Downloader/blob/master/LICENSE.txt
