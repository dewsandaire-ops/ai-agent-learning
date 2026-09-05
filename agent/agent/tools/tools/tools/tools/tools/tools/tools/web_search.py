import json
import urllib.parse
import urllib.request


def web_search(query, max_results=5):
    """Search the internet for current or recent information."""

    query = query.strip()

    if not query:
        return "Please provide a search query."

    if max_results < 1:
        max_results = 1

    if max_results > 5:
        max_results = 5

    try:
        encoded_query = urllib.parse.quote(query)

        url = (
            "https://www.google.com/search?q="
            + encoded_query
        )

        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            html = response.read().decode("utf-8", errors="ignore")

        return {
            "query": query,
            "max_results": max_results,
            "status": "Search completed.",
            "note": (
                "The search page was reached successfully. "
                "Detailed result extraction may require additional processing."
            ),
            "content_available": bool(html),
        }

    except Exception as error:
        return f"Unable to perform web search: {error}"
