import requests


class Main:
    def __int__(self, card_number, exp_month, exp_year):
        self.card_number = card_number
        self.exp_month = exp_month
        self.exp_year = exp_year

        self.status = False

        self.cookies = {
            '_ga': 'GA1.1.52286666.1679625395',
            '_ga_NDJ42PQ0BB': 'GS1.1.1679625394.1.0.1679625394.0.0.0',
            'wf-csrf': 'iDFdOEmDqbdbAgkqChhdWTgM7KVycW6ikEtLIvlMm86q',
            'wf-csrf.sig': 'bhj2zaxpoaLd85_zPDkReLc89tj_JsAAbsL1tNVyi8s',
            '_ga_9NW4NLWKZV': 'GS1.1.1679625394.1.1.1679625442.0.0.0',
        }

        self.header = {
            'authority': 'www.hlabs.audio',
            'accept': '*/*, application/json',
            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://www.hlabs.audio',
            'referer': 'https://www.hlabs.audio/checkout',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',

        }

        self.json_data = [
            {
                'operationName': 'CheckoutUpdateStripePaymentMethod',
                'variables': {
                    'paymentMethod': self.id_payment,
                },
                'query': 'mutation CheckoutUpdateStripePaymentMethod($paymentMethod: String!) {\n  ecommerceStoreStripePaymentMethod(paymentMethod: $paymentMethod) {\n    ok\n    __typename\n  }\n}\n',
            },
        ]

    def _get_status(self):
        self.header['x-wf-csrf'] = 'iDFdOEmDqbdbAgkqChhdWTgM7KVycW6ikEtLIvlMm86q'

        response = requests.post('https://www.hlabs.audio/.wf_graphql/apollo', cookies=self.cookies,
                                 headers=self.header,
                                 json=self.json_data)

        if 'ok' in response.json()[0]['data']['ecommerceStoreStripePaymentMethod']:
            self.status = True

    def _get_id_payment(self):
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,uk;q=0.6',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }

        data = f'type=card&billing_details[name]=Anton+lokomoyskii&billing_details[email]=xomoxex635%40wiroute.com&billing_details[address][line1]=fwoenf&billing_details[address][city]=Denver&billing_details[address][country]=US&billing_details[address][postal_code]=03554&card[number]={card_num}&card[cvc]={card_cvv}&card[exp_month]={card_exp_month}&card[exp_year]={card_exp_year}&guid=c3b56d8a-b504-45d5-bd08-b496eeba46a5d7e7f5&muid=9686caf8-f885-4eb9-8329-e5f085e5e55b722c10&sid=ba3dd030-287d-4bb2-bf96-6225ef352080c8b180&payment_user_agent=stripe.js%2F85402de652%3B+stripe-js-v3%2F85402de652&time_on_page=851096&key=pk_live_nyPnaDuxaj8zDxRbuaPHJjip&_stripe_account=acct_1KHW8FLvVyhnk79Q&_stripe_version=2020-03-02'

        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

        self.id_payment = response.json()['id']

    def run(self):
        self._get_id_payment()

        self._get_status()

        return {'status': self.status}


