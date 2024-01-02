# Dear Fellow Code Explorer,

# When I conjured this incantation in code,
# only I and the programming deities comprehended its essence.
# Now, only the divine compiler holds the secret!

# If you've dared to 'optimize' this enchantment
# and met with futility,
# kindly elevate the ensuing tally
# as an enigmatic prophecy
# for the next brave soul:

# HOURS SPENT HERE = 48

# Reflect upon this comment with a glimmer in your eye and a chuckle in your heart! 🚀🧙‍♂️🤣

from django.http import HttpResponse
from django.shortcuts import render,redirect
import random
import datetime as dt
import os 
import random
from .forms import submit_form
from django.views.decorators.csrf import csrf_exempt

def random1(request):    # Random calender
    weeks = ['', 'Mon', '', 'Wed', '', 'Fri', '']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    year = dt.datetime.now().year
    days =  make_calender(year-1) 
    list1 =[]
    for i in range(0,371,1):
        rand=  random.randint(0,4)
        if rand ==1:
            list1.append([days[i][0],"rgb(209, 255, 200)",days[i][1]])
        elif rand ==2:
            list1.append([days[i][0],"rgb(176, 255, 161)",days[i][1]])
        elif rand>2:
            list1.append([days[i][0],"hsl(110, 100%, 70%)",days[i][1]])
        else:
            list1.append([days[i][0],"rgb(220, 220, 220)",days[i][1]])
    return render(request,'index.html',{"param1":weeks,"param2":months,"param3":list1})

def home(request,file):
    weeks = ['', 'Mon', '', 'Wed', '', 'Fri', '']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    list1 = git_calender_prep(file)
    String1 = "<br>Contributions : "
    String2 = "Github Contributions"
    String3 ="Learn how we count contribution"
    return render(request,'myapp/home.html',{"param1":weeks,"param2":months,"param3":list1,"param4":String1,"param5":String2,"param6":String3})

def make_calender(year):
    from datetime import date, timedelta,datetime
    start_date = datetime(year-1, 12, 31) -timedelta(days=(datetime(year-1, 12, 31).weekday()- 6) % 7)
    day = []
    combine =[]
    months =['Jan','Feb','Mar','Apr','May',"Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']
    for i in range(372): # this for 53 weeks *7 days
        day.append(start_date+timedelta(i))
    for d in day:
        combine.append([str(d.day)+"-"+months[d.month-1]+"-"+str(d.year),weeks[d.weekday()]])
    return combine

def git_calender_prep(file):
    content = make_calender(year = dt.datetime.now().year-1)
    list1 =[]
    list2 =[]
    dates =[]
    commit=[]
    final_list=[]
    file1 = os.path.join('myapp/templates/myapp',file)
    with open(file1,'r') as f:
        list1=f.read().split('\n')
    for l in list1:
        if not l.strip() or len(l.split(','))<2:
            continue
        list2 = l.replace("\n","").split(",")
        dates.append(list2[0])
        commit.append(list2[1])
    for c1 in content:
        e= c1[0]
        if e in dates:
            if int(commit[dates.index(e)]) ==1:
                final_list.append([c1[0],"#9BE9AB",c1[1],commit[dates.index(e)]])
            elif int(commit[dates.index(e)]) ==2:
                final_list.append([c1[0],"#40C463",c1[1],commit[dates.index(e)]])
            elif int(commit[dates.index(e)]) >2:
                final_list.append([c1[0],"#30A14E",c1[1],commit[dates.index(e)]])
            else:
                final_list.append([c1[0],"#216E39",c1[1],0])
        else :
            final_list.append([c1[0],"#EBEDF0",c1[1],0])
    return final_list

@csrf_exempt
def form_input(request):
    if request.method == "POST":
        form = submit_form(request.POST,request.FILES)
        if form.is_valid():
            a= dt.datetime.now().strftime("%Y%m%d%H%M%S") # added datetime timestamp for file name
            data = form.cleaned_data
            file =data.get('input_file')
            with open(os.path.join('myapp/templates/myapp',f'{a}{file.name}'),'wb+') as f:
                f.write(file.read())
            return redirect('home',os.path.basename(os.path.join('myapp/templates/myapp',f'{a}{file.name}')))
    else:
        form =submit_form()
    return render(request,'myapp/index.html',{"form":form})

def stxt(request):
    file_path = 'myapp/templates/myapp/GitHubActivity_4MW21AD043.txt'
    with open(file_path, 'rb') as f1:
        response = HttpResponse(f1.read(), content_type='text/html')  
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
    return response 