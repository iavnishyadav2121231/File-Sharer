from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import user_file_data, share_file_data
from django.contrib import messages


#login-signup
def login_page(request):
    return render(request,"login.html")

def login_x(request):
    if request.method =="POST":
        if("email" not in request.POST or "password" not in request.POST or request.POST['email']== "" or  request.POST['password'] == ""):
            messages.error(request,"Fields cannot be empty")
            return redirect("login_page")


        user_x = authenticate(username = request.POST['email'],password = request.POST['password'])
        if (user_x is not None):
            login(request,user_x)
        else:
            return redirect("login_page")
    
    return redirect("home_page")

def signup_page(request):
    return render(request,"signup.html")

def register(request):
    if request.method =="POST":

        if("email" not in request.POST or "password" not in request.POST or "name" not in request.POST or request.POST['email']== "" or  request.POST['password'] == "" or request.POST['name']== ""):
            messages.error(request,"Fields cannot be empty")
            return redirect("signup_page")
        
        #if user already registered
        try:
            new_user = User.objects.create_user(request.POST['email'],password=request.POST['password'],first_name = request.POST['name'])
            new_user.save()
        except:
            messages.error(request,"Email Already Registered")
            return redirect("signup_page")
      
        
    return redirect("login_page")

def logout_x(request):
    logout(request)
    return redirect("login_page")


#home
def home_page(request):
    
    if(request.user.is_authenticated):
        return render(request,"home.html",{"username":request.user.username})
    else:
        return redirect("login_page")
        
#file_functions
def upload_file(request):
    
    if(request.user.is_authenticated):
        return render(request,"upload_file_form.html",{"username":request.user.username})
    else:
        return redirect("login_page")
    
def upload_file_submit(request):
    if(request.user.is_authenticated and request.method =="POST"):

     
        if("file_x" not in request.FILES):
            messages.error(request,"File field cannot be empty")
            return redirect("upload_file")
        temp_data = user_file_data(user_ref=request.user,file=request.FILES["file_x"])   
        temp_data.save()  
        return redirect("home_page")    
    else:
        return redirect("login_page")
    
def view_files(request):
    if(request.user.is_authenticated):
        file_list = user_file_data.objects.filter(user_ref = request.user)
        shared_file_list =share_file_data.objects.filter(share_ref = request.user)
        return render(request,"view_files_list.html",{"username":request.user.username,"files":file_list,"shared":shared_file_list,"users":(User.objects.values("username"))
                                                      
})
  

    else:
        return redirect("login_page")
    
#inner function
def share(request):
    if(request.user.is_authenticated and request.method =="GET"):
        if(request.GET["file"] == "" or request.GET['email'] == ""):
            messages.error(request,"Fields cannot be empty")
            return redirect("view_files")
        

        #file or receiver don't exist
        try:
            share_ref = User.objects.get(username = request.GET['email'])
            
        except:
            messages.error(request,"Reciever Does not Exist")
            return redirect("view_files")
        try:
            file_Ref= user_file_data.objects.get(file = request.GET["file"])
            
        except:
            messages.error(request,"No Such File Owned by You")
            return redirect("view_files")

        
            
        temp_data = share_file_data(share_ref=share_ref,file_Ref= file_Ref)  

        temp_data.save()  
        return redirect("home_page")    
    else:
        return redirect("login_page")
    
def delete_x(request,file):
    if(request.user.is_authenticated):
        try:
            file_data = user_file_data.objects.get(file = "files/"+file)
            file_data.file.delete()
            file_data.delete()
        except:
            messages.error(request,"No Such File Owned by You")
        return redirect("view_files")    
         
    else:
        return redirect("login_page")

#error when user doen't exist    
def profile(request,email):
    if(request.user.is_authenticated):
        try:
            user_x = User.objects.get(username= email)
            return render(request,"profile.html",{"user":user_x})
        except:
            messages.error(request,"No Such User Exists")
            return redirect("view_files")
        
    else:
        return redirect("login_page")