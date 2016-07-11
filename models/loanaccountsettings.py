# -*- coding:UTF-8 -*-

from openerp import models,fields,api

"""
This class contains the implementation of Accounting mapping with loanProduct 
"""

class LoanProductAccounting(models.Model):
    _inherit = "product.template"
    property_account_fund_id = fields.Many2one('account.account', company_dependent=True,
        string="Fund Account",
        domain=[('deprecated', '=', False)],
        help="Fund Account for the current product.")
    property_loan_portfolio_id = fields.Many2one('account.account', company_dependent=True,
        string="Loan Portfolio Account",
        domain = [('deprecated', '=', False)],
        help="Loan Portfolio Account. ")