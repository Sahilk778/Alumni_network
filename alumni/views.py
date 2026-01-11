from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import AlumniProfile, Job


# -------------------------
# HOME PAGE
# -------------------------
def home(request):
    # If user is logged in, send to dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'alumni/home.html')


# -------------------------
# LOGIN
# -------------------------
def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')   # home will redirect to dashboard
        else:
            return render(request, 'alumni/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'alumni/login.html')


# -------------------------
# REGISTER
# -------------------------
def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        department = request.POST.get('department')
        graduation_year = request.POST.get('year')

        if not name or not email or not password or not graduation_year:
            return render(request, 'alumni/register.html', {
                'error': 'All required fields must be filled'
            })

        if User.objects.filter(username=name).exists():
            return render(request, 'alumni/register.html', {
                'error': 'User already exists'
            })

        user = User.objects.create_user(
            username=name,
            email=email,
            password=password
        )

        AlumniProfile.objects.create(
            user=user,
            department=department,
            graduation_year=graduation_year
        )

        return redirect('/login/')   # 👈 Register → Login

    return render(request, 'alumni/register.html')


# -------------------------
# LOGOUT
# -------------------------
def user_logout(request):
    logout(request)
    return redirect('login')


# -------------------------
# DASHBOARD (PROTECTED)
# -------------------------
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'alumni/dashboard.html')


# -------------------------
# ALUMNI LIST (PROTECTED)
# -------------------------
@login_required(login_url='login')
def alumni_list(request):
    alumni = AlumniProfile.objects.all()
    return render(request, 'alumni/alumni_list.html', {'alumni': alumni})


# -------------------------
# JOB LIST (PROTECTED)
# -------------------------
@login_required(login_url='login')
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'alumni/job_list.html', {'jobs': jobs})


# -------------------------
# ADD JOB (PROTECTED)
# -------------------------
@login_required(login_url='login')
def add_job(request):
    if request.method == "POST":
        title = request.POST.get('title')
        company = request.POST.get('company')
        description = request.POST.get('description')

        Job.objects.create(
            title=title,
            company=company,
            description=description,
            posted_by=request.user
        )

        return redirect('job_list')

    return render(request, 'alumni/add_job.html')
