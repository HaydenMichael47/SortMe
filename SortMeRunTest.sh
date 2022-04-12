python3 SortMe.py >tmpFile.txt

if diff -q -w -b tmpFile.txt SortMeAnswer.txt; 
then
    echo "Sort was correct"
else
    echo "Sort failed"
fi

rm tmpFile.txt
read -p "Execution complete."