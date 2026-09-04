from ddgs import DDGS


def web_search(query, max_results=5):
    try:
        results = DDGS().text(
            query,
            max_results=max_results
        )

        if not results:
            return "No search results were found."

        output = []

        for result in results:
            title = result.get("title", "No title")
            url = result.get("href", "")
            snippet = result.get("body", "")

            output.append(
                f"Title: {title}\n"
                f"URL: {url}\n"
                f"Summary: {snippet}"
            )

        return "\n\n".join(output)

    except Exception as error:
        return f"Web search error: {error}"