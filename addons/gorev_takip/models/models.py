from odoo import models, fields, api


class gorev_takip(models.Model):
    _name = 'gorev_takip.gorev_takip'
    _description = 'gorev_takip.gorev_takip'

    name = fields.Char("Görevin Başlığı")
    description = fields.Text("Görevin Açıklaması")
    isDone = fields.Selection([('0','Yapılıyor'),('1','Yapılmadı'),('2','Yapıldı'),('3','İptal edildi')],string='Yapılma Durumu')
    donumBasinaUcret = fields.Integer("Dönüm başına ücret")
    address_id = fields.One2many('gorev.adres','task_ids',string='Görevin Adresi')
    medicine_id = fields.One2many('task.medicine','medicine_task_ids',string='Görevde Kullanılan İlaçlar')
    pilot_id = fields.One2many('task.pilot','pilot_task_ids',string='Görev Alan Pilotlar')





    