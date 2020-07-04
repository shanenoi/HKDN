import re
import requests
import urllib


def get_source(url:str, method:str='get', data:dict=None) -> str:
    func = {
        "get":    requests.get,
        "post":   requests.post,
        "put":    requests.put,
        "delete": requests.delete,
        "head":   requests.head,
        "patch":  requests.patch
    }
    return func[method](url, data=data).text


class Company(object):

    def __init__(
        self, name:str,
        address:str,
        rating:float,
        rating_count:int
    ):
        self.name = name
        self.address = address
        self.rating = rating
        self.rating_count = rating_count
