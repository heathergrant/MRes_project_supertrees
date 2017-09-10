TEXFILEROOT = flies_tree_of_supertree_qd
PDFVIEWER=open


# For debugging, remove the '> /dev/null' bit, so you can see the error messages!
pdf: $(TEXFILEROOT).tex
	pdflatex $(TEXFILEROOT).tex > /dev/null
	$(PDFVIEWER) $(TEXFILEROOT).pdf &

pdfPage: $(TEXFILEROOT).tex
	pdflatex $(TEXFILEROOT).tex > /dev/null
	$(PDFVIEWER) $(TEXFILEROOT).pdf

clean:
	rm -f $(TEXFILEROOT).aux  $(TEXFILEROOT).log

