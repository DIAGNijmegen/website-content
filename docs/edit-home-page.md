# Edit home page

1. Go to website-content/website-{subgroup}
2. Select pelicanconf.py

# Edit text home page

Edit (one of the) following in the subgroup's pelicanconf.py

```
SITENAME = 'Name of the site'
SITENAME_SHORT = 'Short name of the site, visible in mobile mode. Max 5 characters'
SITELEAD = 'General text home page'
HOME_IMAGE_CAPTION = 'Caption under top image home page'
```

# Edit main image home page

### Static home page image

1. Upload an image to website-content/content/images/general/
2. Edit `HOME_IMAGE = 'images/general/<image>.png` in the subgroup's pelicanconf.py

### Dynamic home page image

Write `HOME_IMAGE = 'highlight'` in the subgroup's pelicanconf.py. The home page image will now automatically switch to the last Highlight

# Edit links header and footers

Edit ```FOOTER_TEXT = 'The .... Group is part of the Department of ... at <a href="link">text</a>.'```

The ```TOP_DOMAIN``` and ```PARENT_DOMAIN``` should not be changed
