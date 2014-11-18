from ..objects import JSONRPCError

METHOD_NOT_FOUND = JSONRPCError(-32601, "Method not found", data="The method does not exist / is not available.")
