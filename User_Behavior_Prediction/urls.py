
from django.conf.urls import url
from django.contrib import admin
from Remote_User import views as remoteuser
from User_Behavior_Prediction import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$', remoteuser.login, name="login"),


    url(r'^Register1/$', remoteuser.Register1, name="Register1"),

    url(r'^Recommend/(?P<pk>\d+)/$', remoteuser.Recommend, name="Recommend"),
    url(r'^Review/(?P<pk>\d+)/$', remoteuser.Review, name="Review"),
    url(r'^View_All_Tweet_Details/$', remoteuser.View_All_Tweet_Details, name="View_All_Tweet_Details"),
    url(r'^View_Tweet_Reviews/$', remoteuser.View_Tweet_Reviews, name="View_Tweet_Reviews"),
    url(r'^ratings/(?P<pk>\d+)/$', remoteuser.ratings, name="ratings"),
    url(r'^dislikes/(?P<pk>\d+)/$', remoteuser.dislikes, name="dislikes"),
    url(r'^likes/(?P<pk>\d+)/$', remoteuser.likes, name="likes"),
    url(r'ViewTrending/$', remoteuser.ViewTrending, name="ViewTrending"),
    url(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    url(r'^View_Tweet_Recommends/$', remoteuser.View_Tweet_Recommends, name="View_Tweet_Recommends"),
    url(r'^Add_Tweets/$', remoteuser.Add_Tweets, name="Add_Tweets"),

    url(r'^serviceproviderlogin/$',serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    url(r'View_Remote_Users/$',serviceprovider.View_Remote_Users,name="View_Remote_Users"),
    url(r'ViewTrendings/$',serviceprovider.ViewTrendings,name="ViewTrendings"),
    url(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts,name="charts"),
    url(r'^dislikeschart/(?P<dislike_chart>\w+)', serviceprovider.dislikeschart,name="dislikeschart"),
    url(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart,name="likeschart"),

    url(r'^View_Tweet_Details/$',serviceprovider.View_Tweet_Details, name='View_Tweet_Details'),
    url(r'^View_Tweet_Details1/$',serviceprovider.View_Tweet_Details1, name='View_Tweet_Details1'),

    url(r'^viewallpostsreviews/$', serviceprovider.viewallpostsreviews, name='viewallpostsreviews'),
    url(r'^View_Recommended_Tweet/$', serviceprovider.View_Recommended_Tweet, name='View_Recommended_Tweet'),

     url(r'^Positive_Sentiments/$', serviceprovider.Positive_Sentiments, name="Positive_Sentiments"),
    url(r'^Negative_Sentiments/$', serviceprovider.Negative_Sentiments, name="Negative_Sentiments"),
    url(r'^Neutral_Sentiment/$', serviceprovider.Neutral_Sentiment, name="Neutral_Sentiment"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
