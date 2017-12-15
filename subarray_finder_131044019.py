################################################################################
# Gozde DOGAN
# 131044019
# CSE321 - Introduction to Algorithm Design
# Homework 4
# Question 1
################################################################################

################################################################################
#
# Metodlarin uzerinde yorum bloklari icinde neler yaptiklari ve karmasikliklari 
# ayrintili olarak anlatildi.
# min_subarray_finder metodunun karmasikligi n olarak bulundu.
# Tasarlanan algoritmanin karmasikligi lineer zaman'dir.
#
################################################################################

import sys

def main():
################################################################################
    print "\n"
    arr = [1, -4, -7, 5, -13, 9, 23, -1]
    msa = min_subarray_finder(arr)
    #print "arr:", arr
    print "msa:", msa
    print "sum msa:", sum(msa)
    print "\n"

################################################################################
#    arr = [23, -1, 15, -13]
#    msa = min_subarray_finder(arr)
#    print "arr:", arr
#    print "msa:", msa
#    print "sum msa:", sum(msa)
#    print "\n"
    
################################################################################
#    arr = [1, -4, -7, 5, -7, -13, 9, 23, -1, 15, -13]
#    msa = min_subarray_finder(arr)
#    print "arr:", arr
#    print "msa:", msa
#    print "sum msa:", sum(msa)
#    print "\n"

################################################################################
#
# findSubArrayMinSum metodunun cagirir.
# findSubArrayMinSum metodunun karmasikligi n oldugu icin;
# min_subarray_finder metodunun karmasikligi n olarak bulunur. 
#
################################################################################
def min_subarray_finder(arr):
    msa = []
    #print "msa:", msa
    #print "sum msa:" , sum(msa)
    msa.append(min(arr)) #array de negatif eleman yoksa sum 0 olur, 
                         #hicbir eleman eklenemez.
    msa = findSubArrayMinSum(arr, msa)
    msa.pop(0) #sum'in ilk degeri icin eklenen eleman geri cikartiliyor
    return msa

################################################################################
#
# Best case'de lineer zamandir.
# Worst case'de left ve right arrayler icin metot recursive olarak cagrilir.
# Bu islem logn'dir.
# merge metodu ise r+l oldugu icin;
# Sistem karmasikligi logn+r+l olarak bulunur. 
# r ve l yi n/2 seklinde dusunursek karmasiklik logn + n
# Burdan da karmasiklik n yani lineer zaman olarak bulunur.
#
################################################################################
def findSubArrayMinSum(arr, msa):
    if len(arr) == 1:
        if sum(msa) > sum(msa)+arr[0]:
            msa.append(arr[0]);
        return msa
            
    elif len(arr)>1:
        middle = (len(arr)+1)/2
        LeftArr = arr[:middle]
        RightArr = arr[middle:len(arr)]
        
        #print "leftArr:", LeftArr, "\trightArr:", RightArr
        left_msa = findSubArrayMinSum(LeftArr, msa)
        right_msa = findSubArrayMinSum(RightArr, msa)
        #print "msa:", msa
        return merge(left_msa, right_msa, msa)
        

################################################################################
#
# Left ve Right arraylerdeki elemanlar eger sub array'in elemanli toplamini 
# kucuk yapiyorsa eklenir.
#
# Sistem best case de LeftArr ve RightArr 2 elemanli olabilir. 
# Burdan da best case'in linner zaman oldugu gorulur.
# Worst case de ise donguler her sekilde eleman sayisi kadar doner
# Burdan da sistemin karmasikligi worst case'de r+l'dir.
# (LeftArr'in boyutu l, RightArr'in boyutu r kabul edildi.)
#
################################################################################
def merge(LeftArr, RightArr, msa):
    sumArr = sum(msa)
          
    #print "MSA:", "\tLeft:", LeftArr, "\tRight:", RightArr
    while not LeftArr:
        leftElm = LeftArr.pop(0)
        if sumArr > sumArr + leftElm and leftElm is not msa:
            msa.append(leftElm);
            sumArr += leftElm
        
    while not RightArr:
        rightElm = RightArr.pop(0)
        if sumArr > sumArr + rightElm and rightElm is not msa:
            msa.append(rightElm);
            sumArr += rightElm
            
    #print "merge:", msa
    return msa


if __name__ == "__main__":
    main()
