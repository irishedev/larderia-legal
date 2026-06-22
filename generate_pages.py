#!/usr/bin/env python3
"""Generate localized privacy and account-deletion HTML pages."""

from __future__ import annotations

from pathlib import Path

from legal_content import DELETE_ACCOUNT_PAGES, PRIVACY_PAGES

ROOT = Path(__file__).resolve().parent

LOCALES: list[tuple[str, str, str]] = [
    ("", "en", "English"),
    ("-de", "de", "Deutsch"),
    ("-es", "es", "Español"),
    ("-fr", "fr", "Français"),
    ("-ja", "ja", "日本語"),
    ("-ko", "ko", "한국어"),
    ("-pt", "pt", "Português"),
    ("-zh", "zh", "简体中文"),
    ("-zh-Hant", "zh-Hant", "繁體中文"),
]

PRIVACY_STYLES = """
    :root {
      color-scheme: light dark;
      --bg: #f9f6f1;
      --text: #221e1a;
      --muted: #5c554d;
      --accent: #3d6b4f;
      --card: #ffffff;
      --border: #e8e2d9;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --bg: #221e1a;
        --text: #f9f6f1;
        --muted: #b8afa3;
        --accent: #7fb896;
        --card: #2c2722;
        --border: #3d3832;
      }
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.6;
      background: var(--bg);
      color: var(--text);
    }
    main {
      max-width: 42rem;
      margin: 0 auto;
      padding: 2rem 1.25rem 3rem;
    }
    h1 {
      font-size: 1.75rem;
      margin: 0 0 0.25rem;
      letter-spacing: -0.02em;
    }
    .updated {
      color: var(--muted);
      font-size: 0.95rem;
      margin-bottom: 1.25rem;
    }
    .lang-switch {
      display: flex;
      flex-wrap: wrap;
      gap: 0.35rem 0.65rem;
      margin-bottom: 1.75rem;
      font-size: 0.85rem;
    }
    .lang-switch a {
      color: var(--muted);
      text-decoration: none;
    }
    .lang-switch a:hover { color: var(--accent); text-decoration: underline; }
    .lang-switch a[aria-current="page"] {
      color: var(--accent);
      font-weight: 600;
      text-decoration: none;
    }
    section {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.25rem 1.35rem;
      margin-bottom: 1rem;
    }
    h2 {
      font-size: 1.05rem;
      margin: 0 0 0.65rem;
      color: var(--accent);
    }
    p, ul, ol { margin: 0 0 0.75rem; }
    ul, ol { padding-left: 1.25rem; }
    li { margin-bottom: 0.35rem; }
    a { color: var(--accent); }
    p:last-child, ul:last-child, ol:last-child { margin-bottom: 0; }
"""

DELETE_ACCOUNT_EXTRA_STYLES = """
    .cta {
      display: inline-block;
      margin-top: 0.25rem;
      padding: 0.55rem 1rem;
      border-radius: 8px;
      background: var(--accent);
      color: var(--bg);
      text-decoration: none;
      font-weight: 600;
    }
"""


def _privacy_filename(suffix: str) -> str:
    return f"privacy{suffix}.html"


def _delete_filename(suffix: str) -> str:
    return f"delete-account{suffix}.html"


def _lang_nav(page: str, current_suffix: str, labels: dict[str, str]) -> str:
    links: list[str] = []
    for suffix, code, _label in LOCALES:
        filename = (
            _privacy_filename(suffix) if page == "privacy" else _delete_filename(suffix)
        )
        label = labels[code]
        if suffix == current_suffix:
            links.append(f'<a href="{filename}" hreflang="{code}" aria-current="page">{label}</a>')
        else:
            links.append(f'<a href="{filename}" hreflang="{code}">{label}</a>')
    return (
        '<nav class="lang-switch" aria-label="Languages">\n      '
        + "\n      ".join(links)
        + "\n    </nav>"
    )


def _render_blocks(blocks: list[dict]) -> str:
    parts: list[str] = []
    for block in blocks:
        kind = block["type"]
        if kind == "p":
            parts.append(block["html"])
        elif kind == "ul":
            items = "".join(f"<li>{item}</li>" for item in block["items"])
            parts.append(f"<ul>{items}</ul>")
        elif kind == "ol":
            items = "".join(f"<li>{item}</li>" for item in block["items"])
            parts.append(f"<ol>{items}</ol>")
        else:
            raise ValueError(f"unknown block type: {kind}")
    return "\n      ".join(parts)


def _render_page(
    *,
    page: dict,
    styles: str,
    lang_nav: str,
    privacy_url: str,
    delete_account_url: str,
) -> str:
    sections_html: list[str] = []
    for section in page["sections"]:
        body = _render_blocks(section["blocks"])
        for key, value in (
            ("{privacy_url}", privacy_url),
            ("{delete_account_url}", delete_account_url),
        ):
            body = body.replace(key, value)
        sections_html.append(
            f"""    <section>
      <h2>{section["heading"]}</h2>
      {body}
    </section>"""
        )

    return f"""<!DOCTYPE html>
<html lang="{page["html_lang"]}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{page["title"]}</title>
  <style>{styles}
  </style>
</head>
<body>
  <main>
    <h1>{page["title"]}</h1>
    <p class="updated">{page["updated"]}</p>
    {lang_nav}

{chr(10).join(sections_html)}
  </main>
</body>
</html>
"""


def generate() -> None:
    labels = {code: label for _suffix, code, label in LOCALES}
    for suffix, code, _label in LOCALES:
        privacy_url = _privacy_filename(suffix)
        delete_url = _delete_filename(suffix)
        privacy = PRIVACY_PAGES[code]
        delete_page = DELETE_ACCOUNT_PAGES[code]

        privacy_html = _render_page(
            page=privacy,
            styles=PRIVACY_STYLES,
            lang_nav=_lang_nav("privacy", suffix, labels),
            privacy_url=privacy_url,
            delete_account_url=delete_url,
        )
        delete_html = _render_page(
            page=delete_page,
            styles=PRIVACY_STYLES + DELETE_ACCOUNT_EXTRA_STYLES,
            lang_nav=_lang_nav("delete", suffix, labels),
            privacy_url=privacy_url,
            delete_account_url=delete_url,
        )

        privacy_path = ROOT / privacy_url
        delete_path = ROOT / delete_url
        privacy_path.write_text(privacy_html, encoding="utf-8")
        delete_path.write_text(delete_html, encoding="utf-8")
        print(f"wrote {privacy_path.name}, {delete_path.name}")


if __name__ == "__main__":
    generate()
