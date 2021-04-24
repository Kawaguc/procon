snippet_file=python.snippets
for pyfile in `ls *.py`;do
    filename_noext=`basename $pyfile .py`
    echo snippet ${filename_noext} [${filename_noext}] >> $snippet_file
    cat $pyfile >> $snippet_file
    echo endsnippet >> $snippet_file
done
