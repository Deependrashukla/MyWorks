a=0

while [ $a -lt 10 ]
do 
	echo $a
	#a=`expr $a + 1`
	a=$((a+1))
done


sleep 2


for var in 0 1 2 3 4 5 6 7 8 9
do 
	echo $var

done


sleep 2
#another method for for loop


max=10

for i in `seq 1 $max`
do 
	echo $i
done

sleep 2
#method 3 

for i in `seq 1 2 $max`
do 
	echo $i
done
