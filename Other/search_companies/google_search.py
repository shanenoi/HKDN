from . import   get_source,\
                re,\
                urllib


class GoogleSearch(object):

    def __init__(self):
        self.url = "https://www.google.com/search?q={}"
        self.content = ""


    def search(self, key_word:str) -> None:
        self.content = get_source(
            url=self.url.format(urllib.parse.quote(key_word)),
        )

    def get_list_results(self) -> list:
        return re.findall(
            'href="/url\?q=(http[^"]+)&amp[^"]+&amp[^"]+&amp[^"]+"',
            self.content
        )
