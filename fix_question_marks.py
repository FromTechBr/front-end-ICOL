"""
Definitive fix for all remaining '?' Mojibake in ICOL HTML files.
Each '?' stands in for a missing accented/special character.
We use context-aware word-pattern replacement (longest patterns first).
"""
import os, glob, re

front_dir = r"c:\Users\isaqu\OneDrive\Documentos\Front-End ICOL\front"
files = sorted(glob.glob(os.path.join(front_dir, "**", "*.html"), recursive=True))

Q = "?"  # the stand-in character

# -----------------------------------------------------------------------
# Replacement table  — ORDER MATTERS: longer / more-specific FIRST
# -----------------------------------------------------------------------
fixes = [
    # ── 3-char + compounds ──────────────────────────────────────────────
    ("Capacita??o",          "Capacitação"),
    ("capacita??o",          "capacitação"),
    ("Orienta??o",           "Orientação"),
    ("orienta??o",           "orientação"),
    ("Transforma??o",        "Transformação"),
    ("transforma??o",        "transformação"),
    ("Localiza??o",          "Localização"),
    ("localiza??o",          "localização"),
    ("Organiza??o",          "Organização"),
    ("organiza??o",          "organização"),
    ("Inscri??es",           "Inscrições"),
    ("inscri??es",           "inscrições"),
    ("Inscri??o",            "Inscrição"),
    ("inscri??o",            "inscrição"),
    ("Coordena??o",          "Coordenação"),
    ("coordena??o",          "coordenação"),
    ("Educa??o",             "Educação"),
    ("educa??o",             "educação"),
    ("Doa??o",               "Doação"),
    ("doa??o",               "doação"),
    ("Atua??o",              "Atuação"),
    ("atua??o",              "atuação"),
    ("Situa??o",             "Situação"),
    ("situa??o",             "situação"),
    ("Aten??o",              "Atenção"),
    ("aten??o",              "atenção"),
    ("Evolu??o",             "Evolução"),
    ("evolu??o",             "evolução"),
    ("Observa??o",           "Observação"),
    ("observa??o",           "observação"),
    ("Avalia??o",            "Avaliação"),
    ("avalia??o",            "avaliação"),
    ("Participa??o",         "Participação"),
    ("participa??o",         "participação"),
    ("Comunica??o",          "Comunicação"),
    ("comunica??o",          "comunicação"),
    ("Constru??o",           "Construção"),
    ("constru??o",           "construção"),
    ("Atualiza??o",          "Atualização"),
    ("atualiza??o",          "atualização"),
    ("Colabora??o",          "Colaboração"),
    ("colabora??o",          "colaboração"),
    ("Orienta??es",          "Orientações"),
    ("orienta??es",          "orientações"),
    ("Avalia??es",           "Avaliações"),
    ("avalia??es",           "avaliações"),
    ("Observa??es",          "Observações"),
    ("observa??es",          "observações"),
    ("Inscri??es",           "Inscrições"),

    # ── ção / ção-variants (single-? compounds) ────────────────────────
    ("Descri??o",            "Descrição"),
    ("descri??o",            "descrição"),
    ("Informa??o",           "Informação"),
    ("informa??o",           "informação"),
    ("Revisa??o",            "Revisão"),
    ("revisa??o",            "revisão"),
    ("Homenagem",            "Homenagem"),   # not corrupted, guard
    ("Publica??o",           "Publicação"),
    ("publica??o",           "publicação"),
    ("Institui??o",          "Instituição"),
    ("institui??o",          "instituição"),
    ("Navega??o",            "Navegação"),
    ("navega??o",            "navegação"),
    ("Administra??o",        "Administração"),
    ("administra??o",        "administração"),

    # ── ??o / ??es → ção / ções (generic fallback) ──────────────────
    ("??o",                  "ção"),
    ("??es",                 "ções"),
    ("??es",                 "ções"),

    # ── Single-? words (alphabetical by correct word) ───────────────────
    ("acolhimento",          "acolhimento"),   # not corrupted
    ("Acredito que ?",       "Acredito que é"),
    ("? mantido",            "é mantido"),
    ("? uma linda",          "é uma linda"),
    ("? atrav?s",            "é através"),
    ("atrav?s",              "através"),
    ("Atrav?s",              "Através"),
    ("ap?s",                 "após"),
    ("Ap?s",                 "Após"),
    ("?rea",                 "Área"),
    ("?reas",                "Áreas"),
    ("Aul?o",                "Aulão"),
    ("aul?o",                "aulão"),
    ("Calend?rio",           "Calendário"),
    ("calend?rio",           "calendário"),
    ("capacita??o",          "capacitação"),   # already above but guard
    ("conte?do",             "conteúdo"),
    ("Conte?do",             "Conteúdo"),
    ("conte?dos",            "conteúdos"),
    ("Conte?dos",            "Conteúdos"),
    ("consult?rio",          "consultório"),
    ("Consult?rio",          "Consultório"),
    ("cria??o",              "criação"),
    ("Cria??o",              "Criação"),
    ("Di?rio",               "Diário"),
    ("di?rio",               "diário"),
    ("D?vidas",              "Dúvidas"),
    ("d?vidas",              "dúvidas"),
    ("Descri??o",            "Descrição"),
    ("espa?o",               "espaço"),
    ("Espa?o",               "Espaço"),
    ("Esqueceu a senha?",    "Esqueceu a senha?"),  # keep real ?
    ("experi?ncia",          "experiência"),
    ("Experi?ncia",          "Experiência"),
    ("exig?ncias",           "exigências"),
    ("Exig?ncias",           "Exigências"),
    ("Fa?a",                 "Faça"),
    ("fa?a",                 "faça"),
    ("fam?lia",              "família"),
    ("Fam?lia",              "Família"),
    ("frequ?ncia",           "frequência"),
    ("Frequ?ncia",           "Frequência"),
    ("Fl?via",               "Flávia"),
    ("fl?via",               "flávia"),
    ("Hist?ria",             "História"),
    ("hist?ria",             "história"),
    ("Hist?rias",            "Histórias"),
    ("hist?rias",            "histórias"),
    ("Hist?rico",            "Histórico"),
    ("hist?rico",            "histórico"),
    ("Hor?rio",              "Horário"),
    ("hor?rio",              "horário"),
    ("In?cio",               "Início"),
    ("in?cio",               "início"),
    ("Inform?tica",          "Informática"),
    ("inform?tica",          "informática"),
    ("Laborat?rio",          "Laboratório"),
    ("laborat?rio",          "laboratório"),
    ("Lan?ar",               "Lançar"),
    ("lan?ar",               "lançar"),
    ("Lan?amento",           "Lançamento"),
    ("lan?amento",           "lançamento"),
    ("Links R?pidos",        "Links Rápidos"),
    ("links r?pidos",        "links rápidos"),
    ("M?dia",                "Média"),
    ("m?dia",                "média"),
    ("m?ximo",               "máximo"),
    ("M?ximo",               "Máximo"),
    ("mem?rias",             "memórias"),
    ("Mem?rias",             "Memórias"),
    ("mem?ria",              "memória"),
    ("Mem?ria",              "Memória"),
    ("miss?o",               "missão"),
    ("Miss?o",               "Missão"),
    ("m?e",                  "mãe"),
    ("M?e",                  "Mãe"),
    ("Navega??o",            "Navegação"),
    ("Ol?",                  "Olá"),
    ("ol?",                  "olá"),
    ("orienta??o",           "orientação"),
    ("Orienta??o",           "Orientação"),
    ("p?blico",              "público"),
    ("P?blico",              "Público"),
    ("Plant?o",              "Plantão"),
    ("plant?o",              "plantão"),
    ("pr?dio",               "prédio"),
    ("Pr?dio",               "Prédio"),
    ("pr?prios",             "próprios"),
    ("Pr?prios",             "Próprios"),
    ("pr?tica",              "prática"),
    ("Pr?tica",              "Prática"),
    ("pr?tico",              "prático"),
    ("Pr?ximo",              "Próximo"),
    ("pr?ximo",              "próximo"),
    ("prop?sito",            "propósito"),
    ("Prop?sito",            "Propósito"),
    ("Publica??o",           "Publicação"),
    ("r?pidos",              "rápidos"),
    ("R?pidos",              "Rápidos"),
    ("r?pido",               "rápido"),
    ("Refor?o",              "Reforço"),
    ("refor?o",              "reforço"),
    ("Refor?ar",             "Reforçar"),
    ("refor?ar",             "reforçar"),
    ("Relat?rios",           "Relatórios"),
    ("relat?rios",           "relatórios"),
    ("Revis?o",              "Revisão"),
    ("revis?o",              "revisão"),
    ("Respons?vel",          "Responsável"),
    ("respons?vel",          "responsável"),
    ("Secret?ria",           "Secretária"),
    ("secret?ria",           "secretária"),
    ("seguran?a",            "segurança"),
    ("Seguran?a",            "Segurança"),
    ("tamb?m",               "também"),
    ("Tamb?m",               "Também"),
    ("T?tulo",               "Título"),
    ("t?tulo",               "título"),
    ("volunt?rios",          "voluntários"),
    ("Volunt?rios",          "Voluntários"),

    # ── Prepositions / short words ─────────────────────────────────────
    ("? educa",              "à educa"),
    ("? transforma",         "à transforma"),
    ("19h ?s 21h",           "19h às 21h"),
    ("21h ?s 22h",           "21h às 22h"),
    ("?s",                   "às"),
    ("?",                    "é"),   # last resort lone accented vowel (be careful)
]

