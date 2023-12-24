from django.shortcuts import render
import datetime
# Create your views here.
def view(request):
    d={'name': 'Rahim','age':20,'lst':['I','love','py thon','very','much','thanks'],
       'course':[
        {
          'id':1,
          'name':'python',
          'fee':500 
       },
        {
          'id':2,
          'name':'Java',
          'fee':400 
       },
        {
          'id':3,
          'name':'Javascript',
          'fee':200 
       },
        {
          'id':4,
          'name':'c++',
          'fee':300 
       }
       ],'num':4,'birthday':datetime.datetime.now(),'about':'my name is Sultan','time':datetime.datetime.now(),
      'blog': datetime.datetime(2023, 1, 2, 9, 30, 0, 123000),'num_tomato':2

       }
    d['can_drive']=d['age']>=20
    d['is_teenager']=13<=d['age']<20
    d['is_child']=8<=d['age']<13

    return render(request, 'first_app/index.html',d)