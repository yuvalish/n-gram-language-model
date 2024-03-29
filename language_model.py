from urllib.request import urlopen
import string

class CorpusReader():
    def CorpusReader(link):
        file = ((urlopen(link)).read()).decode()
        file = file.replace("\r","")
        file = file.replace("“","\"")
        file = file.replace("”","\"")
        out=""
        side_lst = [".",",",":","#","(",")","!","?"," ","\n","\'","\""]
        for i in range(len(file)):
            c = file[i]
            if((c>="a" and c<="z")or (c>="A" and c<="Z") or(c in side_lst)):
                out+=c          
        out = out.lower()
        return out

class LanguageModel():
    def __init__(self,corpus):
        t = LanguageModel.prob(corpus)
        self.unigram = t[0]
        self.bigram = t[1]      

    def prob(corpus):
        corp_len = len(corpus)
        lex_len = 38
        unigram_d = {}
        bigram_d = {} #p = P(x(i+1)=w2/xi=w1), in the dic (w2,w1):p
        bigram_d_count = {}
        lst = list(string.ascii_lowercase)
        lst += [".",",",":","#","(",")","!","?"," ","\n","\'","\""]
        for c1 in lst:
            unigram_d[c1]=1 #laplace
            for c2 in lst:
                bigram_d_count[(c1,c2)]=1 #laplace
                bigram_d[(c1,c2)]=0
        for i in range(corp_len):
            unigram_d[corpus[i]]+=1
            if(i<corp_len-1):
                bigram_d_count[(corpus[i],corpus[i+1])]+=1
        count_d = unigram_d.copy()
        for c1 in lst:
            unigram_d[c1] = unigram_d[c1]/(corp_len+lex_len)
            for c2 in lst:
                bigram_d[(c1,c2)] = (bigram_d_count[(c2,c1)])/(lex_len+count_d[c2]-1)
        return(unigram_d,bigram_d)
