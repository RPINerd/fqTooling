# ToolDoc Formatting Guide

For each new tool, create a new markdown file in the `docs` directory.

## File Naming

File should be at most a few words camelcased together.  
No spaces, no underscores.

For example, the base content filtering tool would be `BaseContentFilter.md`

## File Formatting

The ToolDoc file should adhere to the following structure:

```markdown
# Tool Name

{Brief description of the tool}

## Requirements

{List of required libraries or dependencies if there are any outside of base python}

## Inputs

{Description of the input files and their format}

## Outputs

{Description of the output files or alterations in place to existing files}

## Manual Usage

{Command line usage when running outside of the TUI}

### Options

{List of command line options and their descriptions}
```