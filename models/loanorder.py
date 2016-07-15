# -*- coding: UTF-8 -*-

from openerp import models, fields, api, _

class LoanOrder(models.Model):
    _name = 'sale.loan'
    """
    This class defines the loan _ order where a customer is ordering for loan through customer sales 
    """
    display_name = fields.Char(string='Loan Account', required=True, copy=False, readonly=True, states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))
    origin = fields.Char(string='Loan Account', help="Reference")
    """
    States of loan
    """
    state = fields.Selection([
        ('draft', 'Loan Submitted'),
        ('approved', 'Loan Approved'),
        ('disburse', 'Disburse'),
        ('close', 'Close Loan'),
        ('cancel', 'Cancelled'),
        ('reject','Reject Loan'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
    loan_submit_date = fields.Datetime(string='Submitted Date', required=True, readonly=True, index=True, states={'draft': [('readonly', False)], 'approved': [('readonly', False)]}, copy=False, default=fields.Datetime.now)
    loan_approved_date = fields.Datetime(string='Approved Date', required=True, readonly=True, index=True, states={'approved': [('readonly', False)]}, copy=False, default=fields.Datetime.now)
    loan_disbured_date = fields.Datetime(stirng='Disbursed Date', required=True, readonly=True, index=True, states={'disbursed': [('readonly', False)]}, copy=False, default=fields.Datetime.now)
    product_id = fields.Many2one('product.template', 'Loan Product')
    
    """
    Defining fields that are computed based on the loan products 
    """
    proposed_principal = fields.Float('Principal', digits = (12,2))
    
    approved_principal = fields.Float('Approved Principal', digits=(12,2))
    
    interest_rate = fields.Float('Interest Rate', digits=(10,2))
    
    loan_term = fields.Integer()
    
    partner_id = fields.Many2one('res.partner', string='Customer', readonly=True, states={'draft': [('readonly', False)], 'approved': [('readonly', False)]}, required=True, change_default=True, index=True, track_visibility='always')
    
    
   
    
    
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('sale.loan') or 'New'
            
        result = super(LoanOrder, self).create(vals)
        return result

    
    @api.multi
    def action_approve(self):
        self.write({'state': 'approved'})
    
    
    @api.multi
    def action_cancel(self):
        self.write({'state': 'cancel'})
        
    @api.multi
    def action_draft(self):
        self.write({'state': 'draft'})    
        
    