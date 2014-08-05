from jsonrpc_utils.objects import JSONRPCError

INVALID_REQUEST = JSONRPCError(-32600, "Invalid Request", data="The JSON sent is not a valid Request object.")
