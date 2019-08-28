import os
import glob
import shutil
import sys

directories = ['members', 'highlights', 'presentations', 'projects', 'software', 'vacancies', 'calendar']
site = sys.argv[1]
group_name = site[8:]

print(f"Copying content for {site} (group: {group_name}")

# if not os.path.isdir('output'):
#     os.mkdir('output')

# Create directory
site_dir = os.path.join('output', site)
if not os.path.isdir(site_dir):
    os.mkdir(site_dir)

for dir in directories:
    output_dir = os.path.join(site_dir, dir)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

for dir in directories:
    files = glob.glob(os.path.join('content', 'pages', dir, '*.md'))

    for file_path in files:
        filename = os.path.basename(file_path)
        with open(file_path) as file:
            for line in file:
                if 'groups:' in line:
                    try:
                        groups = line.split(':')[1].replace(' ','').rstrip().split(',')

                        # Check if the content belongs to the current website
                        if group_name in groups:
                            if dir is 'highlights':
                                # Write hightlights to directory out of pages dir
                                out_dir = os.path.join(site, 'content', dir)
                            else:
                                out_dir = os.path.join(site, 'content', 'pages', dir)

                            if not os.path.exists(out_dir):
                                os.makedirs(out_dir)
                            shutil.copyfile(file_path, os.path.join(out_dir, filename))
                    except Exception as e:
                        print(f"Error parsing {file_path}.")
                        print(e)
print(f'Copied pages to website {site}.')
