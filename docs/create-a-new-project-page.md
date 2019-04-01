# Create a new project page 

1. Create new file on website-content/content/pages/projects/
2. Type project name in entry above and end with .md. Example: website-content/content/pages/projects/project.md
3. Fill the page with the following content;

```
MANDATORY

title: Project title (appears on top of page)
title_long: Project title (main caption)
finished: false (change to 'true' to move the project from Current projects to Finished Projects)
picture: {filename}.png (This picture appears on the project home page and is collected from website-content/content/images/projects/. Upload a square and resized image there and keep into account with selecting your image that mostly the top part is showing)
template: project-single
groups: pathology/diag/rse/retina, etc (this tag determines on which websites the project will be shown. Adding diag is not mandatory)
people: names of people involved in the project. (This will cause the project to appear on their personal pages. It is possible to add external people here. If you want their pictures to appear as well, upload a square and resized image to website-content/content/images/people/ with file name: firstname_lastname
description: a short description of +/- 135 characters. This will appear on the project home page.
bibkeys: bibkeys of publications that are connected to the project

FREE TEXT, FOR EXAMPLE:

#Background

{short background on project}

#Aim
{aim of project}

#Funding
{funding + links}

```

4. To add an image to the text, upload a resized image to website-content/content/images/projects/ and type `![link name image]({filename}/images/projects/{filename}.png)`. The first {filename} is text, don't type the actual filename there. 

5. A preview van be viewed by selecting 'Preview' on the top of the edit page. 

6. Commit changes at bottom of the page.
