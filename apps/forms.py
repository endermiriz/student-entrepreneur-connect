from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileSize
from wtforms import StringField, DateField, EmailField, BooleanField
from wtforms.validators import Email, DataRequired
from apps import app


class ContactForm(FlaskForm):
    isim = StringField('Isim', id='name', validators=[DataRequired()])
    bolum = StringField('Bolum', id='bolum', validators=[DataRequired()])
    dogumtarihi = DateField('DogumTarihi', id='dogumtarihi', validators=[DataRequired()])
    mail = EmailField('Email', id='email', validators=[Email()])
    phone = StringField('Phone', id='phone', validators=[DataRequired()])
    ozgecmis = StringField('OzGecmis', id='ozgecmis', validators=[DataRequired()])
    projeOzet = StringField('ProjeOzet', id='projeozet', validators=[DataRequired()])
    hedefPazar = StringField('HedefPazar', id='hedefpazar', validators=[DataRequired()])
    gelirmodeli = StringField('GelirModeli', id='gelirmodeli', validators=[DataRequired()])
    finansal_check = BooleanField('Finansal', id='finansal')
    mentorluk_check = BooleanField('Mentorluk', id='mentorluk')
    isgelistirme_check = BooleanField('IsGelistirme', id='isgelistirme')
    pazarlama_check = BooleanField('Pazarlama', id='pazarlama')
    belge = FileField('DetayDosya', id='detaydosya', validators=[FileSize(app.config.get("MAX_CONTENT_LENGTH"))])
