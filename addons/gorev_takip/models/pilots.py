from odoo import models, fields, api

class TaskPilot(models.Model):
    _name = 'task.pilot'
    _description = 'task.pilot'
    
    name = fields.Char("Pilot Kullanıcı Adı")
    pilotStatus = fields.Selection([('0','Pilot'),('1','Copilot'),('3','Stajyer'),('4','Bölge Sorumlusu')],string='Pilotluk Durumu')
    pilot_task_ids = fields.Many2one('gorev_takip.gorev_takip',string ='Görev(İsteğe Bağlı) ',required=False)