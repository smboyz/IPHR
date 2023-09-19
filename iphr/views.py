from django.shortcuts import render, redirect,HttpResponse
from adminpanel.models import GlobalSettings, Navigation, ContactUS, Hiring, Apply
from django.contrib import messages

def const(request):
    
    return render(request,"New/underconstruction.html")

def Base(request):
    glob = GlobalSettings.objects.all()
    sli = Navigation.objects.filter(status='Publish', page_type='Slider').order_by('position')
    abo = Navigation.objects.filter(status='Publish', page_type='Home/About').order_by('position')
    miss = Navigation.objects.filter(status='Publish', page_type='Mission/Vision').order_by('position')
    serv = Navigation.objects.filter(status='Publish', page_type='Service').order_by('position')
    serv_1 = Navigation.objects.filter(status='Publish', page_type='Service_1').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    cont = Navigation.objects.filter(status='Publish', page_type='Contact').order_by('position')
    cont_1 = Navigation.objects.filter(status='Publish', page_type='Contact_1').order_by('position')
    test = Navigation.objects.filter(status='Publish', page_type='Testimonial').order_by('position')
    test_1 = Navigation.objects.filter(status='Publish', page_type='Testimonial_1').order_by('position')
    features = Navigation.objects.filter(status='Publish', page_type='Feature').order_by('position')
    f_mobile = Navigation.objects.filter(status='Publish', page_type='Feature/mobile').order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        

        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    return render(request, "New/home.html", {'glob':glob,'sli':sli,'abo':abo,'miss':miss,'serv':serv,'serv_1':serv_1,
                                             'step':step,'step_1':step_1,'cont':cont,'test':test,"test_1":test_1,
                                             'cont_1':cont_1,'main':main,'features':features,'f_mobile':f_mobile})

def redirect_to_url(request, name):
    if name == '21':
       return redirect('mass')
    elif name == '36':
        return redirect('staffing')
    elif name == '37':
        return redirect('recruiment')
    elif name == '35':
        return redirect('contact')
    elif name == '118':
        return redirect('about')
    elif name == '48':
        return redirect('oli_gas')
    elif name == '49':
        return redirect('ecommerce')
    elif name == '50':
        return redirect('manufacturing')
    elif name == '51':
        return redirect('hospitality')
    elif name == '52':
        return redirect('healthcare')
    elif name == '53':
        return redirect('financial')
    elif name == '54':
        return redirect('hr_business')
    elif name == '55':
        return redirect('realestate')
    elif name == '56':
        return redirect('supplychain')
    elif name == '57':
        return redirect('energychemical')
    elif name == '58':
        return redirect('retailtrading')
    elif name == '59':
        return redirect('fmcg')
    elif name == '60':
        return redirect('shipping')
    elif name == '61':
        return redirect('information')
    # elif name == '10':
    #     return redirect('service')
       
    else:
        return HttpResponse("Id not Matched")

def service(request,id):
    glob = GlobalSettings.objects.all()
    serv_1 = Navigation.objects.filter(status='Publish', id=id)
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')
    
    return render(request, "New/service.html", {'glob':glob,'serv_1':serv_1,'main':main,})

def mass(request):
    glob = GlobalSettings.objects.all()
    conn = Navigation.objects.filter(status='Publish', page_type='Contact_2')
    mass = Navigation.objects.filter(status='Publish', page_type='mass').order_by('position')
    mass_1 = Navigation.objects.filter(status='Publish', page_type='mass_1').order_by('position')
    mass_2 = Navigation.objects.filter(status='Publish', page_type='mass_2').order_by('position')
    mass_3 = Navigation.objects.filter(status='Publish', page_type='mass_3').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        

        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request, "New/mass.html", {'glob':glob,'conn':conn,'mass':mass,'mass_1':mass_1,'mass_2':mass_2,
                                            'step':step,'step_1':step_1,'mass_3':mass_3,'main':main,})

def contact(request):
    glob = GlobalSettings.objects.all()
    conn = Navigation.objects.filter(status='Publish', page_type='ContactUs')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        Country=request.POST.get('Country')
        subject=request.POST.get('subject')

        if len(name)<2 or len(email)<3 or len(subject)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            con=ContactUS(name=name,email=email,subject=subject,phone=phone,city=city,Country=Country)
            con.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request, "New/contact.html", {'glob':glob,'conn':conn,'main':main,})  

def staffing(request):
  
  glob = GlobalSettings.objects.all()
  staff = Navigation.objects.filter(status='Publish', page_type='Contract').order_by('position')
  staff_1 = Navigation.objects.filter(status='Publish', page_type='Contract_1').order_by('position')
  staff_2 = Navigation.objects.filter(status='Publish', page_type='Contract_2').order_by('position')
  step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
  step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
  conn = Navigation.objects.filter(status='Publish', page_type='Staff/Contact')
  main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

  if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

  
  return render(request, "New/staffing.html", {'glob':glob,'staff':staff,'staff_1':staff_1,'staff_2':staff_2,
                                               'step':step,'step_1':step_1,'conn':conn,'main':main,})

