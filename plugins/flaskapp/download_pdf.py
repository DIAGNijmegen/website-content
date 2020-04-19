import dropbox
dbx = dropbox.Dropbox("r4ABh_NvBxAAAAAAAAABpyZioVr_ClDgJu4h-lMYDgfFgPSplsKGhQGFzV6YhY2J")
result = dbx.files_get_temporary_link("/Get Started with Dropbox.pdf")
print('link')
print(result.link)

