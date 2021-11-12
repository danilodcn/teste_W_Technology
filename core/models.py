from django.db import models


# como os campos de client e empresa possuem os mesmos campos,
# podemos fazer as duas classes herdarem de uma mesma classe
class UserBase(models.Model):
    name = models.CharField("Name", max_length=50, null=False, blank=False)
    doc = models.CharField("CPF/CNPJ", max_length=20, null=False, blank=False)
    about = models.TextField(max_length=250, null=False, blank=False)
    active = models.BooleanField(default=False, blank=False, null=False)
    site = models.CharField(max_length=100)


class Empresa(UserBase):
    ...


class Cliente(UserBase):
    ...


class Oferta(models.Model):
    id_consumer = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    from_field = models.CharField(
        "from", db_column="from", null=False, blank=False
    )

    to = models.CharField(null=False, blank=False)

    initial_value = models.DecimalField(
        decimal_places=2, max_digits=20, blank=False, null=False
    )

    amount = models.DecimalField(
        decimal_places=2, max_digits=20, blank=False, null=False
    )
    amount_type = models.CharField(
        "Amount Type", blank=False, null=False
    )


class Lance(models.Model):
    id_provider = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_offer = models.ForeignKey(Oferta, on_delete=models.CASCADE)

    value = models.DecimalField(
        decimal_places=2, max_digits=20, blank=False, null=False
    )

    amount = models.DecimalField(
        decimal_places=2, max_digits=20, blank=False, null=False
    )
