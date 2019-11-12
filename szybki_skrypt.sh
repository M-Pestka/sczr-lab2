
for i in 1 3
do
	for time in 250000 500000 1000000 2000000 4000000 8000000 16000000
	do
		name=folder_${i}_${time}
		mkdir $name
		cd $name
		# i - liczba klientow
		# 500 - liczba probek
		# 10000 - czas probkowania
		# time - czas przetwarzania 
		../../cw2a $i 100 5000 $time
		cd ..
	done
done
python3 szybki_python.py --output test3.csv