# Deduplicate preserving order (first occurrence wins = most specific)
seen = set()
deduped = []
for bad, good in fixes:
    if bad not in seen and bad != good:
        seen.add(bad)
        deduped.append((bad, good))

# -----------------------------------------------------------------------
# Apply fixes and verify
# -----------------------------------------------------------------------
SAFE_Q_PATTERNS = [
    r'loginForm\?',          # JS optional chaining
    r'aiToggle\?',
    r'aiPanel\?',
    r'\?\.',                 # JS ?. optional chaining
    r'Esqueceu a senha\?',   # genuine question mark
    r'href="\?',             # URL query string
    r'src="\?',
]

def is_safe_question_mark(content, pos):
    """Return True if the ? at position pos is a real ? (not Mojibake)."""
    for pat in SAFE_Q_PATTERNS:
        for m in re.finditer(pat, content):
            if m.start() <= pos < m.end():
                return True
    return False

fixed_count = 0
for path in files:
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        original = f.read()

    content = original
    for bad, good in deduped:
        content = content.replace(bad, good)

    # Count remaining suspicious ?
    remaining = len(re.findall(r"[A-Za-záéíóúãõâêîôûàüçÁÉÍÓÚÃÕÂÊÎÔÛÀÜÇ]{2,}\?|\?[A-Za-záéíóúãõâêîôûàüçÁÉÍÓÚÃÕÂÊÎÔÛÀÜÇ]{2,}|\?{2,}", content))

    rel = os.path.relpath(path, front_dir)
    if content != original:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(content)
        suffix = f" ({remaining} ? remaining)" if remaining else " [CLEAN]"
        print(f"FIXED: {rel}{suffix}")
        fixed_count += 1
    else:
        suffix = f" ({remaining} ?)" if remaining else " [CLEAN]"
        print(f"OK   : {rel}{suffix}")

print(f"\nDone. {fixed_count} file(s) updated.")
