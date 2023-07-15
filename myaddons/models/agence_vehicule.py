from odoo import models, fields

class AgenceVehicule(models.Model):
    _name = 'agence.vehicule'
    _description = 'agence.vehicule'


    marque = fields.Char('Marque', required=True)
    modele = fields.Char('Modele', required=True)
    date_achat = fields.Date("Date d'achat", required=False)
    chauffeur_ids = fields.Many2many('res.partner', string='Chauffeurs')
    chauffeur_note = fields.Char('Chauffer Note', required=False)
