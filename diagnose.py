import os

file_path = r"front\responsavel\dashboard_responsavel.html"

with open(file_path, "rb") as f:
    raw = f.read()

print(f"Total bytes: {len(raw)}")
print(f"First 12 bytes: {raw[:12].hex()}")

# Find the first occurrence of C3 83 (which is "Ã" in double-encoded UTF-8)
idx = raw.find(b"\xc3\x83")
if idx >= 0:
    window = raw[max(0,idx-4):idx+12]
    print(f"\nFound C3 83 at offset {idx}")
    print(f"Context hex: {window.hex()}")
    print(f"Context ASCII: {window}")
    
    # Try to decode this specific window with different encodings
    try:
        print(f"As UTF-8:    {window.decode('utf-8', errors='replace')}")
    except: pass
    try:
        print(f"As Latin-1:  {window.decode('latin-1')}")
    except: pass
else:
    print("C3 83 NOT found")

# Try the round-trip repair on first 500 bytes containing mojibake
chunk = raw[:500]
print(f"\n--- chunk (500 bytes) ---")
print(f"As UTF-8 (errors=replace): {chunk.decode('utf-8', errors='replace')[:200]}")
print(f"\nAs Latin-1: {chunk.decode('latin-1')[:200]}")

# Try unwrap: decode as Latin-1 -> encode as Latin-1 -> decode as UTF-8
try:
    step1 = chunk.decode('latin-1')            # each UTF-8 byte pair -> one Latin-1 char
    step2 = step1.encode('latin-1')             # re-encode back to bytes
    step3 = step2.decode('utf-8', errors='replace')  # now decode as UTF-8
    print(f"\nAfter 1 unwrap: {step3[:200]}")
    
    step4 = step3.encode('latin-1', errors='replace')
    step5 = step4.decode('utf-8', errors='replace')
    print(f"After 2 unwraps: {step5[:200]}")
except Exception as e:
    print(f"Error: {e}")
