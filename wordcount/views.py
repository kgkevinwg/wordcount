from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html',{'test':'your word counter'})

def about(request):
    return render(request,'about.html')

def count(request):
    print("Request: ", request)
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    wordDictionary = {}

    for word in wordlist:
        if word not in wordDictionary:
            wordDictionary[word] = 1
        else:
            wordDictionary[word]+=1

    
    sortedwords = sorted(wordDictionary.items(),key=operator.itemgetter(0),reverse=True)
    return render(request,'count.html',{'ft' : fulltext,'count':len(wordlist),'wdict':sortedwords})
