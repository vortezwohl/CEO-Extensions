from ceo import ability
from duckduckgo_search import DDGS

ddgs = DDGS()


@ability
def search_on_duckduckgo(keywords: list[str], max_results_for_each_keywords: int = 3) -> dict:
    # search on duckduckgo if you don't know clearly about something
    # you can search several keywords at the same time with `search_on_duckduckgo`
    results = dict()
    for kw in keywords:
        search_results = ddgs.text(
            keywords=kw,
            region='wt-wt',
            safesearch='off',
            timelimit=None,
            backend='auto',
            max_results=max_results_for_each_keywords
        )
        for _res in search_results:
            _title = _res.get('title', 'unknown')
            _res.pop('title')
            _link = _res.get('href', 'unknown')
            _res.pop('href')
            _res['source'] = f'({_title})[{_link}]'
            _content = _res.get('body')
            _res.pop('body')
            _res['content'] = _content
        results[f'search results for "{kw}"'] = search_results
    return results
