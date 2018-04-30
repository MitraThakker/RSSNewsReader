class FeedResponse:

	def __init__(self, title="", entries=list(), error=None):
		self.title = title
		self.entries = entries
		self.error = error


class FeedResponseException(Exception):
	pass
