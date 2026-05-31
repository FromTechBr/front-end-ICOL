import os, glob, re

front_dir = r"c:\Users\isaqu\OneDrive\Documentos\Front-End ICOL\front"
files = sorted(glob.glob(os.path.join(front_dir, "**", "*.html"), recursive=True))

word_q = re.compile(r"[A-Za-z\u00c0-\u024f]{2,}\?|\?[A-Za-z\u00c0-\u024f]{2,}|\?{2,}")
safe   = re.compile(r"loginForm\?|aiToggle\?|aiPanel\?|\?\.|Esqueceu a senha\?")

total_issues = 0
for path in files:
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    rel = os.path.relpath(path, front_dir)

    fffd  = content.count(chr(0xfffd))
    bad_q = [m.group() for m in word_q.finditer(content)
             if not safe.search(content[max(0, m.start()-20):m.end()+20])]

    if fffd or bad_q:
        print("ISSUE: " + rel)
        if fffd:
            print("       " + str(fffd) + " U+FFFD chars")
        if bad_q:
            print("       suspicious ?: " + str(bad_q[:8]))
        total_issues += 1
    else:
        print("OK   : " + rel)

print()
if total_issues == 0:
    print("ALL 19 FILES PERFECTLY CLEAN.")
else:
    print(str(total_issues) + " file(s) still need attention.")
