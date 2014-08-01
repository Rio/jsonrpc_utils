from jsonrpc_utils.objects.error import JSONRPCError


# Some predefined error objects.
PARSE_ERROR = JSONRPCError(-32700, "Parse error", data="Invalid JSON was received by the server. An error occured on the server while parsing the JSON test.")
INVALID_REQUEST = JSONRPCError(-32600, "Invalid Request", data="The JSON sent is not a valid Request object.")
METHOD_NOT_FOUND = JSONRPCError(-32601, "Method not found", data="The method does not exist / is not available.")
INVALID_PARAMS = JSONRPCError(-32602, "Invalid params", data="Invalid method parameter(s).")
INTERNAL_ERROR = JSONRPCError(-32603, "Internal error", data="Internal JSON-RPC error.")
