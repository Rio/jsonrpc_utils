from .base import JSONRPCBase


class JSONRPCNotification(JSONRPCBase):
    def __init__(self, method, params=None):
        JSONRPCBase.__init__(self)

        self["jsonrpc"] = "2.0"
        self["method"] = method

        if params:
            if not isinstance(params, list) and not isinstance(params, dict):
                raise TypeError("params MUST be a list of dictionary.")

            self["params"] = params
    # end __init__
# end JSONRPCNotification
