# mkdocs-mermaid-export-to-svg

MkDocs plugin that exports mermaid diagrams to PNG/SVG format and
attaches images into html page with img src tag.

## Setup
Install the plugin using pip:

`pip install mkdocs-mermaid-export-to-svg`

Activate the plugin in `mkdocs.yml`:

```yaml
plugins:
  - search
  - mermaid-export-to-svg
```

More information about plugins in the [MkDocs documentation][mkdocs-plugins].

## Usage

Attach mermaid diagram in your markdown as follows:

```mermaid
   ...
```

Then it will be extracted using the plugin, and the PNG/SVG image will be generated with the mermaid.cli usage

### Requirements

Plugin requires Mermaid.cli to be installed via npm:

npm install -g mermaid.cli

Tested on mermaid.cli on version 8.8.2-beta.8
