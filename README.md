# cv
My CV and tools to generate it in nice formats


## Prerequisits
I use `make`, which keeps track of when either the `template.tex` or `.yaml` files are recently altered.

The recipes in the `Makefile` expect the following to be installed:
  - `pandoc`
  - `pdflatex`


## Usage
Update the `{name}.yaml` file, and make sure the `Makefile` has the filename set in the right variable. Then, simply run

```bash
$ make
```

And the CV will be generated in all sorts of formats.


## License
MIT
