#Note: Pass the blogposts dir as the argument
from post_reader import readPosts
from nltk.tree import Tree
from corenlp_client import StanfordNLP
import os
import sys

nlp = StanfordNLP()

def getTrees(post):
    result = nlp.parse(post)
    trees = []
    for sent in result['sentences']:
        trees.append(sent['parsetree'])
    return trees

blog_dir = sys.argv[1] #"blogs/sample_blogs"
treebanks_dir = "treebanks"
postsmap = readPosts(blog_dir, 0)
treebank = open(treebanks_dir + "/" + os.path.basename(blog_dir) + ".tb", "w")

for post in postsmap[0]:
    for tree in getTrees(post):
        treebank.write(str(tree) + "\n")

