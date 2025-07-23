# Emoji Pack for Alfred

This repository contains a script to generate an Alfred snippet pack for emojis.

## Usage

### Prerequisites

- Python 3
- `requests` library (`pip install requests`)

### Generating the Snippet Pack

To generate the `Emoji Pack.alfredsnippets` file, run the following command:

```bash
python create_emoji_pack.py
```

This will create the `Emoji Pack.alfredsnippets` file in the root of the repository.

### Installation

1.  Double-click the `Emoji Pack.alfredsnippets` file to open it in Alfred.
2.  Click "Import" to add the snippets to your Alfred collection.

## Data Source

The emoji data is sourced from the [unicode-emoji-json](https://github.com/muan/unicode-emoji-json) repository.
