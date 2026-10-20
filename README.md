# QR Code Generator

A simple desktop app built with Python and Tkinter that turns any text or URL into a QR code. Preview it instantly and save it as a PNG.

## Features

- Generate QR codes from text or URLs
- Live preview inside the app
- Save the QR code as a PNG image
- Press **Enter** to generate quickly
- Automatically lowers error-correction level for long text, so longer inputs still work
- Works on Windows, macOS and Linux

## Requirements

- Python 3.8 or newer
- Tkinter (included with Python on Windows and macOS)
- Python packages listed in `requirements.txt`:

```
qrcode[pil]>=7.4
Pillow>=9.1
```

## Installation

1. Put `qr_generator.py` and `requirements.txt` in the same folder.
2. Open a terminal in that folder.
3. Create and activate a virtual environment (recommended):

**Windows (PowerShell)**
```
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```
python3 -m venv venv
source venv/bin/activate
```

4. Install the dependencies:

```
python -m pip install -r requirements.txt
```

## Usage

```
python qr_generator.py
```

1. Type or paste text or a URL into the box.
2. Click **Generate QR Code** (or press Enter).
3. Check the preview.
4. Click **Save QR Code as PNG** and choose where to save it.

## Project Structure

```
python_QR_Code_generator/
├── qr_generator.py
├── requirements.txt
└── README.md
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `Invalid requirement` when installing | `requirements.txt` must contain only package names (see above), not commands like `pip install` |
| `No module named qrcode` | Activate the virtual environment, then run `python -m pip install -r requirements.txt` |
| `No module named '_tkinter'` (macOS, Homebrew) | `brew install python-tk` |
| Tkinter or ImageTk missing (Debian/Ubuntu) | `sudo apt install python3-tk python3-pil.imagetk` |
| `pip` not recognized | Use `python -m pip ...` instead of `pip ...` |
| "Text is too long" message | A QR code holds roughly 2,900 characters at most; shorten the input |

## Built With

- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [qrcode](https://pypi.org/project/qrcode/)
- [Pillow](https://pypi.org/project/pillow/)
