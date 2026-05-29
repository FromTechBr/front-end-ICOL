"""
Final fix: the encoding chain is UTF-8 bytes -> read as windows-1252 -> save as UTF-8.
Key insight: byte 0x83 is undefined in ISO-8859-1 but IS 'f with hook' (U+0192) in Windows-1252.
That's why 'C3 83' (which is U+00C3 = Ã in UTF-8) when re-read as windows-1252 gives
'Ã' then 'ƒ' (0x83 = U+0192 in cp1252), then saved as UTF-8: C3 83  C6 92.

We can see this in the hex: C3 83 C6 92 C3 82 C2 A1 
  C3 83 -> 'Ã' (U+00C3)
  C6 92 -> 'ƒ' (U+0192)  -- this only comes from cp1252 encoding of 0x83
  C3 82 -> 'Â' (U+00C2)
  C2 A1 -> '¡' (U+00A1)
So the string is "Ãƒ Â¡" which is 'á' triple-encoded via windows-1252.

FIX: read the file as UTF-8 (get the mojibake string),
     encode it as windows-1252 to get bytes back,
     decode those bytes as UTF-8.
     Repeat until stable.
"""

import os

front_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "front")

def unwrap(text, passes=3):
    """Unwrap Mojibake encoded via windows-1252."""
    for i in range(passes):
        try:
            b = text.encode("windows-1252")
            decoded = b.decode("utf-8")
            if decoded == text:
                break
            text = decoded
        except (UnicodeEncodeError, UnicodeDecodeError):
            # Try next: encode as cp1252 ignoring errors
            try:
                b = text.encode("windows-1252", errors="replace")
                decoded = b.decode("utf-8", errors="replace")
                if decoded != text:
                    text = decoded
            except Exception:
                pass
            break
    return text

fixed_count = 0
for root, dirs, files_list in os.walk(front_dir):
    for fname in files_list:
        if not fname.endswith(".html"):
            continue
        path = os.path.join(root, fname)
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            original = f.read()

        content = original.lstrip("\ufeff")  # strip BOM char
        fixed = unwrap(content)

        rel = os.path.relpath(path, front_dir)
        if fixed != original.lstrip("\ufeff"):
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(fixed)
            print(f"FIXED: {rel}")
            fixed_count += 1
        else:
            print(f"OK:    {rel}")

print(f"\nDone. {fixed_count} file(s) corrected.")
