from django.db import models

class Gender(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.name

class Brands(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.name

class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    addressline1 = models.CharField(max_length=100,default=None,blank=True,null=True)
    addressline2 = models.CharField(max_length=100,default=None,blank=True,null=True)
    addressline3 = models.CharField(max_length=100,default=None,blank=True,null=True)
    pin = models.CharField(max_length=10,default=None,blank=True,null=True)
    city = models.CharField(max_length=20,default=None,blank=True,null=True)
    state = models.CharField(max_length=20,default=None,blank=True,null=True)
    pic = models.ImageField(upload_to="images/",default=None,null=True,blank=True)
    otp = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id)+" "+self.username

class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    addressline1 = models.CharField(max_length=100,default=None,blank=True,null=True)
    addressline2 = models.CharField(max_length=100,default=None,blank=True,null=True)
    addressline3 = models.CharField(max_length=100,default=None,blank=True,null=True)
    pin = models.CharField(max_length=10,default=None,blank=True,null=True)
    city = models.CharField(max_length=20,default=None,blank=True,null=True)
    state = models.CharField(max_length=20,default=None,blank=True,null=True)
    pic = models.ImageField(upload_to="images/",default=None,null=True,blank=True)
    otp = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id)+" "+self.username


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    subcat = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands,on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE,default=None)
    baseprice = models.IntegerField()
    discount = models.IntegerField(default=0)
    finalprice = models.IntegerField()
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    description = models.TextField()
    stock = models.BooleanField(default=True)
    time = models.DateTimeField(auto_now=True)
    pic1 = models.ImageField(upload_to="images/")
    pic2 = models.ImageField(upload_to="images/")
    pic3 = models.ImageField(upload_to="images/")
    pic4 = models.ImageField(upload_to="images/")

    def __str__(self):
        return str(self.id)+" "+self.name

class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+" "+self.buyer.username

choice = ((1,"Not Packed"),(2,"Packed"),(3,"shipped"),(4,"out of delivery"),(5,"Delivered"))
paymentchoice = ((1,"Pending"),(2,"Done"))
mode = ((1,"COD"),(2,"Net Banking"))

class Checkout(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    product = models.CharField(max_length=30)
    total = models.IntegerField()
    shipping = models.IntegerField(default=0)
    finalamount= models.IntegerField()
    status = models.IntegerField(choices=choice,default=1)
    paymentstatus = models.IntegerField(choices=paymentchoice,default=1)
    mode = models.IntegerField(choices=mode,default=1)
    time = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    orderId=models.CharField(max_length=50,default=None,blank=True,null=True)
    paymentId = models.CharField(max_length=50,default=None,blank=True,null=True)
    paymentsignature = models.CharField(max_length=50,default=None,null=True,blank=True)

    def __str__(self):
        return str(self.id)+" "+self.buyer.username+" "+str(self.active)


class Subscribe(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)+" "+self.email

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=15,default=None)
    subject = models.CharField(max_length=30)
    #message = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)+" "+str(self.active)+" "+self.name+" "+self.subject
