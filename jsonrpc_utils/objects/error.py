from .base import JSONRPCBase


class JSONRPCError(JSONRPCBase):
    def __init__(self, code, message, data=None):
        JSONRPCBase.__init__(self)

        self["code"] = code
        self["message"] = message

        if data:
            self["data"] = data
    # end __init__
# end JSONRPCError
