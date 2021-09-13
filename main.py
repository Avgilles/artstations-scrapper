from argparse import ArgumentParser
import sys, os, time
from lib.artstation import ArtStationAPI
from lib.config import Config
from lib import utils
import schedule

def download_artists(api):
    start_time = time.time()
    result = api.save_artists_json("gillesavraam")
    duration = time.time() - start_time

    # print("--------------all---------------")
    # print(result)
    # print("--------------all---------------")
    print(f"scrap terminé en :\t{duration:.4f} seconds")


def main():
    api = ArtStationAPI()

    if len(sys.argv) == 1 or args.run:
        download_artists(api)


if __name__ == "__main__":
    # main()
    schedule.every(1).hour.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
