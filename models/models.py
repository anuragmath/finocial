# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class lending_core(models.Model):
#     _name = 'lending_core.lending_core'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class LoanProductModel(models.Model):
    
    """
    This class reference all the fields related to loan Calculation from the loan Product these fields 
    can be accessed and used while applying transaction over a loan
    """
    
    _inherit = 'product.template'
    
    loanproductsetingsref = fields.Reference([('product.template.loansettings', 'Loan Settings')])
    loanterms = fields.Reference([('product.template.loanapplicationterms', 'Loan Terms')])
    

