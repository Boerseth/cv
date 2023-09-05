YAML = frode-thorsen-boerseth.yaml
TEMPLATE = template.tex

FORMATS = markdown_strict html
TARGETS = $(FORMATS:%=cv.%)

all: cv.pdf $(TARGETS)

cv.tex: $(YAML) $(TEMPLATE)
	echo "" | pandoc -t latex --metadata-file=$(word 1, $^) --template=$(word 2, $^) --wrap=preserve > $@

cv.pdf: cv.tex
	mkdir -p .temp
	pdflatex -quiet -output-directory .temp $< > /dev/null 2>&1
	mv .temp/$@ ./$@
	rm -rf .temp

$(TARGETS): cv.%: cv.tex
	pandoc -f latex -t $* $< > $@
