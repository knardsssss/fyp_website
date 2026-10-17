# Multi-functional AI Investment Assistant — project webpage

A standalone page and a paste-ready WordPress Custom HTML block. All CSS is inline; no plugin, JavaScript, external stylesheet, or WordPress Additional CSS access is needed.

## Files

- `index.html`: source of truth, with content and inline styles. Open it in a browser to preview.
- `package_wordpress.py`: validates and exports the body of the page using Python's standard library.
- `wordpress/custom-html.html`: generated fragment to paste into WordPress. Do not paste the standalone `index.html`, which includes document-level tags.

## Deploy to the school WordPress site

1. Open `wordpress/custom-html.html` in a text editor and copy its entire contents.
2. Edit the destination WordPress page and add a **Custom HTML** block. Replace the old Shortcode block if one was added.
3. Paste the copied HTML into the block. Choose a full-width page template if the theme provides one.
4. Save the page, reload the editor, and preview the saved page on desktop and mobile. Check navigation links and expand/collapse the methods sections.

WordPress permissions can filter inline CSS properties and HTML elements when saving. The school's exact restrictions have not been verified. If the saved layout differs from the local preview, inspect the saved block to see which attributes or elements were removed. A theme's content width and styles can also affect the result; the block cannot change the site's surrounding header or page template. This approach needs the editor to retain the inline styles used by the page.

## Edit and regenerate

Edit the content or `style` attributes directly in `index.html`, then run:

```sh
python3 package_wordpress.py
```

Update the footer date when changing the content. Copy the regenerated `wordpress/custom-html.html` into the same Custom HTML block and save again. Python is used only for exporting, never on WordPress.

The exporter checks for unsupported document tags, missing inline styles, unresolved CSS variables, duplicate IDs, and broken internal navigation/accessibility labels. There is no plugin ZIP or PHP wrapper to install.

## Layout and interaction

Wrapping flex layouts, an auto-fitting card grid, and fluid spacing allow the page to adapt without media queries. Narrow containers stack the cards and columns. Methods use native HTML `details`/`summary` controls and their browser disclosure markers; they require no scripts. The skip link is always visible, and browser keyboard-focus indicators remain available. Decorative CSS connectors and custom hover/open-state effects were removed because inline styles cannot express pseudo-elements, pseudo-classes, or media queries.

## Content to add later

- Project-plan PDF: upload it to the WordPress Media Library and replace the `pending-download` span with an anchor pointing to the uploaded URL, retaining its inline style.
- Measured evaluation results and demonstration video.

The React/Next.js references in the planned-tools table describe the investment-assistant research platform, not this project webpage.
