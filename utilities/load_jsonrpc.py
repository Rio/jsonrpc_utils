import json

from jsonrpc_utils.objects import JSONRPCRequest, JSONRPCResponse, JSONRPCNotification

def load_jsonrpc(json_string):
    result_dict = json.loads(json_string)

    jsonrpc_object = jsonrpc_from_dict(result_dict)

    return jsonrpc_object
# end load_jsonrpc

def jsonrpc_from_dict(jsonrpc_dictionary):
    dict_keys = jsonrpc_dictionary.keys()

    if not "jsonrpc" in dict_keys:
        raise ValueError("Invalid JSON-RPC message.")

    if jsonrpc_dictionary["jsonrpc"] != "2.0":
        raise ValueError("Invalid JSON-RPC message.")

    if "method" in dict_keys and "id" in dict_keys:
        return JSONRPCRequest.from_dict(jsonrpc_dictionary)

    elif "method" in dict_keys and "id" not in dict_keys:
        return JSONRPCNotification.from_dict(jsonrpc_dictionary)

    elif "result" in dict_keys or "error" in dict_keys and "id" in dict_keys:
        return JSONRPCResponse.from_dict(jsonrpc_dictionary)

    else:
        raise ValueError("Invalid JSON-RPC message.")
# end jsonrpc_from_dict
