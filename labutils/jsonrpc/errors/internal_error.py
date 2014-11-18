from ..objects import JSONRPCError

INTERNAL_ERROR = JSONRPCError(-32603, "Internal error", data="Internal JSON-RPC error.")
