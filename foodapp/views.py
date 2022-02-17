from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
from foodapp.forms import FoodForm
from foodapp.models import Food


def home(request):
    return render(request, 'html/home.html')


def starter(request):
    return render(request, 'html/starter.html')


def menu(request):
    return render(request, 'html/menu.html')


def drinks(request):
    return render(request, 'html/drinks.html')


def meals(request):
    return render(request, 'html/meals.html')


def combo(request):
    return render(request, 'html/combo.html')


def snack(request):
    return render(request, 'html/snack.html')


def cartsave(request):
    return render(request, 'html/cartsave.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'html/home.html')
        else:
            messages.info(request, 'Invalid Password or Username.Try again')
            return render(request, 'html/login.html')
    else:
        return render(request, 'html/login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return render(request, 'html/registration.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return render(request, 'html/registration.html')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                c = "User created Sucessfully"
                return render(request, 'html/registration.html', {'c': c})
        else:
            m = "Password not matched"
            return render(request, 'html/registration.html', {'m': m})

        return render(request, 'html/registration.html')
    else:
        return render(request, 'html/registration.html')


def logout(request):
    auth.logout(request)
    return render(request, 'html/home.html')


def order(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            try:

                form.save()
                c = "Order Placed Successfully, Our Delivery Boy will contact you and inform the actual amount soon."
                return render(request, 'html/cartsave.html', {'c': c})
            except:
                pass
    else:
        form = FoodForm()
        return render(request, 'html/cartsave.html', {'form': form})


def yourcartnew(request):
    return render(request, 'html/yourcart.html')


def yourcart(request):
    member = Food.objects.all()
    return render(request, 'html/yourcart.html', {'member': member})


def delete(request, id):
    m = Food.objects.get(id=id)
    m.delete()
    return redirect('/foodapp/yourcart')


def edit(request):
    return render(request, 'html/edit.html')


def update1(request):
    return render(request, 'html/update.html')


def update(request, id):
    var = Food.objects.get(id=id)
    form = FoodForm(request.POST or None, instance=var)
    if form.is_valid():
        form.save()
        return redirect('/foodapp/yourcart')
    return render(request, 'html/edit.html', {'var': var, 'form': form})

