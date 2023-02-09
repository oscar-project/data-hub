# HinDialect 1.1

Download: `curl --remote-name-all https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-4839/HinDialect%201.1.zip`

From [north-indian-dialect-modelling](https://github.com/niyatibafna/north-indian-dialect-modelling), by @niyatibafna.


The script will download and unzip the corpus, and the convert.py will go from <langname>-<tag>.txt to standard/<bcp47tag>.txt, using `x-tag` for unknown tags.

## Format

The dataset contains a single text file containing folksongs per language. Folksongs are separated from each other by an empty line. The first line of a new piece is the title of the folksong, and line separation within folksongs is preserved.
