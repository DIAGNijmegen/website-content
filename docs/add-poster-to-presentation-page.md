# Add a new poster to the presentation page

1. Create a new file in website-content/content/pages/presentations/
2. Type the name of the page in the empty entry on the top, and end with .md. Example:  website-content/content/pages/presentations/unsupervised-prostate-cancer-detection.md
3. Fill in the following:
```
ALL MANDATORY 

title: Title poster
template: presentation-single
picture_overview: posters/filename.png (Small image for presentation home page. Collected from https://github.com/DIAGNijmegen/website-content/tree/master/content/images/posters. Upload a resized image here)
picture_large: posters/filename.png (Higher resolution image, collected from Collected from https://github.com/DIAGNijmegen/website-content/tree/master/content/images/posters. Upload a resized image here)
arxiv: ArXiv link if possible
author_list: First and last names of people involved
groups: pathology/diag/rse/retina (determines on which website the poster shoud appear)

{text describing the poster}
```

4. Commit changes at bottom of the page to save.
