from django.db import models

class User(models.Model):
    gd = [
        ('M',"Male"),
        ("F","Female"),
        ("O",'Other')
    ]
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True,max_length=150)
    mobile = models.CharField(max_length=150)
    gndr = models.CharField(max_length=10,choices=gd)
    gitlink = models.URLField(blank=True)
    fblink = models.URLField(blank=True)
    linkdinlink = models.URLField(blank=True)
    twerlink = models.URLField(blank=True)
    abotme = models.TextField(blank=True)

    def __str__(self):
        return self.first_name+" "+self.last_name


class ProjectCategory(models.Model):
    ptype = [
        ('mini','Mini'),
        ('major','Major'),
    ]
    prjct_type = models.CharField(max_length=150,choices=ptype,default='mini')
    prjectname = models.CharField(max_length=150)
    projctdsc = models.CharField(max_length=150,blank=True)
    skillsinvolve = models.CharField(max_length=150)
    prj_url=models.URLField(blank=True)
    

    def __str__(self):
        return self.prjectname

class Certification(models.Model):
    certname = models.CharField(max_length=150)
    certorg = models.CharField(max_length=150)
    cerdesc = models.CharField(max_length=150,blank=True)
    issued_on = models.DateField()
    expires_on = models.DateField(blank=True,null=True)
    cerfurl = models.URLField(blank=True)
    cerlogo = models.ImageField(upload_to='certifications/',blank=True)

    def __str__(self):
        return self.certname

class Skills(models.Model):
    skname = models.CharField(max_length=150)
    skprofec = models.PositiveIntegerField()
    sklogo = models.ImageField(upload_to='skills/',blank=True)

    def __str__(self):
        return self.skname

class Education(models.Model):
    ed_type=[
        ('PG','PG'),
        ('UG','UG'),
        ('Intermediate','Intermediate'),
        ('SSC','SSC'),
    ]
    md=[
        ('FullTime','FullTime'),
        ('PartTime','PartTime'),
        ('Distinct','Distinct'),
    ]
    edu_type = models.CharField(max_length=150,choices=ed_type)
    university_name = models.CharField(max_length=150,blank=True)
    institute_name = models.CharField(max_length=150)
    course_degree = models.CharField(max_length=150)
    branch = models.CharField(max_length=150,blank=True)
    yearofpass = models.CharField(max_length=150)
    modeofstudy = models.CharField(max_length=150,choices=md)
    score = models.PositiveIntegerField()
    edu_desc = models.CharField(max_length=150,blank=True)

    def __str__(self):
        return self.university_name