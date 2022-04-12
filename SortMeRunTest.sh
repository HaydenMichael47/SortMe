python3 SortMe.py >tmpFile.txt

if ! diff -w -b tmpFile.txt SortMeAnswer.txt; 
then
    rm tmpFile.txt
    exit 2
fi

rm tmpFile.txt
read -p "Execution complete."