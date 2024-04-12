from django.shortcuts import render
from django.http import HttpResponse
from  home.models import UserModel,UserPosts
import json

# Create your views here.
def Hello(request):
    return HttpResponse("HELLO WORLD")

def Login(request):
    if request.method == 'POST':
        obj=UserModel()
        users=UserModel.objects.all()
        password = request.POST.get('pass')
        email = request.POST.get('email')
        users = UserModel.objects.filter(email=email, password=password)
        
        if users.exists():
            user = users.first()
            # Convert UserModel instance to a dictionary
            user_dict = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                # Add other fields as needed
            }
            # Serialize the dictionary to JSON
            user_json = json.dumps(user_dict)
            # Store the serialized JSON data in the session
            request.session['user'] = user_json
            posts=UserPosts.objects.all()
            return render(request, "home.html", {"user": user.name,"posts":posts})
        else:
            return HttpResponse("Failed: Invalid email or password")
    else:
        return render(request, 'login.html')

def Regis(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('mail')
        password = request.POST.get('pass')
        obj=UserModel(name=name,email=email,password=password)
        obj.save()
        # Do something with the form data, like save to the database
        return HttpResponse(f"registered successfully")
    else:
        return render(request, 'regis.html')
    
def Home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('pass')
        # Do something with the form data, like save to the database
        return HttpResponse(f"Name: {name}, Email: {email}")
    else:
        stored_data = request.session.get('user')
        # Deserialize the JSON data to a dictionary
        user_dict = json.loads(stored_data)
        # Access the 'name' field from the dictionary
        user_name = user_dict.get('name')
        posts=UserPosts.objects.all()
        return render(request, "home.html", {"user": user_name,"posts":posts})
    
def Create(request):
    if request.method == 'POST':
        des = request.POST.get('describe')
        title = request.POST.get('title')
        stored_data = request.session.get('user')
        # Deserialize the JSON data to a dictionary
        user_dict = json.loads(stored_data)
        # Access the 'name' field from the dictionary
        user_name = user_dict.get('name')
        user_email = user_dict.get('email')
        obj=UserPosts(name=user_name,email=user_email,post=des,title=title);
        obj.save()
        # Do something with the form data, like save to the database
        return HttpResponse("Post Created!!")
    else:
        return render(request, 'create.html')

def Logout(request):
    request.session.clear()
    return render(request, 'login.html')