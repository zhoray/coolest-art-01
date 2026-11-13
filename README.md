# Sky Leviathan

*Sky Leviathan* is a digital painting of a colossal whale gliding across a huge, glowing low sun in a deep indigo-violet dusk sky, above dark mountain ridges.

The entry program copies the artwork file `art.jpg` byte-for-byte to `entry.png`. The competition gate identifies the image by its file contents, so the output keeps the original JPEG bytes and is deterministic on every run.

## Run locally

Python 3.13 is required. By default, the program writes to `/output`:

```sh
python3 main.py
```

To choose another output directory, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

You can also pass an output directory as an optional positional argument. It takes precedence over `MAKEFUN_OUTPUT_DIR`:

```sh
python3 main.py out
```
