from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from math import ceil
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.decorators import user_passes_test
from .forms import UserRegisterForms,ProfileUpdateForm,UserUpdateForms,checkoutForm,basicAddForm,smartAddForm
from .models import phone,basic,smart,checkout
import json



@login_required
def index(request):
    if request.method == 'POST':
        search_text = request.POST.get("search")
        all = phone.objects.all()
        result = [item for item in all if search_text.lower() in item.fullName.lower()]
        phn = []
        phn.append(result)
        phn.append(range(ceil(len(result)/4)))
   
        # print(all)
        return render(request,'mobsms/searchresult.html',{'phone':phn,'home':False})
    basicPhone = [basic.objects.values('PhoneId','Brand','Model_name','Model_number','Color','Price','Quantity','Category','Front_image','Primary_camera','Internal_storage','Ram','Supported_networks'),range(ceil(len(basic.objects.all())/4))]
    smartPhone = [smart.objects.values('PhoneId','Brand','Model_name','Model_number','Color','Price','Quantity','Category','Front_image','Primary_camera','Internal_storage','Ram','Supported_networks'),range(ceil(len(smart.objects.all())/4))]

    all_phone = {'basicPhone':basicPhone,'smartPhone':smartPhone,'home':True}
    return render(request,'mobsms/index.html',all_phone)



@login_required
def regester(request):
    if request.method == 'POST':
        form = UserRegisterForms(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request,f'Your acount has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForms()
    return render(request,'mobsms/register.html',{'form':form})



@login_required
def quickView(request,Id):
    cat = (phone.objects.filter(PhoneId = Id)[0].Category)
    if cat == 'smart':
        viewphone = smart.objects.filter(PhoneId = Id)
    elif cat == 'basic':
        viewphone = basic.objects.filter(PhoneId = Id)
    return render(request,'mobsms/quickview.html',{'phone':viewphone[0]})



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForms(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
            
    else:
        u_form = UserUpdateForms(instance= request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    contex = {'u_form':u_form,'p_form':p_form}
    return render(request,'mobsms/profile.html',contex)



@login_required
def checkOut(request):
    if request.method == 'POST':
        check_form = checkoutForm(request.POST)
        if check_form.is_valid():
            id = check_form.save().id
            cart = request.POST.get('cart')
            cart = json.loads(cart)
            for key,value in cart.items():
                PhoneId = key[2:]
                phn = phone.objects.filter(PhoneId = PhoneId)
                new_qty = phn[0].Quantity - value[1]
                phn.update(Quantity = new_qty)
            return redirect(f'/checkout/bill/{id}')
    else:
        check_form = checkoutForm()
    return render(request,'mobsms/checkout.html',{'check_form':check_form})




@login_required
def bill(request,Id):
    get_check = checkout.objects.filter(id = Id)
    return render(request,'mobsms/bill.html',{'full_name':get_check.first().full_name,'email':get_check.first().email,'phone_no':get_check.first().phone_no,'total_price':get_check.first().total_price,'cart':get_check.first().cart,'date':get_check.first().date,'id':get_check.first().id})




@login_required
def add(request):
    if not request.user.is_staff:
        return HttpResponse("<h1>bhag chutiye</h1>")
    if request.method == 'POST':
        b_form = basicAddForm(request.POST,request.FILES)
        s_form = smartAddForm(request.POST,request.FILES)
        category = request.POST.get('select phone')
        if category == 'smart':
            if s_form.is_valid():
                s_form.save()
                messages.success(request, f'Mobile phone has been added!')
                return redirect('add phone')
        elif category == 'basic':
            if b_form.is_valid():
                b_form.save()
                messages.success(request, f'Mobile phone has been added!')
                return redirect('add phone')
    else:
            b_form = basicAddForm()
            s_form = smartAddForm()
    return render(request,'mobsms/addphone.html',{'b_form':b_form,'s_form':s_form})



def updateMobile(request,Id):
    if not request.user.is_staff:
        return HttpResponse("<h1>bhag chutiye</h1> ")
    cat = phone.objects.filter(PhoneId = Id)[0].Category
    if request.method == 'POST':
        if cat == 'smart':
            form = smartAddForm(request.POST,request.FILES,instance=smart.objects.filter(PhoneId = Id)[0])
        else:
            form = basicAddForm(request.POST,request.FILES,instance=basic.objects.filter(PhoneId = Id)[0])

        if form.is_valid():
            form.save()
            messages.success(request, f"Item has been updated!")
            return redirect('home')
    else:
        if cat == 'smart':
            form = smartAddForm(instance=smart.objects.filter(PhoneId = Id)[0])
        else:
            form = basicAddForm(instance=basic.objects.filter(PhoneId = Id)[0])
    return render(request,'mobsms/updatemobile.html',{'form':form})