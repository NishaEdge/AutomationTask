import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_youtube_links(playwright: Playwright) -> None:
    keyword = "environment"
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.youtube.com/")
    page.get_by_placeholder("Search").click()
    page.get_by_placeholder("Search").fill(keyword)
    page.get_by_placeholder("Search").press("Enter")
    time.sleep(2)
    video_links = page.locator("a#video-title").all()
    assert len(video_links) >= 10
    links = []
    for i in range(10):
        video = video_links[i]
        title = video.get_attribute("title")
        if keyword.lower() in title.lower():
            links.append("https://www.youtube.com/" + video.get_attribute("href"))

    for i in range(0, len(links)):
        print(links[i])

    context.close()
    browser.close()
