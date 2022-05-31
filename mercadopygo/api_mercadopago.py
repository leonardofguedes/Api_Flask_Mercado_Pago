import mercadopago
import json

CLIENT_ID = 'leonardoguedes'
CLIENT_SECRET = 'leonardoguedes'


def payment(req, **kwargs):
    product = kwargs['product']
    preference = {
      "items": [
        {
          "title": product.name,
          "quantity": product.quantity,
          "currency_id": "BRL",
          "unit_price": product.price
        }
      ]
    }

    mp = mercadopago.MP(CLIENT_ID, CLIENT_SECRET)

    preferenceResult = mp.create_preference(preference)

    url = preferenceResult["response"]["init_point"]
    
    return url
