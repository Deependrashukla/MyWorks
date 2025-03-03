start=$(date +%s)
myvar=hello
name=sitare


sleep 5

echo $myvar $name

end=$(date +%s)

echo "Time required is: $((end-start)) seconds"
