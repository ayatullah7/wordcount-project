import operator
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')


def count(request):
    text=request.GET['fulltext']
    wordlist=text.split()
    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word]=1
    sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'text':text,'number':len(wordlist),'sortedwords':sortedwords})
