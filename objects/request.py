import uuid

from .notification import JSONRPCNotification


class JSONRPCRequest(JSONRPCNotification):
    def __init__(self, method, params=None):
        JSONRPCNotification.__init__(self, method, params=params)

        self["id"] = str(uuid.uuid4())
    # end __init__
# end JSONRPCRequest
