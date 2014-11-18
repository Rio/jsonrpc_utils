import sys

# do a check of what version of python is running and exchange str type for unicode
if sys.version_info[0] == 2:
    str = unicode

import json

from ..objects import JSONRPCRequest, JSONRPCResponse, JSONRPCNotification
from ..errors import PARSE_ERROR, INVALID_REQUEST

def loads(json_string):
    try:
        result_dict = json.loads(json_string)
        jsonrpc_object = jsonrpc_from_dict(result_dict)

    except ValueError:
        jsonrpc_object = PARSE_ERROR

    except TypeError:
        jsonrpc_object = INVALID_REQUEST

    return jsonrpc_object
# end loads

def jsonrpc_from_dict(jsonrpc_dictionary):
    dict_keys = jsonrpc_dictionary.keys()

    if not "jsonrpc" in dict_keys:
        raise ValueError("jsonrpc field is missing.")

    if jsonrpc_dictionary["jsonrpc"] != "2.0":
        raise ValueError("jsonrpc field is not 2.0.")

    if "method" in dict_keys:
        if not isinstance(jsonrpc_dictionary["method"], str):
            raise TypeError("method field is not of type string.")

        if "id" in dict_keys:
            return JSONRPCRequest.from_dict(jsonrpc_dictionary)

        else:
            return JSONRPCNotification.from_dict(jsonrpc_dictionary)

    elif "result" in dict_keys or "error" in dict_keys and "id" in dict_keys:
        return JSONRPCResponse.from_dict(jsonrpc_dictionary)

    else:
        raise ValueError("No fitting JSON-RPC object found for keys: {0}.".format(dict_keys))
# end jsonrpc_from_dict
