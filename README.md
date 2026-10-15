# Web Responsive - Dark Glass Theme (Odoo 18)

Optional **Dark Glass** theme for the application menu provided by
[OCA/web_responsive 18.0](https://github.com/OCA/web/tree/18.0/web_responsive).

It extends the existing Odoo `res.users.apps_menu_theme` selection and adds
three theme-specific SCSS assets. The OCA menu, preference modal, search
components, icons, and SVG are **reused**, not copied or replaced.

## Requirements

- Odoo Community 18.0
- OCA `web_responsive` (18.0) installed

## Install

1. Extract the ZIP into an addons directory so the path looks like
   `<addons_path>/web_responsive_dark_glass/__manifest__.py`.
2. Make sure this addons directory is included in Odoo's `addons_path`.
3. Restart Odoo if necessary to make new files available.
4. Enable developer mode, then open **Apps > Update Apps List**.
5. Search for **Web Responsive - Dark Glass Theme**, removing the default
   "Apps" filter if it hides technical addons, and install it.
6. Open **Apps Menu Preferences** (droplet icon in the top bar), choose
   **Theme: Dark Glass**, and save. Close/reopen the app menu or reload Odoo
   if necessary (the OCA preferences action reloads the context).

Each user can select Dark Glass, Community, or Milk independently.
Uninstalling this addon returns users of Dark Glass to the default theme
via Odoo's `ondelete` fallback.

## Technical design

- `models/res_users.py`: adds a single `selection_add` entry for `dark_glass`.
- `static/src/scss/dark_glass.scss`: scoped to
  `.o_grid_apps_menu[data-theme="dark_glass"]`.
- `static/src/scss/command_palette.scss`: applies translucent styling to
  Odoo's Command Palette only while Dark Glass is selected. Uses the
  persistent OCA menu theme attribute with CSS `:has()` because the dialog
  is mounted outside the apps menu. No JavaScript patch is required.
- `static/src/scss/navbar.scss`: gives the top navigation bar a translucent
  Dark Glass background and bottom border **only while the OCA apps menu is
  open** (`body.o_apps_menu_opened`). It restores Odoo's normal navbar when
  viewing an application. No `backdrop-filter` is applied to the navbar:
  that would create a containing block for OCA's fixed-position home menu,
  breaking its full-screen overlay and stacking.
- Uses `/web_responsive/static/src/img/home-menu-bg-overlay.svg` from the
  **installed** `web_responsive` addon, so the SVG is not redistributed.
- Gives app icon backgrounds the same translucent glass surface as the menu search bar, without changing tile layout, icon dimensions, rounded corners, or icon assets.
- Icons with an opaque background baked into the PNG keep that artwork; CSS cannot make those image pixels transparent.
- Does not override the `community` or `milk` themes, and does not patch JS.
- The Command Palette styling also applies when opened with Ctrl+K if the
  current user has selected Dark Glass.
- No changes to OCA source files or Odoo Enterprise assets are required.

To adjust the colors, edit the three CSS colors in `--app-menu-background`.
The radial-gradient values are `#123745`, `#1a142f`, and `#03050d`.

## Troubleshooting

- When upgrading an existing installation, rebuild/deploy the addon and
  upgrade the Odoo module to register the additional backend SCSS assets.
- The Command Palette and navbar themes require a modern browser with CSS
  `:has()` support and the OCA apps menu mounted in the navigation bar.
- The navbar background changes only when OCA adds `o_apps_menu_opened` to
  the `<body>`; normal application views keep Odoo's navbar appearance.

- If Dark Glass is absent from the theme dropdown, update the Apps List and
  verify the addon is installed in the same database as `web_responsive`.
- If you see the new selection but old styling, reload assets (`?debug=assets`
  for development), clear the browser cache, and check the backend assets
  compilation logs. You may need to rebuild your Docker image if addons are
  baked into it at build time.
- If you upgrade OCA/web_responsive, confirm it still provides the same
  `apps_menu_theme` field, DOM classes, and SVG path.

## License and attribution

LGPL-3.0-or-later; see `LICENSE`.

This addon is independent from OCA/web_responsive. It relies on its public
extension points and references the SVG already supplied by OCA's module;
no files from OCA are included in this ZIP. The upstream addon is licensed
LGPL-3.0 and contains third-party copyright notices.

Upstream: https://github.com/OCA/web/tree/18.0/web_responsive
