from ceo import ability
from duckduckgo_search import DDGS

ddgs = DDGS()


@ability
def search_on_duckduckgo(keywords: list[str], max_results_for_each_keywords: int = 3) -> dict:
    # search on duckduckgo if you don't know clearly about something
    # you can search several keywords at the same time with `search_on_duckduckgo`
    results = dict()
    for kw in keywords:
        results[f'search for "{kw}"'] = ddgs.text(
            keywords=kw,
            region='wt-wt',
            safesearch='off',
            timelimit=None,
            backend='auto',
            max_results=max_results_for_each_keywords
        )
    return results
