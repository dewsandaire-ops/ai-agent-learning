import re
import urllib.error
import urllib.parse
import urllib.request


def web_search(query, max_results=5):
    """Search the web and return a small list of results."""

    if not query or not str(query).strip():
        return "Please provide a search query."

    query = str(query).strip()
    max_results = max(1, min(max_results, 5))

    url = (
        "https://html.duckduckgo.com/html/?"
        + urllib.parse.urlencode({"q": query})
    )

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 Chrome/131.0 Safari/537.36"
            )
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            html = response.read().decode(
                "utf-8",
                errors="replace",
            )

    except urllib.error.HTTPError as error:
        return (
            f"Unable to perform web search: "
            f"HTTP error {error.code}."
        )

    except urllib.error.URLError as error:
        return (
            f"Unable to perform web search: "
            f"{error.reason}."
        )

    except TimeoutError:
        return (
            "Unable to perform web search: "
            "the request timed out."
        )

    except Exception as error:  # noqa: BLE001
        return f"Unable to perform web search: {error}"

    results = []

    pattern = re.compile(
        r'<a[^>]+class="result__a"[^>]+href="([^"]+)"'
        r'[^>]*>(.*?)</a>',
        re.IGNORECASE | re.DOTALL,
    )

    for match in pattern.finditer(html):
        link = match.group(1)
        title = re.sub(
            r"<[^>]+>",
            "",
            match.group(2),
        )
        title = re.sub(
            r"\s+",
            " ",
            title,
        ).strip()

        if not title:
            continue

        if link.startswith("//"):
            link = "https:" + link

        results.append(
            {
                "title": title,
                "url": link,
            }
        )

        if len(results) >= max_results:
            break

    if not results:
        return f"No web search results found for: {query}"

    lines = [f"Search results for: {query}"]

    for number, result in enumerate(results, start=1):
        lines.append(
            f"{number}. {result['title']}\n"
            f"   {result['url']}"
        )

    return "\n".join(lines)