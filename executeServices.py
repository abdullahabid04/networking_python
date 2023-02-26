import requests

from ServiceRequirements import services
from services import find_station_id_by_name


def execute_service(separated):
    url = services[str(separated[0])]["url"]
    method = services[str(separated[0])]["method"]
    parameters = services[str(separated[0])]["parameters"]

    sid = find_station_id_by_name(separated[1])

    get_keys = parameters.keys()
    keys = [*get_keys]

    values = [sid, *separated[2:]]

    for i in range(len(keys)):
        parameters[keys[i]] = values[i]

    try:
        req = None
        if method == "post":
            req = requests.post(url, parameters)
        if method == "get":
            req = requests.get(url.format(*values))

        if req is not None:
            return req.text

    except Exception as e:
        pass
