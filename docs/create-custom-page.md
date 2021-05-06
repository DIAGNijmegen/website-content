Custom pages are 'stand alone' pages such as https://www.diagnijmegen.nl/doing-a-phd-at-diag/

Custom pages can be made by (1) overwriting a default page, or (2) by creating an independent page

### 1. Overwriting a default page:
Place a .md file inside the website folder. For DIAG this is https://github.com/DIAGNijmegen/website-content/tree/master/website-diag/content. The md file should have the same name as the corresponding default page.  Each page should have at least a `title` tag at the top of the md file. 


### 2. Creating an independent page
An independent page is created via 2 steps:

  - step 1: create a new template .html file. This new template should be placed within the website templates folder. For DIAG this would be https://github.com/DIAGNijmegen/website-content/tree/master/website-diag/content/templates. If the template folder does not exists yet, please create the folder.
    In this template you cannot use the page. attribute (e.g page.title will not work). 

  - step 2: add the following to pelicanconf.py in the website folder
    ```
    ARTICLE_EXCLUDES = ['templates']
    TEMPLATE_PAGES = {
        'templates/my_custom_page.html': 'my_custom_page.html',
    }
    ```
    if ARTICLE_EXCLUDES, TEMPLATE_PAGES already exists in pelicanconf.py, you only need to add your new custom page to TEMPLATE_PAGES dictionary

