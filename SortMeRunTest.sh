python3 SortMe.py >tmpFile.txt

if ! diff -q -w -b tmpFile.txt SortMeAnswer.txt; 
then
    echo "Sort Failed"
fi

rm tmpFile.txt
