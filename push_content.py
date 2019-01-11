import git

repo = git.Repo('output')

diff = repo.index.diff('HEAD')

sites_to_check = ['website-diag', 'website-pathology']
updated_sites = []

for file in diff:
    for s in sites_to_check:
        if s in file.a_path:
            updated_sites.append(s)
            sites_to_check.remove(s)

print(updated_sites)
