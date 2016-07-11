# -*- coding:UTF-8 -*-

from openerp import models, fields, api

"""
This class holds the loanProductTerms which contains these kinds of 
dataTypes which are basic for any loanProduct offering extend at you wish 

@author: Saransh Sharma Team@TheupscaleLabs
"""

class LoanApplicationTerms(models.Model):
    _name = 'product.template.loanapplicationterms'
    name = fields.Char(string='Loan Term Name')
    display_name = fields.Char(string='Loan Application Terms',compute='_compute_display_name')
    principal = fields.Float('Principal', digits = (12,2))
    minPrincipal = fields.Float('Minimum Principal', digits = (12,2))
    maxPrincipal = fields.Float('Maximum Principal', digits = (12,2))
    repayment = fields.Integer();
    minrepayment = fields.Integer('Minimum Number Of Repayments')
    maxRepayment = fields.Integer('Maximum Number of Repayments')
    nominalInterestRate = fields.Float('Interest Rate', digits = (10,2))
    minNominalInterestrate = fields.Float('Minimum Interest Rate',digits = (10,2))
    maxNominalInterestrate = fields.Float('Maximum Interest Rate', digits = (10,2))
    repaidEvery = fields.Integer();
    repaidEveryType = fields.Selection([('a',"Days"),('b',"Months")], default = 'a')
    
    @api.one
    @api.depends('name')
    def _compute_display_name(self):
        names = [self.name]
        self.display_name =  '/'.join(filter(None,names))
        
    

"""
Now we have to define the validations in the models, 
"""


    
    