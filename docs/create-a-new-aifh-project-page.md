# Create a new AI for Health student project page

1. Sign in to your GitHub account

2. Create a Fork of the website-content repository: ```https://github.com/DIAGNijmegen/website-content```

3. Create new file on ```website-content/content/pages/projects/```

4. Type project name in entry above and end with .md. Example: ```website-content/content/pages/projects/project.md```

5. Fill the page with the following content:

```
MODIFY ALL INFORMATION GIVEN IN CURLY BRACKETS 

title: {PROJECT TITLE} (Appears on top of page)
groups: ai-for-health
finished: false 
type: student
picture: {projects/<image>.png} (This picture appears on the the card shown on the project home page and is collected from website-content/content/images/. Image should be landscape, ratio 2:1, minimum width 480 px)
template: project-single
people: {NAMES OF PEOPLE INVOLVED IN THE PROJECT} (Example: John Smith, Jane Doe) 
description: {A SHORT DESCRIPTION OF +/- 135 CHARACTERS} (This will appear on the card shown on the projects home page)


** Start date: {DD-MM-YYYY} ** <br>
** End date: {DD-MM-YYYY} **


## Clinical problem

{DESCRIBE THE CLINICAL PROBLEM THAT MUST BE SOLVED}

## Solution

{DESCRIBE THE MAIN RESULT OR INNOVATION OF THE PROJECT AND HOW IT WILL BE INTEGRATED IN RADBOUDUMC ROUTINE CARE}

## Data

{DESCRIBE THE TRAINING AND TEST DATA USED FOR THE PROJECT}

## Approach

{DESCRIBE THE APPROACH USED TO SOLVE THE CLINICAL PROBLEM}

## Results

{DESCRIBE THE RESULTS OF THE PROJECT} 

```

6. To add an image to the text, upload an image of choice to website-content/content/images/projects/ and type `![name of image link]({{ IMGURL }}/images/projects/<image>.png)`. The first `{{ IMGURL }}` is text, don't type the actual filename there. `IMGURL` makes sure the image is always loaded from the correct domain (in case of using a CDN).

7. A preview van be viewed by selecting 'Preview' on the top of the edit page 

8. Add all people involved in the project to ```website-content/content/external-people.yaml```

```
MODIFY ALL INFORMATION GIVEN IN CURLY BRACKETS 

  - name: {FIRSTNAME LASTNAME}
    position: {POSITION}
    affiliation: {DEPARTMENT/MASTER, HOSPITAL/UNIVERSITY}
    url: {URL TO HOSPITAL/UNIVERSITY/LINKEDIN PAGE}
    picture: {people/external/FIRSTNAME_LASTNAME.EXTENSION} (See point 9 below.)
    email: {EMAIL@ADDRESS}

```
9. Upload a square and resized image to ```website-content/content/images/people/external/``` with file name: firstname_lastname

10. Make a pull request of the changes made to your Fork
