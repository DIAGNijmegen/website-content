import os
import glob
import shutil
import sys

directories = ['members', 'highlights', 'presentations', 'projects', 'software', 'vacancies', 'calendar', 'publications']
site = sys.argv[1]
group_name = site[8:]

print(f"Copying content for {site} (group: {group_name})")

for dir in directories:
    output_dir = os.path.join(site, dir)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

for dir in directories:

    files = glob.glob(os.path.join('content', 'pages', dir, '*.md'))

    for file_path in files:
        filename = os.path.basename(file_path)
        with open(file_path) as file:
            try:
                for line in file:
                    if 'groups:' in line:

                            groups = line.split(':')[1].replace(' ','').rstrip().split(',')

                            # Check if the content belongs to the current website
                            if group_name in groups:
                                if dir is 'highlights':
                                    # Write hightlights to directory out of pages dir
                                    out_dir = os.path.join(site, 'content', dir)
                                else:
                                    out_dir = os.path.join(site, 'content', 'pages', dir)

                                # copy author publication folder
                                if dir is 'publications':
                                    author_publication_folder = filename.replace('.md', '')
                                    author_publication_path = os.path.join('content', 'pages', dir, author_publication_folder)
                                    if os.path.exists(author_publication_path):
                                        out_author_publication_path = os.path.join(site, 'content', 'pages', dir, author_publication_folder)
                                        shutil.copytree(author_publication_path, out_author_publication_path)

                                if not os.path.exists(out_dir):
                                    os.makedirs(out_dir)
                                shutil.copyfile(file_path, os.path.join(out_dir, filename))
  


                            # Stop parsing file
                            break
            except Exception as e:
                print(f"Error parsing {file_path}.")
                print(e)

        


print(f'Copied pages to {site}.')
