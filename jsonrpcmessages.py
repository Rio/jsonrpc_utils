# -*- coding: utf-8 -*-
import uuid


class JSONRPCNotification(dict):
    def __init__(self, method, params=None):
        dict.__init__(self)

        self["jsonrpc"] = "2.0"
        self["method"] = method

        if params:
            if not isinstance(params, list) and not isinstance(params, dict):
                raise TypeError("params MUST be a list of dictionary.")

            self["params"] = params
    # end __init__
# end JSONRPCNotification


class JSONRPCRequest(JSONRPCNotification):
    def __init__(self, method, params=None):
        JSONRPCNotification.__init__(self, method, params=params)

        self["id"] = str(uuid.uuid4())
    # end __init__
# end JSONRPCRequest


class JSONRPCResponse(dict):
    def __init__(self, id, result=None, error=None):
        dict.__init__(self)

        self["jsonrpc"] = "2.0"

        self["id"] = id

        if result and not error:
            self["result"] = result

        elif error and not result:
            if not isinstance(error, JSONRPCError):
                raise TypeError("Error object must be of type JSONRPCError.")

            self["error"] = error

        else:
            raise TypeError("Either result or error MUST be given.")
    # end __init__
# end JSONRPCResponse


class JSONRPCError(dict):
    def __init__(self, code, message, data=None):
        dict.__init__(self)

        self["code"] = code
        self["message"] = message

        if data:
            self["data"] = data
    # end __init__
# end JSONRPCError


# Some predefined errors.
PARSE_ERROR = JSONRPCError(-32700, "Parse error", data="Invalid JSON was received by the server. An error occured on the server while parsing the JSON test.")
INVALID_REQUEST = JSONRPCError(-32600, "Invalid Request", data="The JSON sent is not a valid Request object.")
METHOD_NOT_FOUND = JSONRPCError(-32601, "Method not found", data="The method does not exist / is not available.")
INVALID_PARAMS = JSONRPCError(-32602, "Invalid params", data="Invalid method parameter(s).")
INTERNAL_ERROR = JSONRPCError(-32603, "Internal error", data="Internal JSON-RPC error.")
