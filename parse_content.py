import os
import glob
import shutil

directories = ['members', 'highlights', 'presentations', 'projects', 'software', 'vacancies']
sites = ['website-msc-projects', 'website-retina', 'website-pathology', 'website-rse', 'website-diag', 'website-bodyct', 'website-aiimnijmegen']

if not os.path.isdir('output'):
    os.mkdir('output')

for site in sites:
    site_dir = os.path.join('output', site)
    if not os.path.isdir(site_dir):
        os.mkdir(site_dir)

    for dir in directories:
        output_dir = os.path.join(site_dir, dir)
        if not os.path.isdir(output_dir):
            os.mkdir(output_dir)

for dir in directories:
    print(f"Parsing {dir} directory")
    files = glob.glob(os.path.join('content', 'pages', dir, '*.md'))

    for file_path in files:
        print(file_path)
        filename = os.path.basename(file_path)
        with open(file_path) as file:
            for line in file:
                if 'groups:' in line:
                    try:
                        groups = line.split(':')[1].replace(' ','').rstrip().split(',')

                        for group in groups:
                            group_path = f"website-{group}"
                            if group_path not in sites:
                                raise Exception(f"Invalid site {group} in {file_path}.")

                            if dir is 'highlights':
                                # Write hightlights to directory out of pages dir
                                out_dir = os.path.join(group_path, 'content', dir)
                            else:
                                out_dir = os.path.join(group_path, 'content', 'pages', dir)

                            if not os.path.exists(out_dir):
                                os.makedirs(out_dir)
                            shutil.copyfile(file_path, os.path.join(out_dir, filename))
                    except Exception as e:
                        print(f"Error parsing {file_path}.")
                        print(e)
print('done')
