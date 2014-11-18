from ..objects import JSONRPCError

PARSE_ERROR = JSONRPCError(-32700, "Parse error", data="Invalid JSON was received by the server. An error occured on the server while parsing the JSON text.")
