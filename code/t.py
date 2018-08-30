import numpy as np 
#c = np.load("data/train_instance_triple.npy")
#print(c)
def check_multilabel():
    all_data = {}
    for line in open("../old_data_no_public/train.txt"):
        tmp = line.strip().split("\t")
        if "".join(tmp[0:4])+tmp[5] not in all_data:
            all_data["".join(tmp[0:4])+tmp[5]]=1
        else:
            all_data["".join(tmp[0:4])+tmp[5]]=1+all_data["".join(tmp[0:4])+tmp[5]]
    i = 0
    for key in all_data:
  
        if all_data[key]!=1:
            i=i+1
                #print(all_data[key])
    print(i)
def hold_triple_check():
    all_triples_train = {}
    all_triples_test = {}
    for line in open("../old_data_no_public/train.txt"):
        tmp = line.strip().split("\t")
        if "".join(tmp[0:2])+tmp[4] not in all_triples_train:
            all_triples_train["".join(tmp[0:2])+tmp[4]]=1
    for line in open("../old_data_no_public/test.txt"):
        tmp = line.strip().split("\t")
        if "".join(tmp[0:2])+tmp[4] not in all_triples_test:
            all_triples_test["".join(tmp[0:2])+tmp[4]]=1
    #print(all_triples_train)
    #print(all_triples_test)
    #dict3 = dict.fromkeys([x for x in all_triples_train if x in all_triples_test\
     #and all_triples_train[x]==all_triples_test[x]])
    inter = dict.fromkeys([x for x in all_triples_train if x in all_triples_test])
    print(inter)

def check_word():
    c = np.load("data/test_instance_scope.npy")  
    #print(len(c))
    #dd = np.load("data/test_instance_entity.npy")  
    print(c)
    #print(len(dd))
    


if __name__ =="__main__":
    #test()
    #hold_triple_check()
    check_word()