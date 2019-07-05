import requests
import smtplib
import time
from bs4 import BeautifulSoup

product_list = []
changed_product = []
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

smtp_link = 'smtp.gmail.com'
smtp_port = 587
auth_email = 'email_from_send@example.com'
auth_pass = 'email_app_pass'
email_to = 'email_to_send@example.com'
sleep_time = 60


class Main:
    file_name = 'product-list.txt'

    def init(self):
        self.get_items()

    def get_items(self):
        with open(Main.file_name, 'r') as my_file:
            lines = my_file.readlines()
            for line in lines:
                line_split = line.split('|||')
                nob = {
                    'price': line_split[0],
                    'url': line_split[1]
                }
                product_list.append(nob)
            # print(product_list)
        while(True):
            del changed_product[:]
            self.check_for_changes()
            time.sleep(sleep_time)

    def check_for_changes(self):
        for product in product_list:
            self.check_product(product.get('url'), product.get('price'))
        print(len(changed_product))
        if(len(changed_product) > 0):
            self.send_email()

    def check_product(self, url, reqPrice):
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(id="productTitle").get_text().strip()
        price = soup.find(id="priceblock_ourprice").get_text().strip()
        format_price = price.replace('£', '').replace('€', '').replace(',', '')
        converted_price = float(format_price)

        if converted_price < float(reqPrice):
            product = {
                'title': title,
                'price': price,
                'url': url
            }
            changed_product.append(product)

    def send_email(self):
        server = smtplib.SMTP(smtp_link, smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(auth_email, auth_pass)

        subject = 'Price fell Down!'
        body = 'Check the price for:\n\n'

        for product in changed_product:
            body += f"{product.get('title')} - {product.get('url')}\n\n"

        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(auth_email, email_to, msg)
        print('Email has been sent!')
        server.quit()


main = Main()
main.init()
