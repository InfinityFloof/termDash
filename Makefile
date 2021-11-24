OUTDIR="bin"

all: convert cython_cvrt compile

convert:
	@echo ">>> Converting termDash.py"
	@if [ -d $(OUTDIR) ]; then \
		DIREXISTS=1; \
	else\
		mkdir $(OUTDIR);\
	fi
	@cat termDash.py | sed 's/print()/print(\"\")/g' > $(OUTDIR)/termDash.pyx

cython_cvrt:
	@echo ">>> Converting to C via Cython"
	@cython --embed $(OUTDIR)/termDash.pyx

compile:
	@echo ">>> Compiling"
	@gcc -O2 -I /usr/include/python3.9 -o termDash $(OUTDIR)/termDash.c -lpython3.9 -lpthread -lm -lutil -ldl

clean:
	@rm -rvf $(OUTDIR) termDash