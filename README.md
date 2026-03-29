# Setup

Setip commands

```shell
> which python3
> python -m venv venv
> source venv/bin/activate
> pip install mkdocs-material
> mkdocs new .
> mkdocs serve
```

Open `settings.json` by clicking the ⚙ gear icon in the bottom left, then clicking the 📄 document icon in the top right.

add the following at the bottom of the `settings.json` file:

```json
  "yaml.schemas": {
    "https://squidfunk.github.io/mkdocs-material/schema.json": "mkdocs.yml"
  },
  "yaml.customTags": [
    "!ENV scalar",
    "!ENV sequence",
    "!relative scalar",
    "tag:yaml.org,2002:python/name:material.extensions.emoji.to_svg",
    "tag:yaml.org,2002:python/name:material.extensions.emoji.twemoji",
    "tag:yaml.org,2002:python/name:pymdownx.superfences.fence_code_format"
  ]
```

Now when you mouse-over any of the entries in the mkdocs.yml file, you'll see a popup with more information about that entry. Any errors in the yaml file will also be highlighted.

## References

- [Material for MkDocs: Full Tutorial To Build And Deploy Your Docs Portal](https://jameswillett.dev/getting-started-with-material-for-mkdocs/#add-yaml-schema-validation)