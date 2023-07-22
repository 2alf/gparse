# gparse
quick tool that separates group tags in svgs for future parsing 

Helps you find unique `<g>` tags and save specific `<g>` tags as separate SVG files.

## Usage 🐻

```bash
git clone https://github.com/2alf/gparse.git
python3 main.py
```

- load file
```python
- Enter the path to the SVG file: [ /path/MyFile.svg ]
- Found [$x] unique <g> tags in the SVG file.
```

-read
```python
read <index>
```

-save
```python
save <index>
```

-quit
```python
q
```


# Known issues
- On files with over 600 <g> tags it doesnt automatically copy the <?xml> header.
