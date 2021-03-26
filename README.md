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

## Options

### export_to_pdf (default=false)

Set *export_to_pdf* to true if you want to use your svg in PDF, otherwise (static web) leave it set to false

### debug (default=false)

Use it to see prints to stdout, incl. what will the markdown page look like after including the images.

## Requirements

Plugin requires Mermaid.cli to be installed via npm:

npm install -g mermaid.cli

Tested on mermaid.cli on version 8.8.2-beta.8
