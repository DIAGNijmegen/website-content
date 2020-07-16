# Create a new member page

1. Create a new file in website-content/content/pages/members/
2. Type person's name in entry above. The first and last names should be connected by a dashes and end with .md. For example: ```website-content/content/pages/members/bram-van-ginneken.md```
3. The file should be filled with the following;

```
title: Firstname Lastname
name: Firstname Lastname
template: people-single
picture: people/<image>.png (for adding a picture to a profile see: website-content/docs/adding-picture-to-profile.md. When no picture is availabe, use ```person.png```)
position: Master Student/PhD Candidate/Associate Professor/Assistant Professor/Postdoctoral Researcher/ etc. (pay attention to formulation and capitalisation)
active: yes (change to 'no' when this person is a former employee)
groups: diag, pathology, retina, rse (this determines on which websites the profile will appear. diag is standard, followed by your subgroup)
default_group: diag (the main group of this person, used for internal links. If not set, the first group from 'groups' is used. If set to 'external', internal links and people-circles will load data from external-people.yaml.)
email: example@radboudumc.nl
office: Route ..., room ....
type: phd/chair/faculty/tech/student  (header = Scientific Staff/Chair/Faculty)/Technical Staff/Visiting researchers
linkedin: link
scholar: link
researcherid: link
show_publication_years: yes (if this tag is not present it will be automatically set to yes)

{Text bio.} 
The bio should be written in the 3rd person. Include your former education, the topic of your research and your supervisors. Include links where possible.
External link: [Text](link), e.g.: [Kaggle website](https://www.kaggle.com/c/prostate-cancer-grade-assessment/overview)
Internal link to person: [member/firstname-lastname], e.g.: [member/geert-litjens]
Internal link to project: [project/projectname], e.g. [project/panda-challenge]}  
```

4. After editing, select 'Commit changes' at the bottom of the page. 

# Edit a member page

1. Go to the member page
2. Select the Edit icon at the bottom of the page
3. You are redicted to the markdown file in github
4. Make your changes and commit
