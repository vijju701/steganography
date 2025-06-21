# steganography
The steganography in cyber security is used to encode and decode the sensitive and confidential information in a picture/image.

# LSB‑Stego — Hide and Seek with Images 🔒🖼️

A tiny Python tool that uses **least significant bit (LSB) steganography** to hide text inside any RGB image.  
Give it a carrier picture and a secret message—it will embed the message by flipping just the lowest bit of each pixel’s color values. The change is visually imperceptible, but the data can be extracted later with the built‑in decoder.

---

## ✨ Features
- **Encode** any ASCII text into a PNG/JPEG/BMP image.
- **Decode** and reveal a hidden message from a stego image.
- Supports lossless formats (PNG, BMP) for perfect recovery.
- Minimal code—under 100 lines, pure Python + Pillow.

---

## 📦 Requirements
| Package | Version |
|---------|---------|
| Python  | 3.8 +   |
| Pillow  | ^10.0   |

```bash
pip install pillow


