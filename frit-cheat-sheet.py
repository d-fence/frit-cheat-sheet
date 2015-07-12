#!/usr/bin/python3
import os
import markdown
import jinja2

f = open('frit-cheat-sheet.jinja','r')
d = f.read()
template = jinja2.Template(d)
cheatBlocks = []

for blockFile in sorted(os.listdir('blocks')):
    bpath = os.path.join('blocks', blockFile)
    cb = {}
    with open(bpath,'r') as bf:
        cb['title'] = bf.readline().strip()
        cb['content'] = markdown.markdown(bf.read().strip(),
            extensions=['markdown.extensions.fenced_code',])
        cheatBlocks.append(cb)

output = template.render(cheatBlocks=cheatBlocks)

with open('frit-cheat-sheet.html','w') as outfile:
    outfile.write(output)
