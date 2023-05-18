from apps import app, mail
from flask import render_template, request
from flask_mail import Message
from apps.forms import ContactForm
import os


# Flask route for the POST operation.
@app.route("/sendmail", methods=["GET", "POST"])
def mailtalebi():
    if request.method == "POST":
        isim = request.form.get("name")
        bolum = request.form.get("bolum")
        dogumtarihi = request.form.get("dogumtarihi")
        email = request.form.get("email")
        phone = request.form.get("phone")
        cv = request.form.get("cv")
        projeozet = request.form.get("projeozet")
        hedefpazar = request.form.get("hedefpazar")
        gelirmodeli = request.form.get("gelirmodeli")

        finansal_check = request.form.get("finansalcheck") != None
        mentorluk_check = request.form.get("mentorlukcheck") != None
        isgelistirme_check = request.form.get("isgelistirmecheck") != None
        pazarlama_check = request.form.get("pazarlamacheck") != None

        print(
            f"Finansal = {finansal_check}\n"
            f"Mentorluk = {mentorluk_check}\n"
            f"İs Gelistirme = {isgelistirme_check}\n"
            f"Pazarlama = {pazarlama_check}"
        )

        belge = request.files["belge"]

        print(
            isim,
            bolum,
            dogumtarihi,
            email,
            phone,
            cv,
            projeozet,
            hedefpazar,
            gelirmodeli,
        )

        # Since the information of the developers submitting a support request will be sent to the organization's email account, the organization's email address is entered for both variables.
        msg = Message(
            str(isim),
            sender="Organization Mail Address",
            recipients=["Organization Mail Address"],
        )

        # Determines the structure of the incoming email
        msg.body = (
            isim
            + "\n"
            + bolum
            + "\n"
            + dogumtarihi
            + "\n"
            + email
            + "\n"
            + phone
            + "\n"
            + "\n"
            + "Finansal Destek = "
            + str(finansal_check)
            + "\n"
            + "Mentorluk = "
            + str(mentorluk_check)
            + "\n"
            + "İş Geliştirme = "
            + str(isgelistirme_check)
            + "\n"
            + "Pazarlama = "
            + str(pazarlama_check)
            + "\n\n"
            + cv
            + "\n\n"
            + projeozet
            + "\n\n"
            + hedefpazar
            + "\n\n"
            + gelirmodeli
        )

        # If the developer has attached a document for the project, it will be included as an attachment in the email.
        if belge:
            filename = belge.filename
            belge.save(filename)
            with app.open_resource(filename) as f:
                msg.attach(filename, "application/octet-stream", f.read())
            os.remove(filename)
        else:
            pass

        mail.send(msg)
        return "Mail Gönderildi En Kısa Sürede Döneceğiz."
    else:
        pass


# If the file size exceeds the specified size limit in the 'MAX_CONTENT_LENGTH' section, an error is handled, and the user is notified.
@app.errorhandler(413)
def error413(e):
    return "Dosya boyutunuz çok büyük", 413


# When the website homepage is opened, the desired HTML is loaded.
@app.route("/")
def index():
    return render_template("contacts.html")
