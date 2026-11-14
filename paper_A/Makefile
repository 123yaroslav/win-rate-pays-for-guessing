# Builds main.pdf.
#   make            latexmk with pdfLaTeX and BibTeX
#   make tectonic   same document built with tectonic
#   make todo       list the placeholders that are still unfilled
#   make clean      remove build files, keep main.pdf

LATEXMK  ?= latexmk
TECTONIC ?= tectonic

.PHONY: all tectonic todo clean

all: main.pdf

main.pdf: main.tex refs.bib $(wildcard figs/*)
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error main.tex

tectonic:
	$(TECTONIC) main.tex

todo:
	@grep -n "TODO" main.tex refs.bib | grep -v -E "^[^:]+:[0-9]+:[[:space:]]*%" || echo "no TODO left"

clean:
	$(LATEXMK) -c main.tex
	rm -f main.bbl