def recruiment(request):
    glob = GlobalSettings.objects.all()
    recu = Navigation.objects.filter(status='Publish', page_type='Recruitment').order_by('position')
    recu_1 = Navigation.objects.filter(status='Publish', page_type='Recruitment_1').order_by('position')
    recu_2 = Navigation.objects.filter(status='Publish', page_type='Recruitment_2').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    conn = Navigation.objects.filter(status='Publish', page_type='Recruitment/Contact')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)


    return render(request,"New/recruiment.html", {'glob':glob,'recu':recu,'recu_1':recu_1,'recu_2':recu_2,'step':step,
                                                'step_1':step_1,'conn':conn,'main':main,})


def all_job(request):
  glob = GlobalSettings.objects.all()
  job = Navigation.objects.filter(status='Publish', page_type='AllJob').order_by('position')
  all_job = Navigation.objects.filter(status='Publish', page_type='AllJob_1').order_by('position')
  main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')
  
  return render(request,"New/all-job.html", {'glob':glob,'main':main,'job':job,'all_job':all_job})

def about(request):
  glob = GlobalSettings.objects.all()
  abo = Navigation.objects.filter(status='Publish', page_type='AboutUs').order_by('position')
  about_image = Navigation.objects.filter(status='Publish', page_type='AboutUs_1').order_by('position')
  main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')
  
  return render(request,"New/about.html", {'glob':glob,'main':main,'abo':abo,'about_image':about_image})

def submit_cv(request):
    glob = GlobalSettings.objects.all()
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')
    s_cv = Navigation.objects.filter(status='Publish', page_type='Submit_CV').order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        profession=request.POST.get('profession')
        message=request.POST.get('message')
        visa =request.POST.get('visa')
        cv = request.FILES.get('cv')
        

        if len(name)<2 or len(email)<3  :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            appl=Apply(name=name,email=email,phone=phone,message=message,profession=profession,cv=cv,visa=visa)
            
            appl.save()
            messages.success(request,"Successfully submitted contact you soon..",)

    return render(request,'New/submit-cv.html',{'glob':glob,'main':main,'s_cv':s_cv})

def oli_gas(request):
    glob = GlobalSettings.objects.all()
    oil = Navigation.objects.filter(status='Publish', page_type='Oil and Gas').order_by('position')
    oil_1 = Navigation.objects.filter(status='Publish', page_type='Oil and Gas_1').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    conn = Navigation.objects.filter(status='Publish', page_type='Oil/Contact')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request,"New/Oil and Gas.html",{'glob':glob,'main':main,'oil':oil,'oil_1':oil_1,'step':step,
                                                  'step_1':step_1,'conn':conn})

def ecommerce(request):
    glob = GlobalSettings.objects.all()
    comm = Navigation.objects.filter(status='Publish', page_type='E-Commerce').order_by('position')
    comm_1 = Navigation.objects.filter(status='Publish', page_type='E-Commerce_1').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    conn = Navigation.objects.filter(status='Publish', page_type='Commerce/Contact')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request,"New/ecommerce.html",{'glob':glob,'main':main,'comm':comm,'comm_1':comm_1,'step':step,
                                                  'step_1':step_1,'conn':conn})

def manufacturing(request):
    glob = GlobalSettings.objects.all()
    manu = Navigation.objects.filter(status='Publish', page_type='Manufacturing').order_by('position')
    manu_1 = Navigation.objects.filter(status='Publish', page_type='Manufacturing_1').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    conn = Navigation.objects.filter(status='Publish', page_type='Manufac/Contact')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request,"New/manufacturing.html",{'glob':glob,'main':main,'manu':manu,'manu_1':manu_1,'step':step,
                                                  'step_1':step_1,'conn':conn})

def hospitality(request):
    glob = GlobalSettings.objects.all()
    hosp = Navigation.objects.filter(status='Publish', page_type='Hospitality').order_by('position')
    hosp_1 = Navigation.objects.filter(status='Publish', page_type='Hospitality_1').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    conn = Navigation.objects.filter(status='Publish', page_type='Hospital/Contact')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request,"New/hospitality.html",{'glob':glob,'main':main,'hosp':hosp,'hosp_1':hosp_1,'step':step,
                                                  'step_1':step_1,'conn':conn})

def healthcare(request):
    glob = GlobalSettings.objects.all()
    heal = Navigation.objects.filter(status='Publish', page_type='Healthcare').order_by('position')
    heal_1 = Navigation.objects.filter(status='Publish', page_type='Healthcare_1').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    conn = Navigation.objects.filter(status='Publish', page_type='Health/Contact')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request,"New/healthcare.html",{'glob':glob,'main':main,'heal':heal,'heal_1':heal_1,'step':step,
                                                  'step_1':step_1,'conn':conn})

