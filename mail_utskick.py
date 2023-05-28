import yagmail
import keyring

#Note that keyring elemnts are removed here on github as it contains gmail account information used to send emails when ads are found.

def send_email(ad):
    receiver = "thisisnotanemail@gmail.com"

    yag = yagmail.SMTP("thisisnotanemail1@gmail.com")
    yag.send(
        to=receiver,
        subject="Ny annons",
        contents=ad,

    )
entry_email = "Test 2"

send_email(entry_email)