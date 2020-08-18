from selenium import webdriver
import datetime
import smtplib
import os
from email.message import EmailMessage


def check_stock(url, actual_size, email):
    driver = webdriver.Chrome('/Users/linhan/Desktop/Han/Learning/Project/Restock Alert/chromedriver')
    driver.get(url)

    sold_out = 'rgba(247, 247, 247, 1)'
    size_order = (actual_size - 4.5) * 2
    xpath = '//*[@id="buyTools"]/div[1]/fieldset/div/div[{0}]/label'.format(str(size_order))
    try:
        size_result = driver.find_element_by_xpath(xpath).value_of_css_property('background-color')
        if size_result == sold_out:
            result = 'size {} is sold out.'.format(actual_size)
            print(result)
            # send_email('Nike Stock Alert', result, email)
        else:
            result = 'size {} is in stock.'.format(actual_size)
            print(result)
            send_email('Nike Stock Alert', result, email)
    except:
        result = 'This color is unavailable.'
        print(result)
        # send_email('Nike Stock Alert', result, email)
    driver.close()
    # driver.quit()


def send_email(subject, body, to_email='64linhan@gmail.com'):
    email_address = os.environ.get('GMAIL_USER')
    email_password = os.environ.get('GMAIL_PASS')

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = to_email
    msg.set_content(body)
 
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)


if __name__ == '__main__':
    # url = 'https://www.nike.com/t/wildhorse-6-womens-trail-running-shoe-jJXN1F/BV7099-001'  # black
    url = 'https://www.nike.com/t/wildhorse-6-womens-trail-running-shoe-jJXN1F/BV7099-400'  # green
    actual_size = 6.5
    email = '64linhan@gmail.com'

    print('\n', datetime.datetime.today())
    check_stock(url, actual_size, email)
