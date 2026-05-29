"""Final cleanup: fix all remaining U+FFFD chars identified by direct file inspection."""
import os, glob

front_dir = r"c:\Users\isaqu\OneDrive\Documentos\Front-End ICOL\front"
files = sorted(glob.glob(os.path.join(front_dir, "**", "*.html"), recursive=True))

F = "\ufffd"

# All remaining patterns found by reading the files
final_fixes = [
    # In coordenador/dashboard_coordenador_relatorios.html
    (f"decis{F}es",        "decisões"),
    (f"Conclus{F}o",       "Conclusão"),
    (f"conclus{F}o",       "conclusão"),
    (f"Evas{F}o",          "Evasão"),
    (f"evas{F}o",          "evasão"),
    (f"Matr{F}culas",      "Matrículas"),
    (f"matr{F}culas",      "matrículas"),
    
    # In responsavel/dashboard_responsavel_avisos.html
    (f"Comunica{F}{F}o",   "Comunicação"),
    (f"comunica{F}{F}o",   "comunicação"),
    (f"exerc{F}cio",       "exercício"),
    (f"Exerc{F}cio",       "Exercício"),
    (f"Plant{F}o",         "Plantão"),
    (f"plant{F}o",         "plantão"),
    (f"d{F}vidas",         "dúvidas"),
    (f"D{F}vidas",         "Dúvidas"),
    (f"S{F}bado",          "Sábado"),
    (f"s{F}bado",          "sábado"),
    (f"Laborat{F}rio",     "Laboratório"),
    (f"laborat{F}rio",     "laboratório"),
    (f"Atualiza{F}{F}o",   "Atualização"),
    (f"atualiza{F}{F}o",   "atualização"),
    (f"laborat{F}",        "laboratór"),    # partial guard
    
    # In professor/dashboard_professor_diario.html
    (f"Di{F}rio",          "Diário"),
    (f"di{F}rio",          "diário"),
    (f"freq{F}ência",      "frequência"),
    (f"Freq{F}ência",      "Frequência"),
    (f"aus{F}ncias",       "ausências"),
    (f"Aus{F}ncias",       "Ausências"),
    (f"presen{F}as",       "presenças"),
    (f"Presen{F}as",       "Presenças"),
    (f"ocorr{F}ncias",     "ocorrências"),
    (f"Ocorr{F}ncias",     "Ocorrências"),
    (f"anotaç{F}es",       "anotações"),
    (f"Anotaç{F}es",       "Anotações"),
    (f"Aula pratica",      "Aula prática"),
    (f"pratica",           "prática"),     # fallback
    (f"turm{F}s",          "turmas"),
    (f"T{F}pico",          "Tópico"),
    (f"t{F}pico",          "tópico"),
    (f"revis{F}o",         "revisão"),
    (f"Revis{F}o",         "Revisão"),
    
    # In responsavel/dashboard_responsavel_frequencia.html
    (f"justificad{F}",     "justificadas"),
    (f"Justificad{F}",     "Justificadas"),
    (f"n{F}o",             "não"),
    (f"N{F}o",             "Não"),
    
    # In professor/dashboard_professor_turmas.html
    (f"per{F}odo",         "período"),
    (f"Per{F}odo",         "Período"),
    (f"matr{F}cula",       "matrícula"),
    (f"Matr{F}cula",       "Matrícula"),
    
    # In responsavel/dashboard_responsavel.html
    (f"{F}??rea",          "Área"),   # BOM + rea
    
    # In professor/dashboard_professor_notas.html  
    (f"Avalia{F}{F}o",     "Avaliação"),
    (f"avalia{F}{F}o",     "avaliação"),
    (f"Observa{F}{F}o",    "Observação"),
    (f"evolu{F}{F}o",      "evolução"),
    
    # Theme icon (moon character ☾ was corrupted)
    (f"data-theme-icon aria-hidden=\"true\">{F}<",   
     "data-theme-icon aria-hidden=\"true\">☾<"),
    
    # Nav: Início, Gestão, Relatórios that are still corrupted
    (f">In{F}cio<",        ">Início<"),
    (f">Gest{F}o de Cursos<", ">Gestão de Cursos<"),
    (f">Relat{F}rios<",    ">Relatórios<"),
    (f">Informa{F}{F}o<",  ">Informação<"),
    
    # Generic but contextual
    (f"respons{F}vel",     "responsável"),
    (f"Respons{F}vel",     "Responsável"),
    
    # Final FFFD BOM artifact at start of file
]

fixed_count = 0
for path in files:
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        original = f.read()
    
    content = original
    # Strip leading FFFD
    while content.startswith(F):
        content = content[1:]
    
    for bad, good in final_fixes:
        content = content.replace(bad, good)
    
    remaining = content.count(F)
    rel = os.path.relpath(path, front_dir)
    
    if content != original:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(content)
        suffix = f" ({remaining} FFFD left)" if remaining > 0 else " [CLEAN]"
        print(f"FIXED: {rel}{suffix}")
        fixed_count += 1
    else:
        suffix = f" ({remaining} FFFD)" if remaining > 0 else " [CLEAN]"
        print(f"OK   : {rel}{suffix}")

print(f"\nDone. {fixed_count} file(s) updated.")
