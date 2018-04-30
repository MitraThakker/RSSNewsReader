from feedparser import parse
from src.vo.feed_response import FeedResponse, FeedResponseException


def get_feed_from_source(source: str):
	try:
		return parse(source)
	except Exception as e:
		raise e


def build_feed_response(source: str):
	try:
		feed_data = get_feed_from_source(source=source)
		feed_response_data = FeedResponse(title=feed_data.feed.title, entries=feed_data.entries)
		return feed_response_data
	except AttributeError:
		return FeedResponse(title="", entries=list(), error="No feed data found. Check the URL and try again later.")


if __name__ == "__main__":
	print(get_feed_from_source("http://feeds.bbci.co.uk/news/rss.xml"))
