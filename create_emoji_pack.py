
import json
import os
import requests
import shutil
import uuid

# URL for the emoji data
EMOJI_DATA_URL = "https://raw.githubusercontent.com/muan/unicode-emoji-json/main/data-by-group.json"

# Directory to store the generated snippets
SNIPPETS_DIR = "emojis"

def download_emoji_data():
    """Downloads the emoji data from the specified URL."""
    response = requests.get(EMOJI_DATA_URL)
    response.raise_for_status()
    return response.json()

def create_snippet_pack():
    """Creates the Alfred snippet pack."""
    if os.path.exists(SNIPPETS_DIR):
        shutil.rmtree(SNIPPETS_DIR)
    os.makedirs(SNIPPETS_DIR)

    emoji_data = download_emoji_data()

    for group in emoji_data:
        for emoji in group["emojis"]:
            snippet_name = emoji["name"]
            snippet_keyword = f":{emoji['name'].replace(' ', '_')}:"
            snippet_file = os.path.join(SNIPPETS_DIR, f"{snippet_name}.json")

            snippet_data = {
                "alfredsnippet": {
                    "snippet": emoji["emoji"],
                    "uid": str(uuid.uuid4()),
                    "name": snippet_name,
                    "keyword": snippet_keyword,
                }
            }

            with open(snippet_file, "w") as f:
                json.dump(snippet_data, f, indent=2)

    # Create the info.json file
    info_file = os.path.join(SNIPPETS_DIR, "info.json")
    info_data = {
        "name": "Emoji Pack",
        "description": "A collection of all the latest emojis.",
        "keyword": "emoji",
    }
    with open(info_file, "w") as f:
        json.dump(info_data, f, indent=2)

    # Create the archive
    shutil.make_archive("Emoji Pack", "zip", SNIPPETS_DIR)

    # Rename the archive to .alfredsnippets
    os.rename("Emoji Pack.zip", "Emoji Pack.alfredsnippets")

    print("Alfred snippet pack created successfully!")

if __name__ == "__main__":
    create_snippet_pack()
