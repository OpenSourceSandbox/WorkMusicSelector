# 🎵 노동요 추천 봇

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python version](https://img.shields.io/badge/python-3.8-blue)

**노동요 추천 봇**은 여러분의 업무를 활기차게 만들어줄 오픈소스 프로젝트입니다. 이 봇은 지정된 키워드에 따라 YouTube에서 랜덤한 노래를 가져와서 매일 Slack 채널에 게시합니다. 이 사랑스러운 작은 봇으로 업무 환경을 향상시켜 보세요!

## 목차
1. [특징](#특징)
2. [설치](#설치)
3. [사용 방법](#사용-방법)
4. [기여](#기여)
5. [라이센스](#라이센스)

## 특징
* 사전 정의된 키워드에 따라 YouTube에서 랜덤한 노래를 가져옵니다
* 더 많은 랜덤 결과를 위해 페이지를 자동으로 스크롤합니다
* 원하는 Slack 채널에 노래를 게시합니다
* 강력한 예외 처리로 무한정 실행할 수 있습니다

## 설치
이 프로젝트를 사용하려면 컴퓨터에 [Python](https://www.python.org/downloads/)과 [pip](https://pip.pypa.io/en/stable/installation/)이 설치되어 있어야 합니다. 커맨드 라인에서 다음을 입력하세요:

```bash
# 이 저장소를 복제합니다
$ git clone https://github.com/OpenSourceSandbox/WorkMusicSelector

# 저장소로 이동합니다
$ cd WorkMusicSelector

# 의존성을 설치합니다
$ pip install -r requirements.txt
```

## 사용 방법

```bash
# 봇을 실행합니다
$ python main.py
```
스크립트에서 `SLACK_TOKEN`과 `SLACK_CHANNEL`을 여러분의 Slack 토큰과 게시하려는 Slack 채널로 바꿉니다. 또한 노래 검색을 위한 키워드도 변경할 수 있습니다. 기본 설정은 한국어이지만, 여러분의 선호에 따라 커스터마이징할 수 있습니다.

## 기여
우리는 항상 기여를 환영하고 장려합니다. 기여하기 전에 우리의 기여 가이드라인과 행동 규칙을 읽어보세요.

## 라이센스
이 프로젝트는 MIT 라이센스에 따라 라이선스가 부여됩니다 - 자세한 내용은 [LICENSE.md](LICENSE.md) 파일을 참조하세요.

음악 추천 봇으로 업무를 더 즐겁게 만드세요! 🎵🙉

---

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
