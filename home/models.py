from django.db import models


class Reference(models.Model):
    TYPE_CHOICES = (
        ("brand", "Brand"),
        ("ram", "RAM"),
        ("memory", "Memory"),
        ("color", "Color"),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    value = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = ("type", "value")
    def __str__(self):
        return f"{self.type}: {self.value}"

class Stuff(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('seller', 'Seller'),
        ('manager', 'Manager'),
    ]

    full_name = models.CharField(max_length=150)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='seller')
    phone = models.CharField(max_length=20)
    hired_date = models.DateField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    photo = models.ImageField(upload_to='staff_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.role}"

class Phone(models.Model):
    picture = models.FileField(upload_to="images/phone_photos")
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(
        Reference,
        on_delete=models.PROTECT,
        limit_choices_to={"type": "brand"},
        related_name="brand_phones"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_year = models.PositiveIntegerField()
    display_size = models.CharField(max_length=20)
    resolution = models.CharField(max_length=50)
    cpu = models.CharField(max_length=50)
    ram = models.ForeignKey(
        Reference,
        on_delete=models.PROTECT,
        limit_choices_to={"type": "ram"},
        related_name="ram_phones"
    )
    memory = models.ForeignKey(
        Reference,
        on_delete=models.PROTECT,
        limit_choices_to={"type": "memory"},
        related_name="memory_phones"
    )
    rear_camera = models.CharField(max_length=100)
    front_camera = models.CharField(max_length=50)
    battery = models.PositiveIntegerField()
    weight = models.FloatField()
    color = models.ForeignKey(
        Reference,
        on_delete=models.PROTECT,
        limit_choices_to={"type": "color"},
        related_name="color_phones"
    )
    material = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.memory.value}, {self.color.value})"

class Purchase(models.Model):
    phone = models.ForeignKey(
        Phone, 
        on_delete=models.CASCADE, 
        related_name="purchases"
    )
    quantity = models.PositiveIntegerField(default=1)
    cost_price = models.DecimalField(max_digits=12, decimal_places=2) 
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.phone.quantity += self.quantity
        self.phone.save()

    def __str__(self):
        return f"Purchase: {self.phone.name} ({self.created_at.date()})"

class Sale(models.Model):
    PAYMENT_METHODS = (
        ("cash", "Cash"),
        ("card", "Card"),
        ("transfer", "Transfer"),
    )
    phone = models.ForeignKey(
        Phone, 
        on_delete=models.PROTECT, 
        related_name="sales"
    )
    quantity = models.PositiveIntegerField(default=1)
    price_sold = models.DecimalField(max_digits=10, decimal_places=2) 
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, default="cash")
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.phone.name} - {self.quantity}pcs"

    def remove(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.phone.quantity -= self.quantity
        self.phone.save()
        
    @property
    def total_amount(self):
        return self.price_sold * self.quantity
        print(sale.total_amount())