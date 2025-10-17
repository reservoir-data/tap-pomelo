<div align="center">

# tap-pomelo

<div>
  <a href="https://scientific-python.org/specs/spec-0000/">
    <img alt="SPEC 0 — Minimum Supported Dependencies" src="https://img.shields.io/badge/SPEC-0-green?labelColor=%23004811&color=%235CA038"/>
  </a>
  <a href="https://results.pre-commit.ci/latest/github/reservoir-data/tap-pomelo/main">
    <img alt="pre-commit.ci status" src="https://results.pre-commit.ci/badge/github/reservoir-data/tap-pomelo/main.svg"/>
  </a>
  <a href="https://github.com/reservoir-data/tap-pomelo/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/reservoir-data/tap-pomelo"/>
  </a>
</div>

Singer tap for [Pomelo](https://pomelo.la/mx/).

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

</div>

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`

## Settings

| Setting | Required | Default | Description |
|:--------|:--------:|:-------:|:------------|
| client_id | True | None | Client ID to authenticate in Pomelo |
| client_secret | True | None | Client secret to authenticate in Pomelo |
| audience | True | https://auth.pomelo.la | Audience to authenticate in Pomelo |
| api_url | True | https://api.pomelo.la | Base URL for the API |
| stream_maps | False | None | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |
| stream_maps.__else__ | False | None | Currently, only setting this to `__NULL__` is supported. This will remove all other streams. |
| stream_map_config | False | None | User-defined config values to be used within map expressions. |
| faker_config | False | None | Config for the [`Faker`](https://faker.readthedocs.io/en/master/) instance variable `fake` used within map expressions. Only applicable if the plugin specifies `faker` as an additional dependency (through the `singer-sdk` `faker` extra or directly). |
| faker_config.seed | False | None | Value to seed the Faker generator for deterministic output: https://faker.readthedocs.io/en/master/#seeding-the-generator |
| faker_config.locale | False | None | One or more LCID locale strings to produce localized output for: https://faker.readthedocs.io/en/master/#localization |
| flattening_enabled | False | None | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth | False | None | The max depth to flatten schemas. |
| batch_config | False | None | Configuration for BATCH message capabilities. |
| batch_config.encoding | False | None | Specifies the format and compression of the batch files. |
| batch_config.encoding.format | False | None | Format to use for batch files. |
| batch_config.encoding.compression | False | None | Compression format to use for batch files. |
| batch_config.storage | False | None | Defines the storage layer to use when writing batch files |
| batch_config.storage.root | False | None | Root path to use when writing batch files. |
| batch_config.storage.prefix | False | None | Prefix to use when writing batch files. |

A full list of supported settings and capabilities is available by running: `tap-pomelo --about`

## Usage

You can easily run `tap-pomelo` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-pomelo --version
tap-pomelo --help
tap-pomelo --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh  # or see https://docs.astral.sh/uv/getting-started/installation/
uv sync
```

### Create and Run Tests

Create tests within the `tests` subfolder and then run:

```bash
uv run pytest
```

You can also test the `tap-pomelo` CLI interface directly:

```bash
uv run tap-pomelo --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Use Meltano to run an EL pipeline:

```bash
# Test invocation:
uvx meltano invoke tap-pomelo --version

# OR run a test `elt` pipeline:
uvx meltano run tap-pomelo target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
