# -*- coding:UTF-8 -*-

from openerp import models, fields, api

"""
This class contains Loan Settings which enables a loan to do activities such as amortization
calculation period, define repayment strategy , define days in year, etc

"""

class LoanSettings(models.Model):
    _name = 'product.template.loansettings'
    name = fields.Char(string='Loan Account Settings Name')
    display_name = fields.Char(string='Loan Account Settings', compute='_compute_display_name')
    amortization = fields.Selection([('a',"Equal Installment"),('b',"Equal Principal Payments")], default = 'a')
    interestMethod = fields.Selection([('a',"Declining Balance"), ('b',"Flat")], default = 'a')
    interestCalculationPeriod = fields.Selection([('a',"Same as repayment"),('b', "Daily")], default = 'a')
    calculateExactdays = fields.Boolean()
    repaymentStrategy = fields.Selection([('a',"Penalties Fees Interest Principal Order"),('b',"OverDue/Due Fees/Interest Principal"),('c',"Principal Interest Penalties Fees")], default = 'a')
    arrearsTolerance = fields.Integer()
    arrearsAgeing = fields.Integer()
    daysInYear = fields.Selection([('a',"Actual"), ('b',"360 Days"), ('c',"365 Days"),('d', "364 Days")], default = 'a')
    daysInMonth = fields.Selection([('a',"Actual"), ('b', "30 Days")], default = 'a')
    npa = fields.Integer()
    
    
    @api.one
    @api.depends('name')
    def _compute_display_name(self):
        names = [self.name]
        self.display_name =  '/'.join(filter(None,names))
        
    
    

