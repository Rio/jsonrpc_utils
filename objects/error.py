class JSONRPCError(dict):
    def __init__(self, code, message, data=None):
        dict.__init__(self)

        self["code"] = code
        self["message"] = message

        if data:
            self["data"] = data
    # end __init__
# end JSONRPCError
