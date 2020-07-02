from django.shortcuts import render
from app.models import signInDetails,group,bill
# Create your views here.
def show(request):

    return render(request,"index.html")


def login(request):
    return render(request, "signup.html")


def save(request):
    name=request.POST.get("name")
    email=request.POST.get("email")
    password=request.POST.get("pwd")
    qs=signInDetails.objects.filter(email=email)
    if qs.count() ==0:
        res=signInDetails(name=name,email=email,password=password)
        res.save()
        return render(request,"login.html",{"msg":"account created suussfully"})
    else:
        return render(request,"signup.html",{"msg":"account is there with this email already"})


def check(request):
    email=request.POST.get("email")
    password=request.POST.get("pwd")
    res=signInDetails.objects.filter(email=email,password=password)
    if res.count()!=0:
        s=signInDetails.objects.get(email=email)
        return render(request,"home.html",{"name":s})
    else:
        return render(request,"login.html",{"msg":"invalid login details"})


def Group(request):

    button=request.POST.get("b")
    groupname=request.POST.get("groupName")
    friend1=request.POST.get("m")
    friend2=request.POST.get("n")
    friend3=request.POST.get("o")
    yousEmail=request.POST.get("name")
    email1=request.POST.get("email1")
    email2=request.POST.get("email2")
    email3=request.POST.get("email3")
    s=signInDetails.objects.get(email=yousEmail)
    if button == "getgroups":
        qs = group.objects.all()
        if qs.count() != 0:
            res=group.objects.values("groupName")
            print(type(res))
            print(res)
            r=[]
            for i in res:
               r.append(i['groupName'])
            return render(request,"home.html",{"result":r,"name":s} )
        else:
            return render(request,"home.html",{"msg":"no groups available"})
    elif button== "save":
        s=group(groupName=groupname,you=s.name,yoursemail=s.email,friend1=friend1,friend2=friend2,friend3=friend3,friend1email=email1,friend2email=email2,friend3email=email3)
        s.save()
    return render(request,"home.html",{"msg":"group created succesfully"})


def creatinggroup(request):
    useremail=request.GET.get("s")
    # useremail=request.GET.get("k")
    print(useremail )
    return render(request,"group.html",{"name":useremail})


def bills(request):
    res=group.objects.values("groupName")
    print(res)
    l=[]
    for i in res:
        l.append(i["groupName"])

    return render(request,"home.html",{"res":l})


def addbill(request):
    groupname=request.POST.get("name")
    loginame=request.POST.get("loginname")
    qs=group.objects.get(groupName=groupname)
    print(qs.friend1)

    return render(request,"bill.html",{"res":qs,"groupname":groupname,"username":loginame})


def expense(request):
    groupname=request.POST.get("groupname")


    return render(request,"addbill.html",{"groupname":groupname})


def sharedbill(request):
    groupname=request.POST.get("groupname")
    totalexpense=int(request.POST.get("e"))
    amountPaidByYou=int(request.POST.get("a"))
    amountPaidByFriend1=int(request.POST.get("b"))
    amountPaidByFriend2=int(request.POST.get("c"))
    amountPaidByFriend3=int(request.POST.get("d"))
    totalfriends=4
    amountEqualShareIs=totalexpense/totalfriends
    t1=amountPaidByYou-amountEqualShareIs
    t2=amountPaidByFriend1-amountEqualShareIs
    t3=amountPaidByFriend2-amountEqualShareIs
    t4=amountPaidByFriend3-amountEqualShareIs
    details=group.objects.get(groupName=groupname)

    s=bill(groupName=groupname,totalexpense=totalexpense,you=t1,friend1=t2,friend2=t3,friend3=t4)
    s.save()
    return render(request,"expenses.html",{ "details":details,"groupname":groupname,"you":str(t1),"friend1":str(t2),"friend2":str(t3),"friend3":str(t4)})


def settleup(request):
    details=request.GET.get("a")
    print(type(details))
    print(details)
    a = details.split(" ")
    print(a)
    groupname = a[0]
    username = a[1]
    billName=a[2]
    if billName == "you":
        bill.objects.filter(groupName=groupname).update(you="0")

        return render(request, "SettledUP.html", {"name":username,"groupname":groupname})
    elif billName == "friend1":
        bill.objects.filter(groupName=groupname).update(friend1="0")
        return render(request, "SettledUP.html", {"name": username, "groupname": groupname})

    elif billName == "friend2":
        bill.objects.filter(groupName=groupname).update(friend2="0")
        return render(request, "SettledUP.html", {"name": username, "groupname": groupname})

    elif billName == "friend3":
        bill.objects.filter(groupName=groupname).update(friend3="0")
    return render(request, "SettledUP.html", {"name": username, "groupname": groupname})
