from django.db import models
# from django.utils import timezone

class GlobalSettings(models.Model):
    SiteName = models.CharField(max_length=100)
    SiteContact = models.CharField(max_length=100)
    SiteEmail = models.EmailField()
    SiteAddress = models.CharField(max_length=500)
    Sitedescription = models.CharField(max_length=500)
    Sitelicence = models.CharField(max_length=300)
    Sitetwitterlink = models.CharField(max_length=300)
    Sitefacebooklink = models.CharField(max_length=300)
    Sitelinkdinlink = models.CharField(max_length=300)
    Siteinstagramlink = models.CharField(max_length=300,null=True)
    Sitewhatsapplink = models.CharField(max_length=300)
    Sitefax = models.CharField(max_length=300,null=True)
    logo = models.ImageField(upload_to="logo/",max_length=200, null=True, default=None)
    back_image = models.ImageField(upload_to="backgroundimage/",null=True)
    brochure = models.FileField(upload_to="brochure/",null=True)
    brochure_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.SiteName

class ContactUS(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    phone = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=50,null=True)
    Country = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name
    
class Hiring(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    phone = models.CharField(max_length=50,null=True)
    business = models.CharField(max_length=50,null=True)

    def _str_(self):
        return self.name
    
class Apply(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    phone = models.CharField(max_length=50,null=True)
    profession = models.CharField(max_length=50,null=True)
    visa = models.CharField(max_length=80,null=True)
    cv = models.FileField(upload_to='cv_uploads/',null=True)

    def _str_(self):
        return self.name

class Navigation(models.Model):
    PAGE_TYPE = (
        ('Home', 'Home'),('Mission/Vision','Mission/Vision'),('Home/About', 'Home/About'),('Group', 'Group'),
        ('Slider', 'Slider'),('Service', 'Service'),('Service_1', 'Service_1'),('Step', 'Step'),('Step_1', 'Step_1'),
        ('Contact', 'Contact'),('Connectstaff', 'Connectstaff'),('mass', 'mass'),('Contact_1', 'Contact_1'),
        ('Contact_2', 'Contact_2'),('Testimonial', 'Testimonial'),('Testimonial_1', 'Testimonial_1'),('Feature','Feature'),('Feature/mobile','Feature/mobile'),('mass_1', 'mass_1'),
        ('mass_2', 'mass_2'),('mass_3', 'mass_3'),('Contract','Contract'),('Contract_1','Contract_1'),('Contract_2','Contract_2'),
        ('Recruitment','Recruitment'),('Recruitment_1','Recruitment_1'),('Recruitment_2','Recruitment_2'),
        ('Staff/Contact', 'Staff/Contact'),('Recruitment/Contact', 'Recruitment/Contact'),('ContactUs', 'ContactUs'),
        ('AllJob', 'AllJob'),('AllJob_1', 'AllJob_1'),('AboutUs', 'AboutUs'),('AboutUs_1', 'AboutUs_1'),
        ('Oil and Gas', 'Oil and Gas'),('E-Commerce', 'E-Commerce'),('Manufacturing', 'Manufacturing'),('Hospitality', 'Hospitality'),
        ('Healthcare', 'Healthcare'),('Financial & Banking', 'Financial & Banking'),('HR and Business', 'HR and Business'),('Real Estate', 'Real Estate'),
        ('Supply chain', 'Supply chain'),('Energy & Chemicals', 'Energy & Chemicals'),('Retail & Trading', 'Retail & Trading'),('FMCG', 'FMCG'),
        ('Shipping', 'Shipping'),('Information', 'Information'),('Oil and Gas_1', 'Oil and Gas_1'),('E-Commerce_1', 'E-Commerce_1'),('Manufacturing_1', 'Manufacturing_1'),
        ('Hospitality_1', 'Hospitality_1'),('Healthcare_1', 'Healthcare_1'),('Financial & Banking_1', 'Financial & Banking_1'),('HR and Business_1', 'HR and Business_1'),
        ('Real Estate_1', 'Real Estate_1'),('Supply chain_1', 'Supply chain_1'),('Energy & Chemicals_1', 'Energy & Chemicals_1'),('Retail & Trading_1', 'Retail & Trading_1'),
        ('FMCG_1', 'FMCG_1'),('Shipping_1', 'Shipping_1'),('Information_1', 'Information_1'),('Oil/Contact', 'Oil/Contact'),
        ('Commerce/Contact', 'Commerce/Contact'),('Manufac/Contact', 'Manufac/Contact'),('Hospital/Contact', 'Hospital/Contact'),('Health/Contact', 'Health/Contact'),
        ('Financial/Contact', 'Financial/Contact'),('HR/Contact', 'HR/Contact'),('Real/Contact', 'Real/Contact'),
        ('Supply/Contact', 'Supply/Contact'),('Energy/Contact', 'Energy/Contact'),('Retail/Contact', 'Retail/Contact'),('FMCG/Contact', 'FMCG/Contact'),
        ('Shipping/Contact', 'Shipping/Contact'),('Inform/Contact', 'Inform/Contact'),
        ('Submit_CV','Submit_CV')
    )

    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft')
    )
    name = models.CharField(max_length=100, null=False)
    caption = models.CharField(max_length=100)
    status = models.CharField(choices=STATUS, max_length=50)
    position = models.IntegerField()
    page_type = models.CharField(choices=PAGE_TYPE, null=True, blank=True, max_length=50)
    title = models.CharField(max_length=200)
    short_desc = models.TextField(null=True)
    desc = models.TextField(null=True)
    bannerimage = models.ImageField(upload_to="bannerimage/",null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_keyword = models.CharField(max_length=100, null=True)
    icon_image = models.TextField(null=True)
    image = models.ImageField(upload_to="image/", null=True)
    slider_image = models.ImageField(upload_to="sliderimage/", null=True)
    Parent = models.ForeignKey('self', related_name="childs", on_delete=models.CASCADE, null=True, blank=True)
    brochure = models.FileField(upload_to="brochure/",null=True)

    def __str__(self):
        return self.name
    





