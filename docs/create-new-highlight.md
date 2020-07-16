# Create new highlight

1. Create new file in website-content/content/pages/highlights/
2. Type name of page in empty entry on top and end with .md. Example: ```website-content/content/pages/highlights/new-highlight.md```
3. Fill with the following:
```
title: Title of highlight
date: date highlight published (YYYY-MM-DD)
picture: news/<image>.png (Image is collected from website-content/content/images/news/. Image should be landscape, ratio 2:1, minimum width 480 px)
groups: diag/retina/pathology, etc. This determines on which website the highlight will appear. Groups are divided by commas.

{Text Highlight}
```
4. To add an image to the text, upload an image of choice to website-content/content/images/projects/ and type `![name of image link]({{ IMGURL }}/images/projects/<image>.png)`. The first `{{ IMGURL }}` is text, don't type the actual filename there. `IMGURL` makes sure the image is always loaded from the correct domain (in case of using a CDN).

5. Commit changes at bottom of the page to submit.
