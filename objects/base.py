import json


class JSONRPCBase(dict):
    def serialize(self):
        return json.dumps(self)
    # end serialize
# end JSONRPCBase
