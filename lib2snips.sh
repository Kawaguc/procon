snippet_file_to_update=python.snippets
if [ -e $snippet_file_to_update ]; then
    rm $snippet_file_to_update
fi
touch $snippet_file_to_update
modules_dir='./procon'
for pyfile in `ls ${modules_dir}/*.py`;do
    filename_noext=`basename $pyfile .py`
    echo $filename_noext
    echo snippet ${filename_noext} [${filename_noext}] >> $snippet_file_to_update
    cat $pyfile >> $snippet_file_to_update
    echo endsnippet >> $snippet_file_to_update
done
