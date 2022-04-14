num=[35,10,20,40,90,45]
print('최솟값   :'+str(min(num)))
print('최댓값   :'+str(max(num)))
sum=0
for k in num :
    sum=sum+k
print('총합     :' + str(sum))
print('평균     :'+str(sum/len(num)))    
