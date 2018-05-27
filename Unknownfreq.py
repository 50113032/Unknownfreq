
# coding: utf-8

# In[1]:


#kyoto-test.mrph.ja>形態素をリストtestlistに変換

file1=open('kyoto-test.mrph.ja.txt','r',encoding='utf-8')
file2=open('kyoto-train.voc20k.ja.txt','r',encoding='utf-8')

testlist=[]
for i in file1:
    if 'EOS'in i:
        continue
    j=i.split()
    testlist.append(j[0])
    
#kyoto-train.voc20k.ja>連想配列voctableに格納

voctable={}
for i in file2:
    j=i.split()
    voctable[j[1]]=int(j[0])

#未知語をリストunkに格納、未知語数と異なり未知語数を出力
    
unk=[]
for i in testlist:
    if i in voctable.keys():
        continue
    else:
        unk.append(i)
print('未知語数=',len(unk))
print('異なり未知語数=',len(set(unk)))
print('未知語率=',len(set(unk))/len(testlist)*100,'%')

file1.close()
file2.close()

