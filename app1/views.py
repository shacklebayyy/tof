
import random
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import StudentForm
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login ,logout
from django.core.mail import send_mail 
from django.contrib.auth.models import User
from django.conf import settings



def verify_otp(request):
    return render(request, 'verify_otp.html')  # Ensure this template exists

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('app1:login')  # Redirect to login page


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('app1:dashboard')  # Change to your dashboard URL
        else:
            messages.error(request, "Incorrect username or password")

    return render(request, "app1/login.html")
def search_student(request):
    query = request.GET.get('adm')  # Get admission number from form input
    student = None

    if query:
        try:
            student = Student.objects.get(adm=query)
        except Student.DoesNotExist:
            student = None

    return render(request, 'search.html', {'student': student, 'query': query})




@login_required(login_url='/login/')  # Redirects to login page
def index(request):
    messages.success(request, "Welcome back!")  # Display a success message
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("app1:register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("app1:register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect("app1:register")

        # Generate 4-digit OTP
        otp = random.randint(1000, 9999)
        request.session["otp"] = otp
        request.session["temp_user"] = {"username": username, "email": email, "password": password}

        # Send email
        send_mail(
            "Your Verification Code",
            f"Your OTP is: {otp}",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        messages.info(request, "A verification code has been sent to your email.")
        return redirect("app1:verify_otp")

    return render(request, "register.html")

def verify_otp(request):
    if request.method == "POST":
        entered_otp = request.POST["otp"]
        saved_otp = request.session.get("otp")

        if str(entered_otp) == str(saved_otp):
            temp_user = request.session.get("temp_user")
            if temp_user:
                # Create user
                user = User.objects.create_user(
                    username=temp_user["username"],
                    email=temp_user["email"],
                    password=temp_user["password"]
                )
                user.save()

                # Clear session
                del request.session["otp"]
                del request.session["temp_user"]

                login(request, user)
                messages.success(request, "Registration successful!")
                return redirect("/")
        else:
            messages.error(request, "Invalid verification code!")

    return render(request, "verify_otp.html")

def updateData(request, id):
    student = Student.objects.get(id=id)  # Fetch the student record

    if request.method == "POST":
        fname = request.POST.get('fname', student.fname)  # Default to existing value
        sname = request.POST.get('sname', student.sname)
        kcpe_marks = request.POST.get("kcpe_marks")
        current_grade = request.POST.get("current_grade")
        adm = request.POST.get('adm', student.adm)
        age = request.POST.get('age', student.age)
        classs = request.POST.get('classs', student.classs)
        stream = request.POST.get('stream', student.stream)
        mistake = request.POST.get('mistake', student.mistake)
        third_mistake = request.POST.get('third_mistake', student.third_mistake)
        mistake_1 = request.POST.get('mistake_1', student.mistake_1)
        punshmentgiven = request.POST.get('punshmentgiven', student.punshmentgiven)
        picture = request.FILES.get('picture', student.picture)  # Handle image update
        blackbook = request.POST.get('blackbook', student.blackbook)
        # ✅ Update the record
        student.fname = fname
        student.sname = sname
        student.kcpe_marks = kcpe_marks
        student.current_grade = current_grade
        student.adm = adm
        student.age = age
        student.classs = classs
        student.stream = stream
        student.mistake = mistake
        student.mistake_1 = mistake_1
        third_mistake =third_mistake
        blackbook = blackbook
        student.punshmentgiven = punshmentgiven
        student.picture = picture  # Update image if a new one is uploaded

        student.save()
        messages.success(request, "Student data updated successfully!")
        return redirect("/viewdata/")  # Redirect after update

    return render(request, "edit.html", {"d": student})  # Pass existing data



def viewdata(request):
    data = Student.objects.all()  # Fetch all student records
    return render(request, 'viewdata.html', {'data': data})

def insert_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to home or success page
    else:
        form = StudentForm()

    data = Student.objects.all()
    return render(request, 'upload.html', {'form': form, 'data': data})








def insertData(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        sname=request.POST.get('sname')
        kcpe_marks = request.POST.get("kcpe_marks")
        current_grade = request.POST.get("current_grade")
        adm=request.POST.get('adm')
        age=request.POST.get('age')
        classs =request.POST.get('classs')
        stream =request.POST.get('stream')
        mistake = request.POST.get('mistake')
        mistake_1 = request.POST.get('mistake_1')
        third_mistake = request.POST.get('third_mistake')
        punshmentgiven = request.POST.get('punshmentgiven')
        picture = request.FILES.get('picture')  # ✅ Get the uploaded image
        blackbook = request.POST.get('blackbook')
        # print(name,email,age,gender)
        query=Student(fname=fname,sname = sname,kcpe_marks = kcpe_marks ,current_grade = current_grade ,adm =adm ,age=age,classs =classs, stream =stream, mistake = mistake,  mistake_1 = mistake_1,  third_mistake =third_mistake,  blackbook = blackbook, punshmentgiven = punshmentgiven, picture =picture )
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/")

    return render(request,"index.html")












# def updateData(request,id):
#     if request.method=="POST":
#         fname=request.POST.get('fname')
#         sname=request.POST.get('sname')
#         adm=request.POST.get('adm')
#         age=request.POST.get('age')
#         classs =request.POST.get('classs')
#         stream =request.POST.get('stream')
#         mistake = request.POST.get('mistake')
#         punshmentgiven = request.POST.get('punshmentgiven')
      

#         edit=Student.objects.get(id=id)
#         edit.fname= fname
#         edit.sname = sname
#         edit.adm = adm 
#         edit.age=age
#         edit.classs = classs
#         edit.stream =stream
#         edit.mistake = mistake
#         edit.punshmentgiven = punshmentgiven
     
#         edit.save()
#         messages.warning(request,"Data Updated Successfully")
#         return redirect("/")

#     d=Student.objects.get(id=id) 
#     context={"d":d}
#     return render(request,"edit.html",context)

def deleteData(request,id):
    d=Student.objects.get(id=id) 
    d.delete()
    messages.error(request,"Data deleted Successfully")
    return redirect("/")
    