from setuptools import setup, find_packages

setup(
    name='mkdocs-mermaid-export-to-svg',
    version='0.2.4',
    description='MkDocs plugin for showing a history log for a specified markdown file',
    keywords='mkdocs git meta yaml frontmatter',
    url='https://github.com/pawelsikora/mkdocs-export-mermaid-to-svg/',
    author='Pawel Sikora',
    author_email='sikor6@gmail.com',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'mkdocs>=1.1',
        'GitPython',
        'jinja2'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'mermaid-export-to-svg = mkdocs_mermaid_export_to_svg_plugin.plugin:MermaidExportToSvg'
        ]
    }
)
