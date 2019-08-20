# Create a new member page

1. Create a new file in website-content/content/pages/members/
2. Type person's name in entry above. The first and last names should be connected by a dashes ad end with .md. For example: website-content/content/pages/members/bram-van-ginneken.mnd
3. The file should be filled with the following;

```
title: Firstname Lastname
name: Firstname Lastname
template: people-single
picture: {filename}.png (for adding a picture to a profile see: website-content/docs/adding-picture-to-profile.md)
position: PhD student/Associate Professor/Assistant Professor/Postdoctoral researcher/ etc. (free text but keep consistent throughout pages, so please check how other groups have written down the positions)
active: yes (change to 'no' when this person is a former employee)
groups: diag, pathology, retina, rse (this determines on which websites the profile will appear. DIAG is standard, followed by your subgroup)
default_group: diag (the main group of this person, used for internal links. If not set, the first group from 'groups' is used.)
email: example@radboudumc.nl
office: Route ..., room ....
type: phd (profile appears under Scientific Staff)/faculty (profile appears under Faculty)/tech(profile appears under Technical Staff)/student(profile appears under Visiting researchers)
linkedin: link
scholar: link
researcherid: link

{Text bio.}  
```

4. After editing, select 'Commit changes' at the bottom of the page. 
