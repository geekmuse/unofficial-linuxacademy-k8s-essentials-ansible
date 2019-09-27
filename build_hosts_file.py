#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import yaml

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, ".")

e = Environment(loader=FileSystemLoader(templates_dir))
e.add_extension("jinja2.ext.do")

with open('conf.yml') as f:
    config = yaml.safe_load(f)

    for filename in os.listdir(templates_dir):
        if filename.endswith(".j2"):
            tpl = e.get_template(filename)
            with open(f"{templates_dir}{os.path.sep}{filename[0:-3]}", "w") as out:
                out.write(tpl.render(config=config))
