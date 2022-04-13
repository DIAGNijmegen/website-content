# Removing a website

To remove one of the websites entirely, the following steps need to performed strictly in this order:

## Remove DNS settings

Delete or change the DNS record for the domain or subdomain in the yourhosting account. Remember to note the changes in the DNS ticket (#9282) in trac.

## Remove website from build pipeline

In the `deploy-master.yml` file in the GitHub Actions workflow configuration (inside the repository in the `.github` folder), remove the website from the matrix configuration. This will exclude the website from the automated build process, even though the content is still in the repository.

## Remove website name from list of secrets

In the settings dialog of the repository, navigate to the secrets page and remove the secret with the name of the website.

## Remove website from netlify

Delete the corresponding netlify site in the netlify dashboard.

## Remove website content

Delete the folder with the content of the website, i.e., `website-XXX` in the root of the repository.

Also, remove content specific to the removed website from the general `content` folder. If there are pages, like member profiles for example, with the default_group set to the removed website, this will break the build. Either remove these pages or assign a different default group. If this concerns members who should now no longer be visible on any website, do not remove their profile page but set them to inactive instead. This will ensure that their publications remain on the website.
