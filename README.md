# SpotYT

Telegram Bot that helps you download direct MP3 file for personal uses.

<img src = "https://user-images.githubusercontent.com/65273165/82033717-c3b93600-96ba-11ea-9e65-bdd2022d63f3.png" height="100" width="100">



## Introduction
This is Telegram Bot that helps you download direct .mp3 file, using Spotify Track
link or YouTube Video link, directly into your memory for personal uses.

It contains a Python Library [python-telegram-bot](https://pypi.org/project/python-telegram-bot/) that provides a pure Python interface for the [Telegram Bot API](https://core.telegram.org/bots/api). It's compatible with Python versions 3.5+ and [PyPy](http://pypy.org/).

It also contain [spotdl](https://pypi.org/project/spotdl/) library which helps in downloading songs from YouTube in an MP3 format by using Spotify's HTTP link.




## Installation

You can install or upgrade python-telegram-bot with:

```
pip install python-telegram-bot --upgrade
```
You also have to install [spotdl](https://pypi.org/project/spotdl/) library.


```
pip install spotdl
```

## Running 
Go the directory where you have downloaded the files using `cd` for windows.
And then run the `SpotYT.py`
```bash
python SpotYT.py
```

## Usage

For the most basic usage, downloading tracks is as easy as

```
spotdl --song https://open.spotify.com/track/4HBZA5flZLE435QTztThqH
```
Check out the [Available options](https://github.com/ritiek/spotify-downloader/wiki/Available-options) wiki page for the list of currently available options with their description

## Screenshots



<img src = "https://user-images.githubusercontent.com/65273165/82029736-09730000-96b5-11ea-8964-7f10f80c2cb6.jpg" width="400" height="350">

![Image](https://user-images.githubusercontent.com/65273165/82029743-0b3cc380-96b5-11ea-8a8e-45ad5adbd3e1.jpg)

<img src = "https://user-images.githubusercontent.com/65273165/82031275-43dd9c80-96b7-11ea-8a29-d0a3e15fa5f3.png" width="360" height="350"> 

<img src = "https://user-images.githubusercontent.com/65273165/82030442-16dcba00-96b6-11ea-98e8-409eb40d29c9.jpg" height = "350" width = "360">


<img src = "https://user-images.githubusercontent.com/65273165/82029772-142d9500-96b5-11ea-83ba-1df68244e061.jpg" height= "350" width= "360">


## Contributing
Contributions of all sizes are welcome. 

## Note
Before running the `SpotYT.py` in the terminal you must:

- Assign the `TOKEN` of your Bot editing the `SpotYT.py`.
- Assign the `PASSWORD` for which it will authenticate you.

You are good to go now.
All the Best.


## License
[MIT](https://choosealicense.com/licenses/mit/)



