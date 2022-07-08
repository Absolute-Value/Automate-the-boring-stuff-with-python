#! /usr/bin/env python3
# 8.10.2 作文ジェネレータ

import re

origin_file = open("Composition/Origin.txt")
origin_content = origin_file.read()
origin_file.close()

content_regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
targets = content_regex.findall(origin_content)

export_content = origin_content
for target in targets:
    export_content = re.sub(target, input(f"Enter {target.lower()}:\n"), export_content, 1)

print(export_content)
export_file = open("Composition/Generated.txt", 'a')
export_file.write(export_content)
export_file.close()