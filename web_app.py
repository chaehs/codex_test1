"""A tiny built-in Python web app example."""

from datetime import datetime, UTC
from html import escape
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server


def app(environ, start_response):
    """WSGI app that renders a simple greeting page."""
    query = parse_qs(environ.get("QUERY_STRING", ""))
    name = query.get("name", ["world"])[0]
    safe_name = escape(name)
    now = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")

    html = f"""<!doctype html>
<html lang=\"ko\">
  <head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>간단 웹 앱</title>
    <style>
      body {{ font-family: sans-serif; margin: 2rem; line-height: 1.5; }}
      .card {{ max-width: 520px; border: 1px solid #ddd; border-radius: 12px; padding: 1rem 1.25rem; }}
      code {{ background: #f4f4f4; padding: 0.1rem 0.35rem; border-radius: 6px; }}
    </style>
  </head>
  <body>
    <div class=\"card\">
      <h1>안녕하세요, {safe_name}님 👋</h1>
      <p>이 페이지는 Python 내장 서버로 띄운 아주 작은 웹 예제입니다.</p>
      <p>현재 시각: <strong>{now}</strong></p>
      <p>이름 바꾸기 예시: <code>http://127.0.0.1:8000/?name=Codex</code></p>
    </div>
  </body>
</html>
"""

    data = html.encode("utf-8")
    headers = [
        ("Content-Type", "text/html; charset=utf-8"),
        ("Content-Length", str(len(data))),
    ]
    start_response("200 OK", headers)
    return [data]


def main() -> None:
    """Run the local development server."""
    host, port = "127.0.0.1", 8000
    print(f"Serving on http://{host}:{port}")
    with make_server(host, port, app) as server:
        server.serve_forever()


if __name__ == "__main__":
    main()
