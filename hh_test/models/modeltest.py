# -*- coding: utf-8 -*-
from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)

class ModelA(models.Model):
    _name = 'hhtest.modela'
    name = fields.Char('TEN A')
    model_b = fields.One2many('hhtest.modelb','modela_id')



class ModelB(models.Model):
    _name = 'hhtest.modelb'
    name = fields.Char("TEn B")
    modela_id = fields.Many2one('hhtest.modela', ondelete='cascade')