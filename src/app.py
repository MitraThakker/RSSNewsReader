from flask import Flask, render_template, request
from src.app_utils import build_feed_response
from src.vo.feed_response import FeedResponse, FeedResponseException

# Initializing app here
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def fetch_rss_feeds():
	"""
	This URL renders the HTML template using the Jinja2 templating library.
	:return:
	"""
	rss_feed_data = FeedResponse()  # Initialized as an empty dictionary
	if request.method == "POST":  # In case of a POST request when user provides RSS URL
		try:
			rss_feed_data = build_feed_response(request.form["sourceURL"])
			if len(rss_feed_data.entries) == 0:
				raise FeedResponseException
		except FeedResponseException or AttributeError:
			rss_feed_data.error = "No feed data found. Check the URL and try again later."
	return render_template("index.html", rss_feed=rss_feed_data)


if __name__ == "__main__":
	"""I'm aware of the fact that app.run() isn't meant for use in production.
	This code is meant for local dev-testing only.
	I'm using app.run() here because I don't have any recent experience with cloud deployments."""
	app.run(host="localhost", port=5000, debug=True)
