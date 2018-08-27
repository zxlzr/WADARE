# Dataset
You could download the dataset from . 

The dataset contains four files, including source_train.txt, source_valid.txt, source_test.txt, target_train.txt, target_valid.txt, target_test.txt, common_relation2id.txt. The structures of *_train.txt, *_valid.txt, *_test.txt are homogeneous. Each line in those files is a instance, containing a entity pair and a corresponding sentence. The first element in each line is the id of the head entity, and the second element is the id of the tail entity. The subsequent two elements are the name of head and tail entity respectively, and the fifth element is the relation type. The later part in each line is a sentence corresponding with this entity pair.

The common_relation2id.txt records the name of all relation types, each name resides in a line.

More statistics and details of this dataset are shown in the paper.  

