python3 SortMe.py -r >tmpFile.txt

if diff -q -w -b tmpFile.txt SortMeReverseAnswer.txt; then
    echo "Sort was correct."
else
    echo "Sort failed."
fi
rm tmpFile.txt
read -p "Execution complete."

