
def test():
	
    '''
    for line in open("origin_data/wiki_all.txt"):
    	tmp = line.strip().split("    ")[2]
    	wiki_relations.add(tmp)
    '''
    with open("origin_data/nyt_relation2wiki_id.txt",'w') as out:

        all_wikidata_relations = {}
        nyt_relation = set()
        for line in open("origin_data/wikidata_relation2id.txt"):
            tmp = line.strip().split("\t")
            all_wikidata_relations['_'.join(tmp[0].split(" "))] = tmp[1]
        for line in open("origin_data/nyt/relation2id.txt"):
            tmp = line.strip().split("\t")[0]
            if tmp in all_wikidata_relations:
                val = all_wikidata_relations[tmp]
                out.write(tmp+"\t"+val+"\n")
def test_wiki():
    with open("origin_data/wiki_relation2wiki_id.txt",'w') as out:

        all_wikidata_relations = {}
        nyt_relation = set()
        for line in open("origin_data/wikidata_relation2id.txt"):
            tmp = line.strip().split("\t")
            all_wikidata_relations['P'+tmp[1]] = ['_'.join(tmp[0].split("\t")),tmp[1]]
        i = 0
        exits_relations = set()
        for line in open("origin_data/wiki_all.txt"):
            tmp = line.strip().split("\t")[2]
            #print(tmp)
            #print(str(i))
            #i = i+1
            if tmp in all_wikidata_relations and tmp not in exits_relations:
                exits_relations.add(tmp)
                val = all_wikidata_relations[tmp]
                out.write(val[0]+"\t"+val[1]+"\n")

def test_joint():
    with open("common_relations.txt", 'w'): 
        for line in  open("origin_data/wikidata_relation2id"):
           pass
        for line in  open("origin_data/nyt_relation2wiki_id.txt"):
           pass
def create_dataset():
    wiki_relation2id = {}
    for line in open("origin_data/wikidata_relation2id.txt"):
        if line.strip().split("\t")[1] not in wiki_relation2id:
            wiki_relation2id['P'+line.strip().split("\t")[1]] = \
            "_".join(line.strip().split("\t")[0].split(" "))
    wiki_relation2id['P0'] = 'NA'
    wiki_relation2id['P2416'] = 'sports_discipline_competed'
    wiki_relation2id['P1589'] = 'deepest_point'
    wiki_relation2id['P2079'] = 'fabrication_method'
    wiki_relation2id['P1582'] = 'natural_product_of_taxon'


    common_relation2id = {}
    
    for line in open("origin_data/common_relation.txt"):
        tmp = line.strip().split("\t")
        if len(tmp) == 1:
            continue
        #print(tmp)
        common_relation2id[tmp[0]] = tmp[1]
        #id2relation['P'+tmp[1]] = tmp[0]

    with open("origin_data/source_train.txt", 'w') as out1,\
     open("origin_data/source_test.txt", 'w') as out2,\
     open("origin_data/source_valid.txt", 'w') as out3:
        for line in open("origin_data/filterer-training.txt"):
            tmp = line.strip().split('\t')
            if line.strip().split("\t")[4] in wiki_relation2id:
                if wiki_relation2id[line.strip().split("\t")[4]] in common_relation2id:
            #line.strip().split("\t")[4] in id2relation:
                    out1.write(tmp[0]+"\t"+tmp[1]+"\t"+tmp[2]+"\t"+tmp[3]+"\t"+wiki_relation2id[line.strip().split("\t")[4]]\
                    +"\t"+tmp[5]+'\n')
        for line in open("origin_data/filterer-held-out.txt"):
            tmp = line.strip().split('\t')
            if line.strip().split("\t")[4] in wiki_relation2id:            
                if wiki_relation2id[line.strip().split("\t")[4]] in common_relation2id:
                    out2.write(tmp[0]+"\t"+tmp[1]+"\t"+tmp[2]+"\t"+tmp[3]+"\t"+wiki_relation2id[line.strip().split("\t")[4]]\
                    +"\t"+tmp[5]+'\n')
        for line in open("origin_data/filterer-validation.txt"):
            tmp = line.strip().split('\t')
            if line.strip().split("\t")[4] in wiki_relation2id:
                if wiki_relation2id[line.strip().split("\t")[4]] in common_relation2id:
                    out3.write(tmp[0]+"\t"+tmp[1]+"\t"+tmp[2]+"\t"+tmp[3]+"\t"+wiki_relation2id[line.strip().split("\t")[4]]\
                    +"\t"+tmp[5]+'\n')
    with open("origin_data/target_train.txt", 'w') as out4,\
     open("origin_data/target_test.txt", 'w') as out5,\
     open("origin_data/target_valid.txt", 'w') as out6:
        for line in open("origin_data/nyt/train.txt"):
            if line.strip().split("\t")[4] in common_relation2id:
            #line.strip().split("\t")[4] in id2relation:
                out4.write(line)
        for line in open("origin_data/nyt/test.txt"):
            if line.strip().split("\t")[4] in common_relation2id:
                out5.write(line)
        for line in open("origin_data/nyt/valid.txt"):
            if line.strip().split("\t")[4] in common_relation2id:
                out6.write(line)
