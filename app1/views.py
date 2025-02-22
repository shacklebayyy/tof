from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import StudentForm
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')  # Redirects to login page
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user
            return redirect('/')  # Redirect to home page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


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
        punshmentgiven = request.POST.get('punshmentgiven', student.punshmentgiven)
        picture = request.FILES.get('picture', student.picture)  # Handle image update

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
        punshmentgiven = request.POST.get('punshmentgiven')
        picture = request.FILES.get('picture')  # ✅ Get the uploaded image

        # print(name,email,age,gender)
        query=Student(fname=fname,sname = sname,kcpe_marks = kcpe_marks ,current_grade = current_grade ,adm =adm ,age=age,classs =classs, stream =stream, mistake = mistake, punshmentgiven = punshmentgiven, picture =picture )
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
    