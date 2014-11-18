from ..objects import JSONRPCError

INVALID_PARAMS = JSONRPCError(-32602, "Invalid params", data="Invalid method parameter(s).")
