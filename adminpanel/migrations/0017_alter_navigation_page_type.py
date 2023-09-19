# Generated by Django 4.2.5 on 2023-09-08 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0016_apply_alter_navigation_page_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigation',
            name='page_type',
            field=models.CharField(blank=True, choices=[('Home', 'Home'), ('Mission/Vision', 'Mission/Vision'), ('Home/About', 'Home/About'), ('Group', 'Group'), ('Slider', 'Slider'), ('Service', 'Service'), ('Service_1', 'Service_1'), ('Step', 'Step'), ('Step_1', 'Step_1'), ('Contact', 'Contact'), ('Connectstaff', 'Connectstaff'), ('mass', 'mass'), ('Contact_1', 'Contact_1'), ('Contact_2', 'Contact_2'), ('Testimonial', 'Testimonial'), ('Testimonial_1', 'Testimonial_1'), ('Feature', 'Feature'), ('Feature/mobile', 'Feature/mobile'), ('mass_1', 'mass_1'), ('mass_2', 'mass_2'), ('mass_3', 'mass_3'), ('Contract', 'Contract'), ('Contract_1', 'Contract_1'), ('Contract_2', 'Contract_2'), ('Recruitment', 'Recruitment'), ('Recruitment_1', 'Recruitment_1'), ('Recruitment_2', 'Recruitment_2'), ('Staff/Contact', 'Staff/Contact'), ('Recruitment/Contact', 'Recruitment/Contact'), ('ContactUs', 'ContactUs'), ('AllJob', 'AllJob'), ('AllJob_1', 'AllJob_1'), ('AboutUs', 'AboutUs'), ('AboutUs_1', 'AboutUs_1'), ('Oil and Gas', 'Oil and Gas'), ('E-Commerce', 'E-Commerce'), ('Manufacturing', 'Manufacturing'), ('Hospitality', 'Hospitality'), ('Healthcare', 'Healthcare'), ('Financial & Banking', 'Financial & Banking'), ('HR and Business', 'HR and Business'), ('Real Estate', 'Real Estate'), ('Supply chain', 'Supply chain'), ('Energy & Chemicals', 'Energy & Chemicals'), ('Retail & Trading', 'Retail & Trading'), ('FMCG', 'FMCG'), ('Shipping', 'Shipping'), ('Information', 'Information'), ('Oil and Gas_1', 'Oil and Gas_1'), ('E-Commerce_1', 'E-Commerce_1'), ('Manufacturing_1', 'Manufacturing_1'), ('Hospitality_1', 'Hospitality_1'), ('Healthcare_1', 'Healthcare_1'), ('Financial & Banking_1', 'Financial & Banking_1'), ('HR and Business_1', 'HR and Business_1'), ('Real Estate_1', 'Real Estate_1'), ('Supply chain_1', 'Supply chain_1'), ('Energy & Chemicals_1', 'Energy & Chemicals_1'), ('Retail & Trading_1', 'Retail & Trading_1'), ('FMCG_1', 'FMCG_1'), ('Shipping_1', 'Shipping_1'), ('Information_1', 'Information_1'), ('Oil/Contact', 'Oil/Contact'), ('Commerce/Contact', 'Commerce/Contact'), ('Manufac/Contact', 'Manufac/Contact'), ('Hospital/Contact', 'Hospital/Contact'), ('Health/Contact', 'Health/Contact'), ('Financial/Contact', 'Financial/Contact'), ('HR/Contact', 'HR/Contact'), ('Real/Contact', 'Real/Contact'), ('Supply/Contact', 'Supply/Contact'), ('Energy/Contact', 'Energy/Contact'), ('Retail/Contact', 'Retail/Contact'), ('FMCG/Contact', 'FMCG/Contact'), ('Shipping/Contact', 'Shipping/Contact'), ('Inform/Contact', 'Inform/Contact')], max_length=50, null=True),
        ),
    ]