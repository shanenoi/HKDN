from . import   Company,\
                get_source,\
                google_search,\
                re


class ReviewCongTy(google_search.GoogleSearch):

    web_url = "https://reviewcongty.com/"

    def search(self, key_word:str):
        super(ReviewCongTy, self).search(
            key_word + f" site:{self.web_url}"
        )

    def get_list_results(self) -> list:
        for url in super(ReviewCongTy, self).get_list_results():
            try:
                yield re.findall(
                    "(https://\w+.\w+/companies/[\w-]+)",
                    url
                )[0]
            except IndexError:
                pass

    @staticmethod
    def get_info(url:str) -> Company:
        source = get_source(url)
        return Company(
            name=re.search('name": *"([^"]+)"', source).groups(0)[0],
            address=re.search('address": *"([^"]+)"', source).groups(0)[0],
            rating=float(re.search('ratingValue": *"([^"]+)"', source).groups(0)[0]),
            rating_count=int(re.search('ratingCount": *"([^"]+)"', source).groups(0)[0])
        )
