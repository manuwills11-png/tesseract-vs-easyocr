# OCR Comparison

Compares Tesseract and EasyOCR text extraction on images using Jaccard similarity to measure accuracy between the two methods.

## How it works

1. Both Tesseract and EasyOCR read text from the same image
2. The extracted texts are compared using Jaccard similarity
3. A score of `1.0` means both methods extracted identical text, `0.0` means no overlap

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

> Tesseract also requires a separate installation:
> - Windows: download from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)

## Usage

Place your image in the `photo/` folder and update `image_path` in `main.py`, then run:

```bash
python main.py
```

## Example output

```
Tesseract: STAY BADASS
EasyOCR: STAY BADASS
Jaccard Similarity: 1.0000
```

## Dependencies

- [pytesseract](https://github.com/madmaze/pytesseract)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [OpenCV](https://opencv.org/)
