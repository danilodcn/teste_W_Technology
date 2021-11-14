from django.test import TestCase
from core.models import Cliente, Empresa, Lance, Oferta

class TestBasic(TestCase):
    def teste_converte_cliente_em_str_(self):
        nome = "Danilo Nascimento"
        client = Cliente(
            name=nome,
            doc="61148978964",
            about="Ola mundo",
            site="www.danilo.site"
        )
        # print("Dentro")
        
        esperado = nome
        resultado = str(client)

        self.assertEqual(esperado, resultado)

    def teste_converte_Empresa_em_str(self):
        nome = "Google"
        client = Empresa(
            name=nome,
            doc="111111111/99999",
            about="Google",
            site="www.google.com"
        )
        # print("Dentro")
        
        esperado = nome
        resultado = str(client)

        self.assertEqual(esperado, resultado)

    def teste_converte_Oferta_em_str(self):
        nome = "Google"
        empresa = Empresa(
            name=nome,
            doc="111111111/99999",
            about="Google",
            site="www.google.com"
        )

        oferta = Oferta(
            id_consumer=empresa,
            from_field="Acailandia",
            to = "Parauapebas",
            initial_value=50.09,
            amount=5568.43,
        )
        # print("Dentro")
        
        esperado = f"Oferta do {nome}"
        resultado = str(oferta)

        self.assertEqual(esperado, resultado)

    def teste_converte_lance_em_str_(self):
        nome = "Danilo Nascimento"

        client = Cliente(
            name=nome,
            doc="61148978964",
            about="Ola mundo",
            site="www.danilo.site"
        )

        nome = "Google"
        empresa = Empresa(
            name=nome,
            doc="111111111/99999",
            about="Google",
            site="www.google.com"
        )

        oferta = Oferta(
            id_consumer=empresa,
            from_field="Acailandia",
            to = "Parauapebas",
            initial_value=50.09,
            amount=5568.43,
        )

        lance = Lance(
            id_provider=client,
            id_offer=oferta,
            value = 20.40,
            amount = 60.87
        )
        # print("Dentro")
        
        esperado = 'Lance (offer=Oferta do Google, provider=Danilo Nascimento)'
        resultado = str(lance)

        self.assertEqual(esperado, resultado)
