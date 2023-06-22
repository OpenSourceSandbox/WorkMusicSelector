import sys

from driver import WebDriverManager
from song_recommendation import SongRecommendation

if __name__ == "__main__":
    while True:
        try:
            driver_manager = WebDriverManager()
            song_rec = SongRecommendation("h3 > a#video-title",
                                          "SLACK_TOKEN",    # 자신의 슬랙 토큰
                                          "SLACK_CHANNEL",  # 알림을 보내고 싶은 슬랙 체널 EX) #일반
                                          driver_manager)
            song_rec.recommend_song()
            break
        except Exception as e:
            # print(e)
            continue
