import os
import glob
import shutil
import sys

from pelican.settings import get_settings_from_file

directories = [
    "about",
    "members",
    "news",
    "presentations",
    "projects",
    "software",
    "vacancies",
    "calendar",
    "publications",
    "research",
]

site = sys.argv[1]
group_name = site[8:]

print(f"Copying content for {site} (group: {group_name})")

for dir in directories:
    output_dir = os.path.join(site, dir)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

for dir in directories:
    files = glob.glob(os.path.join("content", "pages", dir, "*.md"))

    for file_path in files:
        filename = os.path.basename(file_path)
        with open(file_path) as file:
            try:
                for line in file:
                    if "groups:" in line:
                        groups = line.split(":")[1].replace(" ", "").rstrip().split(",")
                        # Check if the content belongs to the current website
                        if group_name in groups:
                            if dir == "news":
                                # Write hightlights to directory out of pages dir
                                out_dir = os.path.join(site, "content", dir)
                            else:
                                out_dir = os.path.join(site, "content", "pages", dir)

                            if not os.path.exists(out_dir):
                                os.makedirs(out_dir)
                            if dir == "members":
                                print(os.path.join(out_dir, filename))
                            shutil.copyfile(file_path, os.path.join(out_dir, filename))

                        # Stop parsing file
                        #break
            except Exception as e:
                print(f"Error parsing {file_path}.")
                print(e)

# Copy only the default pages that are actually used
default_pages = set()

# -> pages that are linked to in the navigation bar
settings = get_settings_from_file(os.path.join(site, "pelicanconf.py"))
for section in settings["NAV_SECTIONS"]:
    page = section["url"].split("/")[0] + ".md"
    default_pages.add(page)

# -> pages that have a sub-content, e.g., software pages exist = copy software.md
for file_path in glob.glob(os.path.join("content", "pages", "defaults", "*.md")):
    page = os.path.basename(file_path)
    name = page[:-3]
    if os.path.exists(os.path.join(site, "content", "pages", name)):
        default_pages.add(page)

for page in default_pages:
    src_path = os.path.join("content", "pages", "defaults", page)
    dst_path = os.path.join(site, "content", "pages", page)
    if os.path.exists(src_path) and not os.path.exists(dst_path):
        shutil.copyfile(src_path, dst_path)

print(f"Copied pages to {site}.")
