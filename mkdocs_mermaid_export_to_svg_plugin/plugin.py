import re
import time
from os import environ
from datetime import datetime
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
import subprocess
import tempfile

class MermaidExportToSvg(BasePlugin):
    config_scheme = (
        ('export_to_pdf', config_options.Type(bool, default=False)),
        ('debug', config_options.Type(bool, default=False)),
    )

    def __init__(self):
        self.enabled = True

    def on_page_markdown(self, markdown, page, config, files):
        try:
            cnt = markdown.count("mermaid")
            
            for i in range(0,cnt):
                pos = markdown.index("```mermaid") or markdown.index("    ```mermaid") or markdown.index("        ```mermaid")
                pos += 11
                
                start_str = markdown[pos:]
                pos_end = start_str.index("```")
                
                s = start_str[:pos_end]
                tf = tempfile.NamedTemporaryFile(delete=False)
                f = open(tf.name, "w")

                if self.config('debug') is True:
                    print("WRITING MERMAID CODE INTO FILE:")
                    print(s)
                f.write(s)
                f.close()
                tmp_name_svg=tf.name + ".png"
                if self.config('debug') is True:
                    print("MERMAID diagram found! Saving to svg: " + tmp_name_svg)
                
                try:
                    subprocess.run(['mmdc','-s', '1.2', '-t', 'default`', '-b', 'transparent', '-i', tf.name, '-o', tmp_name_svg])
                except subprocess.CalledProcessError as e:
                    print("ERROR IN RUNNING MMDC COMMAND")
                    print(e.output)
               
                if self.config['export_to_pdf'] is False:
                    file_prefix = ""
                else:
                    file_prefix = "file://"

                if self.config('debug') is True:
                    print("Replacing mermaid diagram code with html img tag and prefix:")
                markdown = markdown[:pos-11] + "<img src=\"" + file_prefix + tmp_name_svg + "\" style=\"page-break-inside: avoid;\">" + markdown[pos+pos_end+3:]
        except:
            return markdown
        
        return markdown

    def on_page_content(self, html, page, config, files):
        html = re.sub(r"<p><img", "<img", html)
        html = re.sub(r"svg\"><\/p>", "svg\">", html)
        print(html)
        return html
