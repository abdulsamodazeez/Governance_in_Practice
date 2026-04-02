# DSA 2026 paper submission (filled)

This folder contains the **filled** paper using the DSA 2026 LaTeX template. The **original template** is unchanged in `../Latex_template_DSA_2026/`.

## Files

- `main.tex` — Paper content (governance schema, five datasets, tool)
- `references.bib` — Bibliography
- `dsa2026.sty` — Copy of template style (so this folder compiles standalone)

## Compile

From this folder:

```bash
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

Or upload this folder to Overleaf and set `main.tex` as the main document.

## Tool screenshots

The paper includes two screenshots of the Streamlit tool (\texttt{tool\_screenshot\_browse.png} and \texttt{tool\_screenshot\_form.png}) in one figure in the Schema Design section.

## Before submission

1. Replace author names, affiliations, and emails in `main.tex` (email is already set to Abdulsamod2@gmail.com).
2. Add acknowledgments if needed.
3. Check page count (max 5 pages including references).