def create_common():
    source_train = set()
    source_valid = set()
    source_test = set()
    target_train = set()
    target_test = set()
    target_valid = set()
    wiki_relation2id = {}
    for line in open("origin_data/wikidata_relation2id.txt"):
        if line.strip().split("\t")[1] not in wiki_relation2id:
            wiki_relation2id['P'+line.strip().split("\t")[1]] = \
            "_".join(line.strip().split("\t")[0].split(" "))
    wiki_relation2id['P0'] = 'NA'
    wiki_relation2id['P2416'] = 'sports_discipline_competed'
    wiki_relation2id['P1589'] = 'deepest_point'
    wiki_relation2id['P2079'] = 'fabrication_method'
    wiki_relation2id['P1582'] = 'natural_product_of_taxon'
    #organisation directed from the office
    
    
    
    #print(wiki_relation2id)
    for line in open("origin_data/filterer-training.txt"):
        if line.strip().split("\t")[4] not in source_train:
            if line.strip().split("\t")[4] in wiki_relation2id:
                source_train.add(wiki_relation2id[line.strip().split("\t")[4]])
    for line in open("origin_data/filterer-validation.txt"):
        if line.strip().split("\t")[4] not in source_valid:
            if line.strip().split("\t")[4] in wiki_relation2id:
                source_valid.add(wiki_relation2id[line.strip().split("\t")[4]])
    for line in open("origin_data/filterer-held-out.txt"):
        if line.strip().split("\t")[4] not in source_test:
            if line.strip().split("\t")[4] in wiki_relation2id:
                source_test.add(wiki_relation2id[line.strip().split("\t")[4]])


    for line in open("origin_data/nyt/train.txt"):
        if line.strip().split("\t")[4] not in target_train:
            target_train.add(line.strip().split("\t")[4])
    for line in open("origin_data/nyt/valid.txt"):
        if line.strip().split("\t")[4] not in target_valid:
            target_valid.add(line.strip().split("\t")[4])
    for line in open("origin_data/nyt/test.txt"):
        if line.strip().split("\t")[4] not in target_test:
            target_test.add(line.strip().split("\t")[4])


    source = source_train & source_valid & source_test
    #print(len(source))
    #print(source)
    target = target_train & target_valid & target_test
    #print(len(target))
    #print(target)
    common = source & target 
    print(common)
    print(len(common))
    with open("common_relation.txt",'w') as out:
        id = 0
        out.write(str(len(common))+"\n")
        for relation  in common:
            out.write(relation+"\t"+str(id)+"\t"+"\n")
            id = id + 1

    #print(target)




'''
    with open("origin_data/source_wikipedia.txt", 'w') as out2:
        for line in open("origin_data/wiki_all.txt"):
            tmp = line.strip().split("\t")
            if tmp[4] in id2relation:
                out2.write(tmp[0]+"\t"+tmp[1]+"\t"+tmp[2]+"\t"+tmp[3]+"\t"+\
                id2relation[tmp[4]]+"\t"+tmp[5]+"\n")
'''
def create_common_relation2id():
    with open("origin_data/common_relation2id.txt",'w') as out:
        out.write("80\n")
        #out.write("NA\t0\n")
        i = 1
        for line in open("origin_data/common.txt"):
            out.write(line.strip().split("\t")[0]+"\t"+str(i)+"\n")
            i = i+1
def create_triple():
    source_triple = {}
    target_triple = {}
    for line in open("origin_data/source_wikipedia.txt"):
        t = line.strip().split('\t')
        if t[0]+'#'+t[1]+'#'+t[4] not in source_triple:
            source_triple[t[0]+'#'+t[1]+'#'+t[4]]=1
        else:
            source_triple[t[0]+'#'+t[1]+'#'+t[4]]=source_triple[t[0]+'#'+t[1]+'#'+t[4]]+1
    with open("origin_data/source_triple.txt", 'w') as out :
        for key in source_triple:
            #print(key)
            out.write(key)
    for line in open("origin_data/target_nyt.txt"):
        t = line.strip().split('\t')
        if t[0]+'#'+t[1]+'#'+t[4] not in source_triple:
            source_triple[t[0]+'#'+t[1]+'#'+t[4]]=1
        else:
            source_triple[t[0]+'#'+t[1]+'#'+t[4]]=source_triple[t[0]+'#'+t[1]+'#'+t[4]]+1
    with open("origin_data/target_triple.txt", 'w') as out :
        for key in source_triple:
            #print(key)
            out.write(key+'\n')


def check_classes():
    category = {}

    for line in open("origin_data/target_test.txt"):
        if line.strip().split('\t')[4] not in category:
           category[line.strip().split('\t')[4]] =1
    print(len(category))

       
   
    


if __name__ == "__main__":
    #check_classes()
    #create_dataset()
    create_dataset()
    #create_common()
    #create_common_relation2id()
    #create_triple()