
from django.db.models import  Count, Avg,Max
from django.shortcuts import render, redirect
from django.db.models import Count
import datetime


# Create your views here.
from Remote_User.models import productdetails_model,ClientRegister_Model,review_Model,recommend_Model


def serviceproviderlogin(request):
    if request.method  == "POST":
        admin = request.POST.get('username')
        password = request.POST.get('password')
        if admin == "SProvider" and password =="SProvider":
            return redirect('View_Tweet_Details')


    return render(request,'SProvider/serviceproviderlogin.html')



def viewtreandingquestions(request,chart_type):
    dd = {}
    pos,neu,neg =0,0,0
    poss=None
    topic = productdetails_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics=t['ratings']
        pos_count=productdetails_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss=pos_count
        for pp in pos_count:
            senti= pp['names']
            if senti == 'positive':
                pos= pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics]=[pos,neg,neu]
    return render(request,'SProvider/viewtreandingquestions.html',{'object':topic,'dd':dd,'chart_type':chart_type})

def Positive_Sentiments(request):

    rtype='Positive'
    #obj = review_Model.objects.all()

    obj = review_Model.objects.all().filter(sanalysis=rtype)

    return render(request,'SProvider/Positive_Sentiments.html',{'list_objects': obj})

def Negative_Sentiments(request):

    rtype='Negative'
    #obj = review_Model.objects.all()

    obj = review_Model.objects.all().filter(sanalysis=rtype)

    return render(request,'SProvider/Negative_Sentiments.html',{'list_objects': obj})

def Neutral_Sentiment(request):

    rtype='Neutral'
    #obj = review_Model.objects.all()

    obj = review_Model.objects.all().filter(sanalysis=rtype)

    return render(request,'SProvider/Neutral_Sentiment.html',{'list_objects': obj})


def View_Remote_Users(request):
    obj=ClientRegister_Model.objects.all()
    return render(request,'SProvider/View_Remote_Users.html',{'objects':obj})

def ViewTrendings(request):
    topic = productdetails_model.objects.values('topics').annotate(dcount=Count('topics')).order_by('-dcount')
    return  render(request,'SProvider/ViewTrendings.html',{'objects':topic})

def negativechart(request,chart_type):
    dd = {}
    pos, neu, neg = 0, 0, 0
    poss = None
    topic = productdetails_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics = t['ratings']
        pos_count = productdetails_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss = pos_count
        for pp in pos_count:
            senti = pp['names']
            if senti == 'positive':
                pos = pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics] = [pos, neg, neu]
    return render(request,'SProvider/negativechart.html',{'object':topic,'dd':dd,'chart_type':chart_type})


def charts(request,chart_type):
    chart1 = productdetails_model.objects.values('names').annotate(dcount=Avg('ratings'))
    return render(request,"SProvider/charts.html", {'form':chart1, 'chart_type':chart_type})

def dislikeschart(request,dislike_chart):
    charts = productdetails_model.objects.values('names').annotate(dcount=Avg('dislikes'))
    return render(request,"SProvider/dislikeschart.html", {'form':charts, 'dislike_chart':dislike_chart})

def likeschart(request,like_chart):
    charts = productdetails_model.objects.values('names').annotate(dcount=Avg('likes'))
    return render(request,"SProvider/likeschart.html", {'form':charts, 'like_chart':like_chart})

def View_Tweet_Details(request):
    obj = productdetails_model.objects.all()
    return render(request, 'SProvider/View_Tweet_Details.html', {'list_objects': obj})

def View_Tweet_Details1(request):
    obj=''
    if request.method == "POST":
     top = request.POST.get('stype')

     top1=int(top)
     obj = productdetails_model.objects.filter(likes__gt=top1)#aggregate(Max('likes'))

    return render(request, 'SProvider/View_Tweet_Details1.html', {'list_objects': obj})

def viewallpostsreviews(request):

        obj = review_Model.objects.all()

        return render(request, 'SProvider/Viewallpostsreviews.html', {'list_objects': obj})

def View_Recommended_Tweet(request):
    obj = recommend_Model.objects.all()

    return render(request, 'SProvider/View_Recommended_Tweet.html', {'list_objects': obj})

