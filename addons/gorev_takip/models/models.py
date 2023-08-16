from odoo import models, fields, api

class gorev_takip(models.Model):
    _name = 'gorev_takip.gorev_takip'
    _description = 'gorev_takip.gorev_takip'

    addressname = fields.Char("Görevin Başlığı")
    description = fields.Text("Görevin Açıklaması")
    isDone = fields.Selection([('0','Yapılıyor'),('1','Yapılmadı'),('2','Yapıldı'),('3','İptal edildi')],string='Yapılma Durumu')
    donumBasinaUcret = fields.Integer("Dönüm başına ücret")





    