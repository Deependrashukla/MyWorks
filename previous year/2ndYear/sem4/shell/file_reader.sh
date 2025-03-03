for file in /home/deependra/Documents/ajava/shell/*
do 
	echo "file or folder name with path : $file"
	echo "only file name : $(basename $file)"
	sleep 2
done
