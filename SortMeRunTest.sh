python3 SortMe.py >tmpFile.txt

if diff tmpFile.txt SortMeAnswer.txt; then
    echo "Sort was correct."
else
    echo "sort failed."
fi
rm tmpFile.txt
read -p "Execution complete."