cat data/*.bed | sort -k1,1 -k2,2n | bedtools merge   >  infinity_merge.bed
for file in $(ls ./data)
do
	echo $(wc -l data/$file)
	if [ $(wc -l <data/$file) -ge 50 ]
	then
		bedtools intersect  -a infinity_merge.bed -b  data/$file  >  infinity_merge.bed
	else
		echo "Skipping $file"
	fi
	echo $(wc -l infinity_merge.bed)
done
