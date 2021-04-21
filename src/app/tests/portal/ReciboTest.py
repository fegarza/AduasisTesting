import unittest
from app.tests.portal.LoginTest import LoginTest
from app.configuration.Configuration import Configuration

class ReciboTest(unittest.TestCase):

    def test_crear_recibo(self):
        config = Configuration()
        #config.driver.get(config.portal_url+'/OrdenCompra/Recibo/Create.xhtml')
        config.driver.get(config.portal_url+'/Embarque/Configuracion/Botones.xhtml')

        
        self.assertEqual(config.driver.title, 'Portal Aduanero')