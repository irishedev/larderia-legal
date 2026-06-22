# larderia-legal

Public legal pages for [Larderia](https://github.com/irishedev/inventory-app) (privacy policy, account deletion).

Hosted on **GitHub Pages** so the app repo can stay private.

## Live URLs

Canonical English (use in App Store Connect / Google Play Console):

- **Privacy:** https://irishedev.github.io/larderia-legal/privacy.html
- **Account deletion:** https://irishedev.github.io/larderia-legal/delete-account.html

Localized pages (linked from the in-app Settings footer by device/app language):

| Locale | Privacy | Account deletion |
|--------|---------|------------------|
| English | `privacy.html` | `delete-account.html` |
| Deutsch | `privacy-de.html` | `delete-account-de.html` |
| Español | `privacy-es.html` | `delete-account-es.html` |
| Français | `privacy-fr.html` | `delete-account-fr.html` |
| 日本語 | `privacy-ja.html` | `delete-account-ja.html` |
| 한국어 | `privacy-ko.html` | `delete-account-ko.html` |
| Português | `privacy-pt.html` | `delete-account-pt.html` |
| 简体中文 | `privacy-zh.html` | `delete-account-zh.html` |
| 繁體中文 | `privacy-zh-Hant.html` | `delete-account-zh-Hant.html` |

Each page includes a language switcher linking all versions.

## Updating content

1. Edit translations in `legal_content.py` (or English sections only if a single-locale fix).
2. Regenerate HTML:

   ```bash
   python3 generate_pages.py
   ```

3. Commit and push. No app release is required unless URL paths change.

The app resolves locale-specific URLs in `inventory-app/lib/core/constants/app_urls.dart`.

## One-time setup

1. Create a **public** repo named `larderia-legal` on GitHub (under `irishedev`).
2. Push this folder.
3. In the repo: **Settings → Pages →** source **Deploy from branch** → branch `main`, folder **`/ (root)`** → Save.
4. Wait 1–2 minutes and open the live URL in a private browser window.
