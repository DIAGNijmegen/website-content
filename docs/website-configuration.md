# Website configuration

Using `pelicanconf.py` you can set site-wide settings that control the build of the website. Most of the settings are self-explanatory (like `FOOTER_TEXT`), others are described here.

## Setting navigation

The menu items (top navigation) can be controlled using the `NAV_SECTIONS` setting.

```python
NAV_SECTIONS = [
    {"name": "Highlights", "url": "highlights", "icon": "megaphone"},

    # Use "hidden" to only show a icon until a user hovers. The value of "hidden" controls the
    # slide-in animation and aproximates the length of the label and can be one of [90, 85, 60]
    {"name": "Publications", "url": "publications", "icon": "file-text-o", "hidden": 85},
]
```

## Layout of the home page

Content on the home page can be configured using `HOME_SECTIONS`. All the available sections are shown below:

```python
HOME_SECTIONS = {
    "Highlights": 'Highlights', 
    "Vacancies": "Vacancies", 
    "Projects": "Projects", 
    "Members": 'Members",
    "PageCards": "",
}
```

Using the value of each dictionary item, the title of the section can be set.

## Enable PDF form for publications

Set `ENABLE_PUBLICATION_PDF_REQUEST` to `True` to enable a form on each publication page to request a pdf.

## Breadcrumbs

To enable or disable breadcrumbs on each page, you can set the `ENABLE_BREADCRUMBS` tag:

```python
# Whether to show breadcrumbs on the page
ENABLE_BREADCRUMBS = True
```

## Card layout

The website uses cards for showing projects, software, etc. Some layout properties can be changed:

```python
# Add the following to the config to disable gradients on the card images.
SHOW_CARD_GRADIENT = False
```