from django.db import models
from accounts.models import User
from clients.models import Client
from vehicles.models import Vehicle

class Order(models.Model):

    STATUS_CHOICES = (
        ('aberta', 'Aberta'),
        ('aguardando aprovacao', 'Aguardando Aprovação'),
        ('aguardando pecas', 'Aguardando Peças'),
        ('em andamento', 'Em Andamento'),
        ('cancelada', 'Cancelada'),
        ('concluida', 'Concluída'),
        ('entregue', 'Entregue')
    )
    service_order_number = models.CharField(max_length=20,unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='orders')
    operator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='operated_orders')
    mechanic = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mechanic_orders')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='aberta')
    description_problem = models.TextField()
    description_service = models.TextField()
    observations = models.TextField (blank=True, null=True)
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    finalized_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.client} - {self.vehicle} - {self.status}'

    class Meta:
        ordering = ['-created_at']
