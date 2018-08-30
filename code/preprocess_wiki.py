# -*- coding: utf-8 -*- 
import json
file_list = ["held-out", "training", "validation"]
for file in file_list:
    with open("origin_data/semantic-graphs-filtered-"+file+".02_06.json") as f:
        wikidata_corpus = json.load(f)
    f_out = open("origin_data/filterer-"+file+".txt", 'w')
    for wikidata in wikidata_corpus:
        edgeset = wikidata['edgeSet']
        vertexset = wikidata['vertexSet']
        if len(edgeset) == 1:
            continue
        temp = wikidata
        edgeSet = temp['edgeSet']
        merge_word = {}
        for edge in edgeSet:
            if len(edge['left']) > 1 and edge['left'][0] not in merge_word :
                merge_word[edge['left'][0]] = (edge['left'])
            if len(edge['right']) > 1 and edge['right'][0] not in merge_word :
                merge_word[edge['right'][0]] = (edge['right'])
        tokens = temp['tokens']
        sentence = str()
        i=0
        while i < len(tokens):
            if i in merge_word:
                entity_pos = merge_word[i]
                entity_word = str()
                for pos in entity_pos:
                    entity_word += tokens[pos] + "_"
                i += len(entity_pos)
                entity_word = entity_word[:-1]
                sentence += entity_word + " "
            else:
                sentence += tokens[i] + " "
                i += 1
        for i in range(len(edgeSet)):
            edge = edgeSet[i]

            left_pos = edge['left']
            right_pos = edge['right']
            e1 = ""
            e2 = ""
            for vertex in vertexset:
                #print(vertex['kbID'])
                #print(vertex['tokenpositions'])
                if left_pos == vertex['tokenpositions']:
                    e1 = vertex['kbID']
                elif right_pos == vertex['tokenpositions']:
                    e2 = vertex['kbID']
                #print(e1)
                #print(e2)
            #exit(1)
            left_entity = str()
            right_entity = str()
            for j in left_pos:
                left_entity += tokens[j]+"_"
            left_entity = left_entity[:-1]
            for j in right_pos:
                right_entity += tokens[j]+"_"
            right_entity = right_entity[:-1]
            if left_entity.strip()!='' and right_entity.strip()!='':
                f_out.write(e1+'\t'+e2+'\t'+left_entity +'\t'+right_entity +'\t'+edge['kbID']+'\t'+ sentence+'\n')
            else:
                continue
                #print("error")