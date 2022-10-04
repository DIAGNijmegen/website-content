# Create a new member page

1. Create a new file in website-content/content/pages/members/
2. Type person's name in entry above. The first and last names should be connected by a dashes and end with .md. For example: ```website-content/content/pages/members/bram-van-ginneken.md```
3. The file should be filled with the following;

```
title: Firstname Lastname
name: Firstname Lastname
pub_name: publication name / pseudonym
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
publons: link
orcid: link
twitter: link
show_publication_years: yes (if this tag is not present it will be automatically set to yes)

{Text bio.} 
The bio should be written in the 3rd person. Include your former education, the topic of your research and your supervisors. Include links where possible.
External link: [Text](link), e.g.: [Kaggle website](https://www.kaggle.com/c/prostate-cancer-grade-assessment/overview)
Internal link to person: [member/firstname-lastname], e.g.: [member/geert-litjens]
Internal link to project: [project/projectname], e.g. [project/panda-challenge]}  
```

4. After editing, select 'Commit changes' at the bottom of the page.

## Guidelines

* Check the other people pages to see what a bio text looks like. Write in the same style.
* Make sure you mention the project you work on as a link.
* Make sure you mention who supervises you, and make this a link, with "[member/bram-van-ginneken]" you create a link to a people page. You can make links by putting the link text between square brackets [ and ] immediately followed by the url between normal parentheses, ( and ). You can refer to publications with "/publications/kars92" as the url text.
* Do not write a title like Prof. or Professor or Dr. before the name of a colleague.

# Editing a member page

1. Go to the member page
2. Select the Edit icon at the bottom of the page
3. You are redirected to the markdown file on GitHub
4. Make your changes and commit
