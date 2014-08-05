import json


class JSONRPCBase(dict):
    def serialize(self):
        return json.dumps(self)
    # end serialize

    @classmethod
    def from_dict(cls, jsonrpc_dict):
        if "jsonrpc" in jsonrpc_dict:
            jsonrpc_dict.pop("jsonrpc")

        if not isinstance(jsonrpc_dict, dict):
            raise ValueError("Data should be type dict.")

        return cls(**jsonrpc_dict)
    # end from_dict
# end JSONRPCBase
