# larderia-legal

Public legal pages for [Larderia](https://github.com/irishedev/inventory-app) (privacy policy, etc.).

Hosted on **GitHub Pages** so the app repo can stay private.

## Live URL

After Pages is enabled:

**https://irishedev.github.io/larderia-legal/privacy.html**

Use that URL in App Store Connect, Google Play Console, and the in-app Settings link.

## One-time setup

1. Create a **public** repo named `larderia-legal` on GitHub (under `irishedev`).
2. Push this folder:

   ```bash
   cd larderia-legal
   git init
   git add index.html privacy.html README.md
   git commit -m "Add Larderia privacy policy for GitHub Pages"
   git branch -M main
   git remote add origin https://github.com/irishedev/larderia-legal.git
   git push -u origin main
   ```

3. In the repo: **Settings → Pages →** source **Deploy from branch** → branch `main`, folder **`/ (root)`** → Save.
4. Wait 1–2 minutes and open the live URL in a private browser window.

## Updating the policy

Edit `privacy.html`, bump the “Last updated” date, commit, and push. No app release is required unless the URL changes.
