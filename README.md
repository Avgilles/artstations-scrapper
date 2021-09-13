# ArtStation Scraper

This is my personal project created to download images from [ArtStation](https://www.artstation.com/) website. The program will download artworks from specified artists to specified download directory. In the download directory, the program will create and name subdirectories using the artist IDs, then save artworks to the corresponding subdirectories. For each artwork, the file modification time are set in order from newest to oldest so that you can sort files by modified date. Lastly, when running this program, it will check each artist directory to see if an update is needed such that only new uploads will be downloaded.

## Instructions

1. install [Python 3.6+](https://www.python.org/)

2. install `requests` library

    ```bash
    pip install --user requests
    ```