def financial(request):
    glob = GlobalSettings.objects.all()
    fan = Navigation.objects.filter(status='Publish', page_type='Financial & Banking').order_by('position')
    fan_1 = Navigation.objects.filter(status='Publish', page_type='Financial & Banking_1').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    conn = Navigation.objects.filter(status='Publish', page_type='Financial/Contact')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request,"New/financialbanking.html",{'glob':glob,'main':main,'fan':fan,'fan_1':fan_1,'step':step,
                                                  'step_1':step_1,'conn':conn})

def hr_business(request):
    glob = GlobalSettings.objects.all()
    hr = Navigation.objects.filter(status='Publish', page_type='HR and Business').order_by('position')
    hr_1 = Navigation.objects.filter(status='Publish', page_type='HR and Business_1').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    conn = Navigation.objects.filter(status='Publish', page_type='HR/Contact')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request,"New/hr_businesssupport.html",{'glob':glob,'main':main,'hr':hr,'hr_1':hr_1,'step':step,
                                                  'step_1':step_1,'conn':conn})

def realestate(request):
    glob = GlobalSettings.objects.all()
    real = Navigation.objects.filter(status='Publish', page_type='Real Estate').order_by('position')
    real_1 = Navigation.objects.filter(status='Publish', page_type='Real Estate_1').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    conn = Navigation.objects.filter(status='Publish', page_type='Real/Contact')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request,"New/realestate_construction.html",{'glob':glob,'main':main,'real':real,'real_1':real_1,'step':step,
                                                  'step_1':step_1,'conn':conn})

def supplychain(request):
    glob = GlobalSettings.objects.all()
    supp = Navigation.objects.filter(status='Publish', page_type='Supply chain').order_by('position')
    supp_1 = Navigation.objects.filter(status='Publish', page_type='Supply chain_1').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    conn = Navigation.objects.filter(status='Publish', page_type='Supply/Contact')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request,"New/supplychain_logistic.html",{'glob':glob,'main':main,'supp':supp,'supp_1':supp_1,'step':step,
                                                  'step_1':step_1,'conn':conn})

def energychemical(request):
    glob = GlobalSettings.objects.all()
    eng = Navigation.objects.filter(status='Publish', page_type='Energy & Chemicals').order_by('position')
    eng_1 = Navigation.objects.filter(status='Publish', page_type='Energy & Chemicals_1').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    conn = Navigation.objects.filter(status='Publish', page_type='Energy/Contact')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request,"New/energychemical.html",{'glob':glob,'main':main,'eng':eng,'eng_1':eng_1,'step':step,
                                                  'step_1':step_1,'conn':conn})

def retailtrading(request):
    glob = GlobalSettings.objects.all()
    ret = Navigation.objects.filter(status='Publish', page_type='Retail & Trading').order_by('position')
    ret_1 = Navigation.objects.filter(status='Publish', page_type='Retail & Trading_1').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    conn = Navigation.objects.filter(status='Publish', page_type='Retail/Contact')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request,"New/retailtrading.html",{'glob':glob,'main':main,'ret':ret,'ret_1':ret_1,'step':step,
                                                  'step_1':step_1,'conn':conn})

def fmcg(request):
    glob = GlobalSettings.objects.all()
    fmcg = Navigation.objects.filter(status='Publish', page_type='FMCG').order_by('position')
    fmcg_1 = Navigation.objects.filter(status='Publish', page_type='FMCG_1').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    conn = Navigation.objects.filter(status='Publish', page_type='FMCG/Contact')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request,"New/fmcg_industry.html",{'glob':glob,'main':main,'fmcg':fmcg,'fmcg_1':fmcg_1,'step':step,
                                                  'step_1':step_1,'conn':conn})

def shipping(request):
    glob = GlobalSettings.objects.all()
    ship = Navigation.objects.filter(status='Publish', page_type='Shipping').order_by('position')
    ship_1 = Navigation.objects.filter(status='Publish', page_type='Shipping_1').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    conn = Navigation.objects.filter(status='Publish', page_type='CShipping/Contact')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request,"New/shipping.html",{'glob':glob,'main':main,'ship':ship,'ship_1':ship_1,'step':step,
                                                  'step_1':step_1,'conn':conn})
def information(request):
    glob = GlobalSettings.objects.all()
    info = Navigation.objects.filter(status='Publish', page_type='Information').order_by('position')
    info_1 = Navigation.objects.filter(status='Publish', page_type='Information_1').order_by('position')
    step = Navigation.objects.filter(status='Publish', page_type='Step').order_by('position')
    step_1 = Navigation.objects.filter(status='Publish', page_type='Step_1').order_by('position')
    conn = Navigation.objects.filter(status='Publish', page_type='Inform/Contact')
    main = Navigation.objects.filter(status='Publish', Parent = None).order_by('position')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        business=request.POST.get('business')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<4 :
            messages.error(request,"Cannot submit your message. Something went wrong.",)

        else:
            hir=Hiring(name=name,email=email,phone=phone,business=business,message=message)
            hir.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...",)

    return render(request,"New/information.html",{'glob':glob,'main':main,'info':info,'info_1':info_1,'step':step,
                                                  'step_1':step_1,'conn':conn})

