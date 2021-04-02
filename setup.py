
def test_setup():
    try:
        import google_play_scraper
        import openpyxl
        import tkinter
        #from google_play_scraper.scraper import PlayStoreScraper

        #print("Import Successful")
    except ImportError:
        try:
            from pip import main as pipmain
        except ImportError:
            from pip._internal import main as pipmain

        pipmain(["install", "google_play_scraper"])
        pipmain(["install", "openpyxl"])
        pipmain(["install", "tkinter"])
        #pipmain(["install", "google-play-scraper-dmi"])
        #print("Import Unsuccessful")
