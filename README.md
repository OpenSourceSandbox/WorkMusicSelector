# 🎵 Song Recommendation Bot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python version](https://img.shields.io/badge/python-3.8-blue)

**Song Recommendation Bot** is an open-source project designed to cheer up your day at work. This bot fetches a random song from YouTube based on certain keywords and posts it on your Slack channel daily. Improve your work environment with our lovely little bot!

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contribution](#contribution)
5. [License](#license)

## Features
* Fetches a random song from YouTube based on predefined keywords
* Automatically scrolls the page for more random results
* Posts the song on your desired Slack channel
* Can run indefinitely with robust exception handling

## Installation
To use this project, you'll need [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/OpenSourceSandbox/WorkMusicSelector

# Go into the repository
$ cd WorkMusicSelector

# Install dependencies
$ pip install -r requirements.txt
```


## Usage

```bash
# Run the bot
$ python main.py
```
In the script, replace `SLACK_TOKEN` and `SLACK_CHANNEL` with your Slack token and the Slack channel you wish to post in. You can also change the keyword for song searching. By default, it's in Korean, but you can customize it as per your preference.

## Contribution
We always welcome and encourage contributions. Please read our contribution guidelines and code of conduct before you start to contribute.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. 

Make your work more enjoyable with our Song Recommendation Bot! 🎵🙉
