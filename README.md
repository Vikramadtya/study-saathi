# Setup

## Run using `docker`

Spin the container up

```shell
docker-compose up --build
```

## Run Locally

Create new virtual env

```shell
python3 -m venv venv
```

activate the environment

```shell
source venv/bin/activate
```

to install the dependecy

```shell
pip3 install -r requirements.txt
```

to start the server

```shell
python3 -m mkdocs serve
```

## Add new plugin

```shell
pip3 install <plugin>
```

```shell
pip3 freeze > requirements2.txt
```

## Config

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