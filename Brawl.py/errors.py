class BrawlException(Exception):
    """The base Exception. Should catch everything, ideally."""

    def __init__(self, stat, reason):
        self.stat = str(stat)
        self.reason = reason
        print(stat + " : " + reason)


class Unauthorized(BrawlException):
    """Fires if a request was not sent in the correct format, i.e not using HTTPS."""
    pass


class NotFound(BrawlException):
    """Fires if something isn't found in Brawlhalla's database."""
    pass


class Forbidden(BrawlException):
    """Fires if you don't have a working API key."""
    pass


class BadRequest(BrawlException):
    """Fires if you're missing parameters or a param is not a valid parameter."""
    pass


class RateLimited(BrawlException):
    """Fires if you hit the ratelimit."""
    pass


class Unavailable(BrawlException):
    """Fires if the Brawlhalla servers are down."""
    pass
