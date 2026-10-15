# Multi-functional AI Investment Assistant — project webpage

One HTML/CSS website, with a small PHP wrapper for WordPress. No frontend framework or JavaScript is required.

## Structure

```text
fyp_website/
├── index.html                 # All page content; edit this file
├── styles.css                 # All page styles; edit this file
├── package_wordpress.py       # Creates the WordPress installation ZIP
├── wordpress/
│   ├── fyp-project-page.php   # PHP shortcode wrapper
│   └── fyp-project-page.zip   # Generated installation package
└── README.md
```

`index.html` and `styles.css` are the single source for the webpage. The ZIP packages that same page for WordPress; it is not a separate implementation.

## Preview and edit

Open `index.html` in a browser. Edit the text in `index.html` and the layout in `styles.css`. Update the footer date when changing the content.

After editing, regenerate the WordPress package:

```sh
python3 package_wordpress.py
```

Python is used only for packaging; the deployed site requires no Python installation.

## Deploy to WordPress

1. Upload `wordpress/fyp-project-page.zip` through **Plugins → Add New → Upload Plugin**, then activate it.
2. Create a page and add a Shortcode block containing `[fyp_project_page]`.
3. Select a full-width page template if available, and preview on desktop and mobile.

This requires permission to install a plugin on the school's WordPress site. The PHP wrapper displays the bundled HTML and loads the scoped stylesheet. Future updates are made in the source files and deployed by replacing the plugin with the regenerated ZIP. The page content is maintained in `index.html` rather than native WordPress text blocks.

The PHP wrapper still needs a runtime check on WordPress. Theme-specific spacing may need adjustment there.

## Content to add later

- Supervisor's name.
- Project-plan PDF: upload it to the WordPress Media Library and replace the `pending-download` span with an anchor pointing to its uploaded URL.
- Measured evaluation results and demonstration video.

The React/Next.js references in the planned-tools table describe the investment-assistant research platform, not this project webpage.
