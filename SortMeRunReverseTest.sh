python3 SortMe.py -r >tmpFile.txt

if ! diff -w -b tmpFile.txt SortMeReverseAnswer.txt; then
    rm tmpFile.txt
    exit 2
fi
rm tmpFile.txt


