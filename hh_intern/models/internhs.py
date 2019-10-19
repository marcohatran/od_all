# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import models, fields, api
import intern_utils
from odoo.exceptions import ValidationError, Warning

import logging
_logger = logging.getLogger(__name__)

class InternHS(models.Model):
    _name = 'intern.internhs'
    _description = 'Thực tập sinh'

    hktt = fields.Char("Địa chỉ hộ khẩu thường trú của TTS (Tiếng Việt có dấu)")
    contact_person = fields.Char("Khi cần liên lạc với ai (Tên: Bố, Mẹ, Vợ.. có dấu)")
    # contact_relative = fields.Char("Quan hệ với TTS - Tiếng Hán")
    contact_relative = fields.Many2one('relation',"Quan hệ với TTS")
    contact_phone = fields.Char("Số điện thoại của người quan hệ với TTS - Thêm đầu +84")
    contact_address = fields.Char("Địa chỉ của người liên lạc (Tiếng Việt có dấu)")



    last_time_education = fields.Char("Thời gian học từ năm nào tới năm nào (Trường học mới nhất ghi trong hồ sơ TTS) - Chữ Hán",store=False,compute='_last_time_education')

    last_education_from_month = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                        ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                        ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng", default='09')

    last_education_from_year = fields.Char("Năm", size=4)

    last_education_to_month = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                                  ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                                  ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng", default='06')
    last_education_to_year = fields.Char("Năm", size=4 )

    @api.multi
    @api.depends('last_education_from_month','last_education_from_year','last_education_to_month','last_education_to_year')
    def _last_time_education(self):
        for rec in self:
            if rec.last_education_from_month and rec.last_education_from_year:
                rec.last_time_education = intern_utils.date_time_in_jp(None,rec.last_education_from_month,rec.last_education_from_year)
            else:
                rec.last_time_education = ""
            if rec.last_education_from_year and rec.last_education_to_year:
                rec.last_time_education = rec.last_time_education + u'～ '

            if rec.last_education_to_month and rec.last_education_to_year:
                rec.last_time_education = rec.last_time_education + \
                                           intern_utils.date_time_in_jp(None,rec.last_education_to_month,rec.last_education_to_year)

    last_time_education2 = fields.Char(
        "Thời gian học từ năm nào tới năm nào - Chữ Hán", store=False,
        compute='_last_time_education2')

    last_education_from_month2 = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                                  ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                                  ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng")

    last_education_from_year2 = fields.Char("Năm", size=4)

    last_education_to_month2 = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                                ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                                ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng")
    last_education_to_year2 = fields.Char("Năm", size=4)

    @api.multi
    @api.depends('last_education_from_month2', 'last_education_from_year2', 'last_education_to_month2',
                 'last_education_to_year2')
    def _last_time_education2(self):
        for rec in self:
            if rec.last_education_from_month2 and rec.last_education_from_year2:
                rec.last_time_education2 = intern_utils.date_time_in_jp(None, rec.last_education_from_month2,
                                                                       rec.last_education_from_year2)
            else:
                rec.last_time_education2 = ""
            if rec.last_education_from_year2 and rec.last_education_to_year2:
                rec.last_time_education2 = rec.last_time_education2 + u'～ '

            if rec.last_education_to_month2 and rec.last_education_to_year2:
                rec.last_time_education2 = rec.last_time_education2 + \
                                          intern_utils.date_time_in_jp(None, rec.last_education_to_month2,
                                                                       rec.last_education_to_year2)



    last_school_education = fields.Char("TÊN TRƯỜNG gần nhất của TTS - tiếng Việt")
    last_school_education_jp = fields.Char("TÊN TRƯỜNG gần nhất của TTS - chữ Hán")

    last_school_education2 = fields.Char("TÊN TRƯỜNG gần nhất của TTS - tiếng Việt")
    last_school_education_jp2 = fields.Char("TÊN TRƯỜNG gần nhất của TTS - chữ Hán")

    time_employee = fields.Char("THỜI GIAN làm việc tại CÔNG TY HOẶC NƠI LÀM VIỆC THỨ NHẤT tiếng Nhật(trước khi vào công ty PC thứ 2 nếu có",store=False,compute='_time_employee')

    time_employee_from_month = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                                  ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                                  ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng")

    time_employee_from_year = fields.Char("Năm", size=4)

    time_employee_to_month = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                                ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                                ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng")
    time_employee_to_year = fields.Char("Năm", size=4)

    @api.depends('time_employee_from_month', 'time_employee_from_year', 'time_employee_to_month',
                 'time_employee_to_year')
    def _time_employee(self):
        for rec in self:
            if rec.time_employee_from_year:
                rec.time_employee = intern_utils.date_time_in_jp(None,rec.time_employee_from_month,
                                                                 rec.time_employee_from_year)
            else:
                rec.time_employee = ""

            if rec.time_employee_from_year and rec.time_employee_to_year:
                rec.time_employee = rec.time_employee + u'～ '

            if rec.time_employee_to_year:
                rec.time_employee = rec.time_employee + \
                                           intern_utils.date_time_in_jp(None,rec.time_employee_to_month,
                                                                        rec.time_employee_to_year)


    job_employee_jp = fields.Char("Ngành nghề - TIẾNG NHẬT")
    job_employee_vi = fields.Char("Ngành nghề - TIẾNG VIỆT")

    time_employee2 = fields.Char(
        "THỜI GIAN làm việc tại CÔNG TY HOẶC NƠI LÀM VIỆC THỨ HAI tiếng Nhật(trước khi vào công ty PC thứ 2 nếu có",store=False,compute='_time_employee2')

    time_employee2_from_month = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                                 ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                                 ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng")

    time_employee2_from_year = fields.Char("Năm", size=4)

    time_employee2_to_month = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                               ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                               ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng")
    time_employee2_to_year = fields.Char("Năm", size=4)

    @api.depends('time_employee2_from_month', 'time_employee2_from_year', 'time_employee2_to_month',
                 'time_employee2_to_year')
    def _time_employee2(self):
        for rec in self:
            if rec.time_employee2_from_year:
                rec.time_employee2 = intern_utils.date_time_in_jp(None,rec.time_employee2_from_month,
                                                                  rec.time_employee2_from_year)
            else:
                rec.time_employee2 = ""

            if rec.time_employee2_from_year and rec.time_employee2_to_year:
                rec.time_employee2 = rec.time_employee2 + u'～ '

            if rec.time_employee2_to_year:
                rec.time_employee2 = rec.time_employee2 + \
                                     intern_utils.date_time_in_jp(None,rec.time_employee2_to_month,
                                                                  rec.time_employee2_to_year)



    job_employee2_jp = fields.Char(
        "Ngành nghề - TIẾNG NHẬT")
    job_employee2_vi = fields.Char(
        "Ngành nghề - TIẾNG VIỆT")

    time_employee3 = fields.Char(
        "THỜI GIAN làm việc tại CÔNG TY HOẶC NƠI LÀM VIỆC THỨ BA tiếng Nhật(trước khi vào công ty PC thứ 2 nếu có",store=False,compute='_time_employee3')
    job_employee3_jp = fields.Char(
        "Ngành nghề - TIẾNG NHẬT")
    job_employee3_vi = fields.Char(
        "Ngành nghề - TIẾNG VIỆT")

    time_employee3_from_month = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                                  ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                                  ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng")

    time_employee3_from_year = fields.Char("Năm", size=4)

    time_employee3_to_month = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                                ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                                ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng")
    time_employee3_to_year = fields.Char("Năm", size=4)

    @api.depends('time_employee3_from_month', 'time_employee3_from_year', 'time_employee3_to_month',
                 'time_employee3_to_year')
    def _time_employee3(self):
        for rec in self:
            if rec.time_employee3_from_year:
                rec.time_employee3 = intern_utils.date_time_in_jp(None,rec.time_employee3_from_month,
                                                                  rec.time_employee3_from_year)
            else:
                rec.time_employee3 = ""

            if rec.time_employee3_from_year and rec.time_employee3_to_year:
                rec.time_employee3 = rec.time_employee3 + u'～ '

            if rec.time_employee3_to_year:
                rec.time_employee3 = rec.time_employee3 + \
                                      intern_utils.date_time_in_jp(None,rec.time_employee3_to_month,
                                                                   rec.time_employee3_to_year)
    #
    time_employee4 = fields.Char(
        "THỜI GIAN làm việc tại CÔNG TY HOẶC NƠI LÀM VIỆC THỨ TƯ tiếng Nhật(trước khi vào công ty PC thứ 2 nếu có",
        store=False, compute='_time_employee4')
    job_employee4_jp = fields.Char(
        "Ngành nghề - TIẾNG NHẬT")
    job_employee4_vi = fields.Char(
        "Ngành nghề - TIẾNG VIỆT")

    time_employee4_from_month = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                                  ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                                  ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng")

    time_employee4_from_year = fields.Char("Năm", size=4)

    time_employee4_to_month = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                                ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                                ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng")
    time_employee4_to_year = fields.Char("Năm", size=4)

    @api.depends('time_employee4_from_month', 'time_employee4_from_year', 'time_employee4_to_month',
                 'time_employee4_to_year')
    def _time_employee4(self):
        for rec in self:
            if rec.time_employee4_from_year:
                rec.time_employee4 = intern_utils.date_time_in_jp(None, rec.time_employee4_from_month,
                                                                  rec.time_employee4_from_year)
            else:
                rec.time_employee4 = ""

            if rec.time_employee4_from_year and rec.time_employee4_to_year:
                rec.time_employee4 = rec.time_employee4 + u'～ '

            if rec.time_employee4_to_year:
                rec.time_employee4 = rec.time_employee4 + \
                                     intern_utils.date_time_in_jp(None, rec.time_employee4_to_month,
                                                                  rec.time_employee4_to_year)
    #
    time_employee5 = fields.Char(
        "THỜI GIAN làm việc tại CÔNG TY HOẶC NƠI LÀM VIỆC THỨ NĂM tiếng Nhật(trước khi vào công ty PC thứ 2 nếu có",
        store=False, compute='_time_employee5')
    job_employee5_jp = fields.Char(
        "Ngành nghề - TIẾNG NHẬT")
    job_employee5_vi = fields.Char(
        "Ngành nghề - TIẾNG VIỆT")

    time_employee5_from_month = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                                  ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                                  ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ],
                                                 "Tháng")

    time_employee5_from_year = fields.Char("Năm", size=4)

    time_employee5_to_month = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                                ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                                ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ],
                                               "Tháng")
    time_employee5_to_year = fields.Char("Năm", size=4)

    @api.depends('time_employee5_from_month', 'time_employee5_from_year', 'time_employee5_to_month',
                 'time_employee5_to_year')
    def _time_employee5(self):
        for rec in self:
            if rec.time_employee5_from_year:
                rec.time_employee5 = intern_utils.date_time_in_jp(None, rec.time_employee5_from_month,
                                                                  rec.time_employee5_from_year)
            else:
                rec.time_employee5 = ""

            if rec.time_employee5_from_year and rec.time_employee5_to_year:
                rec.time_employee5 = rec.time_employee5 + u'～ '

            if rec.time_employee5_to_year:
                rec.time_employee5 = rec.time_employee5 + \
                                     intern_utils.date_time_in_jp(None, rec.time_employee5_to_month,
                                                                  rec.time_employee5_to_year)


    #
    time_start_at_pc = fields.Char("Thời gian bắt đầu làm công ty PC thứ 2(từ tháng, năm, đến nay) TIẾNG NHẬT",store=False,compute='_time_start_at_pc')

    time_start_at_pc_from_month = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                                  ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                                  ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng")

    time_start_at_pc_from_year = fields.Char("Năm", size=4)


    @api.multi
    @api.depends('time_start_at_pc_from_month', 'time_start_at_pc_from_year')
    def _time_start_at_pc(self):
        for rec in self:
            if rec.time_start_at_pc_from_year:
                rec.time_start_at_pc = intern_utils.date_time_in_jp(None,rec.time_start_at_pc_from_month,
                                                                    rec.time_start_at_pc_from_year)
            else:
                rec.time_start_at_pc = ""


            if rec.time_start_at_pc_from_year :
                rec.time_start_at_pc = rec.time_start_at_pc + u'～ 現在'



    # name_and_job_position_pc2_jp = fields.Char("Tên công ty PC2 và vị trí làm việc của TTS tại công ty - TIẾNG NHẬT")
    # name_and_job_position_pc2_vn = fields.Char("Tên công ty PC2 và vị trí làm việc của TTS tại công ty - TIẾNG VIỆT")

    time_at_pc_month = fields.Integer('Tổng thời gian làm việc tại công ty PC2 (tháng)')
    time_at_pc_year = fields.Integer('Tổng thời gian làm việc tại công ty PC2 (năm)')

    total_time_at_pc_jp = fields.Char("Tổng thời gian làm việc tại công ty PC2",store=False)
    total_time_at_pc_vi = fields.Char("Tổng thời gian làm việc tại công ty PC2",store=False)
    #



class DispatchCom2(models.Model):
    _name = 'dispatchcom2'
    _description = u'Công ty phái cử thứ 2'
    _sql_constraints = [('uniq_name', 'unique(name)', u'Đã tồn tại cty phái cử này!'),
                        ('uniq_name_vn','unique(name_vn)', u'Đã tồn tại cty phái cử này!')]
    name = fields.Char(u"Tên công ty (Tiếng Anh)",required=True)

    @api.multi
    @api.onchange('name')
    def onchange_name(self):
        for rec in self:
            if rec.name:
                if type(rec.id) == int:
                    dispatchs = self.env['dispatchcom2'].search([('name','ilike',rec.name.strip()),('id','!=',rec.id)])
                    if len(dispatchs) > 0:
                        raise ValidationError('Dường như có đã có cty phái cử này. Bạn nên kiểm tra lại')
                else:
                    dispatchs = self.env['dispatchcom2'].search([('name', 'ilike', rec.name.strip())])
                    if len(dispatchs) > 0:
                        raise ValidationError('Dường như có đã có cty phái cử này. Bạn nên kiểm tra lại')


    name_vn = fields.Char(u"Tên công ty (Tiếng Việt)",required=True)

    @api.multi
    @api.onchange('name_vn')
    def onchange_name_vn(self):
        for rec in self:
            if rec.name_vn:
                if type(rec.id) == int:
                    dispatchs = self.env['dispatchcom2'].search([('name_vn', 'ilike', rec.name_vn.strip()), ('id', '!=', rec.id)])
                    if len(dispatchs) > 0:
                        raise ValidationError('Dường như có đã có cty phái cử này. Bạn nên kiểm tra lại')
                else:
                    dispatchs = self.env['dispatchcom2'].search([('name_vn', 'ilike', rec.name_vn.strip())])
                    if len(dispatchs) > 0:
                        raise ValidationError('Dường như có đã có cty phái cử này. Bạn nên kiểm tra lại')

    address = fields.Char(u"Địa chỉ công ty (Tiếng Anh)",required=True)

    @api.multi
    @api.onchange('address')
    def onchange_address(self):
        for rec in self:
            if rec.address:
                if type(rec.id) == int:
                    dispatchs = self.env['dispatchcom2'].search(
                        [('address', 'ilike', rec.address.strip()), ('id', '!=', rec.id)])
                    if len(dispatchs) > 0:
                        raise ValidationError('Dường như có đã có cty phái cử này. Bạn nên kiểm tra lại')
                else:
                    dispatchs = self.env['dispatchcom2'].search([('address', 'ilike', rec.address.strip())])
                    if len(dispatchs) > 0:
                        raise ValidationError('Dường như có đã có cty phái cử này. Bạn nên kiểm tra lại')

    director = fields.Char(u"Tên giám đốc công ty (Tiếng Việt)",required=True)
    position_person_sign = fields.Char(u"Chức danh của ký thư PC (Tiếng Nhật)",required=True)
    phone_number = fields.Char(u"Số ĐT",required=True)
    fax_number = fields.Char(u"Số fax")

    day_create = fields.Char(u"Ngày", size=2,required=True)
    month_create = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                           ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                           ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng",required=True)

    year_create = fields.Char(u"Năm", size=4,required=True)

    date_create = fields.Char("Ngày thành lập công ty", store=False,
                                    compute='_date_create')


    @api.multi
    @api.depends('day_create', 'month_create',
                 'year_create')
    def _date_create(self):
        for rec in self:
            if rec.day_create and rec.month_create and rec.year_create:
                rec.date_create = u"Ngày %s tháng %s năm %s" % (
                    rec.day_create, rec.month_create,
                    rec.year_create)
            elif rec.month_create and rec.year_create:
                rec.date_create = u"Tháng %s năm %s" % (
                    rec.month_create, rec.year_create)
            elif rec.year_create:
                rec.date_create = u'Năm %s' % rec.year_create
            else:
                rec.date_create = ""



class DispatchCom1(models.Model):
    _name = 'dispatchcom1'
    _description = u'Công ty phái cử thứ nhất'
    name_short = fields.Char("Tên thường gọi")
    name_jp = fields.Char("Pháp nhân - Chữ Hán",required=True)
    name_en = fields.Char("Pháp nhân - Tiếng Anh",required=True)
    name = fields.Char("Pháp nhân - Tiếng Việt",required=True)
    director = fields.Char("Tên người đại diện",required=True)
    position_director = fields.Char("Chức vụ (Tiếng Nhật)",default=u'社長',required=True)
    position_director_vi = fields.Char("Chức vụ (Tiếng Việt)",default=u'Giám đốc',required=True) #a123
    address_vi = fields.Char("Địa chỉ công ty - Tiếng Việt",required=True)  #a124
    # address_jp = fields.Char("Địa chỉ công ty - Tiếng Nhật",required=True)
    address_en = fields.Char("Địa chỉ công ty - tiếng Anh (Thư TC tiếng Nhật)",required=True)
    phone_number = fields.Char("Số điện thoại")
    fax_number = fields.Char("Số fax")
    license_number = fields.Char("Số giấy phép")  # 121
    day_create = fields.Char("Ngày", size=2,required=True)
    month_create = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                     ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                     ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng",required=True)

    year_create = fields.Char("Năm", size=4,required=True)

    date_create = fields.Char("Ngày thành lập công ty", store=False,
                              compute='_date_create')
    @api.multi
    @api.depends('day_create', 'month_create',
                 'year_create')
    def _date_create(self):
        for rec in self:
            if rec.day_create and rec.month_create and rec.year_create:
                rec.date_create = u"Ngày %s tháng %s năm %s" % (
                    rec.day_create, rec.month_create,
                    rec.year_create)
            elif rec.month_create and rec.year_create:
                rec.date_create = u"Tháng %s năm %s" % (
                    rec.month_create, rec.year_create)
            elif rec.year_create:
                rec.date_create = u'Năm %s' % rec.year_create
            else:
                rec.date_create = ""

    @api.multi
    def name_get(self):
        res = []
        for record in self:
            if record.name_short:
                res.append((record.id, record.name_short))
            else:
                res.append((record.id, record.name))
        return res

    mission = fields.Text("Ngành nghề, nhiệm vụ (Tiếng Nhật)")  # a128
    number_of_employee = fields.Integer("Số nhân viên") #a129
    capital = fields.Char("Tiền vốn (Tiếng Nhật)")  #a130
    revenue = fields.Char("Doanh thu (Tiếng Nhật)") #a131




class TrainingCenter(models.Model):
    _name= "trainingcenter"
    _description = u'Trung tâm đào tạo'
    name_jp = fields.Char("Tên trung tâm đào tạo - Chữ Hán",required=True)
    # address_jp = fields.Char("Địa chỉ TTĐT - Chữ Hán",required=True)
    address_en = fields.Char("Địa chỉ TTĐT - Tiếng Anh",required=True) #a125

    day_create = fields.Char("Ngày", size=2)
    month_create = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                     ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                     ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng")

    year_create = fields.Char("Năm", size=4)

    date_create = fields.Char("Ngày thành lập trung tâm đào tạo", store=False,
                              compute='_date_create')

    @api.multi
    @api.depends('day_create', 'month_create',
                 'year_create')
    def _date_create(self):
        for rec in self:
            rec.date_create = intern_utils.date_time_in_jp(rec.date_create,rec.month_create,rec.year_create)

    phone_number = fields.Char("SĐT")
    responsive_person = fields.Char("Người đại diện",required=True)

    mission = fields.Text("Ngành nghề, nhiệm vụ (Tiếng Nhật)") #a126
    number_of_employee = fields.Integer("Số nhân viên") #a127

    @api.multi
    @api.depends('name_jp')
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, record.name_jp))
        return res

class Guild(models.Model):
    _name ='intern.guild'
    _description = u'Nghiệp đoàn'

    _sql_constraints = [('uniq_name', 'unique(name_acronym)', u'Đã tồn tại nghiệp đoàn có tên này!'),
                        ('uniq_name_jp', 'unique(name_in_jp)', u'Đã tồn tại nghiệp đoàn có tên tiếng hán này!'),
                        ('uniq_name_en', 'unique(name_in_en)', u'Đã tồn tại nghiệp đoàn có tên tiếng anh này!')]
    name_acronym = fields.Char("Tên viết tắt - chữ Romaji")
    name_in_jp = fields.Char("Tên đầy đủ - chữ Hán")
    name_in_en = fields.Char("Tên tiếng Anh")
    license_number = fields.Char("Số giấy phép")             #120
    address_in_jp = fields.Char("Địa chỉ - tiếng Nhật ")
    address_in_romaji = fields.Char("Địa chỉ - chữ ROMAJI")
    post_code = fields.Char("Mã bưu điện (bằng số)")
    phone_number = fields.Char("Số điện thoại")
    fax_number = fields.Char("Số fax (nếu có)")
    position_of_responsive_vi = fields.Char("Chức vụ của người đại diện (ký trong hợp đồng)-Tiếng Việt")
    position_of_responsive_jp = fields.Char("Chức vụ của người đại diện (ký trong hợp đồng)-Chữ Hán")
    name_of_responsive_jp = fields.Char("Tên người đại diện - Chữ Hán")
    name_of_responsive_romaji = fields.Char("Tên người đại diện - Chữ Romaji")

    day_sign = fields.Char("Ngày", size=2)
    month_sign = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
                                     ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
                                     ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ], "Tháng")

    year_sign = fields.Char("Năm", size=4)
    date_sign_agreement = fields.Char("Ngày ký hiệp định giữa Nghiệp đoàn với pháp nhân",store=False,
                              compute='_date_sign_agreement')

    @api.multi
    @api.depends('day_sign', 'month_sign',
                 'year_sign')
    def _date_sign_agreement(self):
        for rec in self:
            rec.date_sign_agreement = intern_utils.date_time_in_jp(rec.day_sign, rec.month_sign, rec.year_sign)

    fee_training_nd_to_pc = fields.Integer("Phí ủy thác đào tạo (Yên)")

    subsidize_start_month = fields.Integer("Trợ cấp đào tạo tháng đầu(Yên)")

    note_subsize_jp = fields.Char("Ghi chú tiếng Nhật")
    note_subsize_vi = fields.Char("Ghi chú tiếng Việt")

    @api.multi
    @api.depends('name_acronym')
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, record.name_acronym))
        return res

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if name:
            args = args or []
            recs = self.search([('name_acronym', 'ilike', name)] + args, limit=limit)
            if not recs:
                recs = self.search([('name_in_en', operator, name)] + args, limit=limit)
            if not recs:
                recs = self.search([('name_in_jp', operator, name)] + args, limit=limit)
            return recs.name_get()
        else:
            return super(Guild, self).name_search(name, args, operator, limit)


class Enterprise(models.Model):
    _name = 'intern.enterprise'
    _description = u'Xí nghiệp'
    _sql_constraints = [('uniq_name', 'unique(name_vi)', u'Đã tồn tại xí nghiệp có tên này!'),
                        ('uniq_name_jp', 'unique(name_jp)', u'Đã tồn tại xí nghiệp có tên tiếng hán này!'),
                        ('uniq_name_romaji', 'unique(name_romaji)', u'Đã tồn tại xí nghiệp có tên tiếng romaji này!')]
    name_vi = fields.Char("Tên xí nghiệp - tiếng Việt")
    name_jp = fields.Char("Tên xí nghiệp - tiếng Hán",required=True)
    name_romaji = fields.Char("Tên xí nghiệp - tiếng Romaji",required=True)

    address_jp = fields.Char("Địa chỉ làm việc - tiếng Hán (lấy từ bảng hợp đồng lương)")
    address_romoji = fields.Char("Địa chỉ làm việc - tiếng Romaji (Tự phiên âm, kiểm tra với khách hàng và PTTT trước khi điền vào HS)")
    phone_number = fields.Char("Số điện thoại")
    fax_number = fields.Char("Số fax")
    name_of_responsive_jp = fields.Char("Tên người đại diện - Tiếng Nhật")
    name_of_responsive_en = fields.Char("Tên người đại diện - Tiếng Anh")



    @api.multi
    @api.depends('name_romaji')
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, record.name_romaji))
        return res

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if name:
            args = args or []
            recs = self.search([('name_romaji', 'ilike', name)] + args, limit=limit)
            if not recs:
                recs = self.search([('name_jp', operator, name)] + args, limit=limit)
            return recs.name_get()
        else:
            return super(Enterprise, self).name_search(name, args, operator, limit)


class PhieuTraLoi(models.Model):
    _name = 'intern.phieutraloi'
    name = fields.Char('Mã số',required=True)
    total_intern = fields.Integer('Tổng số TTS',default=30,required=True)
    total_intern_men = fields.Integer('Tổng số TTS nam',required=True)
    total_intern_women = fields.Integer('Tổng số TTS nữ',required=True)

    total_current_intern = fields.Integer('Số TTS đã đưa vào DS',compute='_compute_total_current_intern')

    @api.multi
    @api.onchange('total_intern','total_intern_women')
    def compute_man(self):
        for record in self:
            record.total_intern_men = record.total_intern - record.total_intern_women

    @api.depends('interns')
    def _compute_total_current_intern(self):
        if self.interns:
            self.total_current_intern = len(self.interns)
        else:
            self.total_current_intern = 0

    interns = fields.One2many('intern.internclone', 'phieutraloi_id')

    @api.model
    def create(self, vals):
        if 'interns' in vals:
            ids = []
            for tmp in vals['interns']:
                ids.append(tmp[0])
            interns = self.env['intern.internclone'].search([('id', 'in', ids)])
            count_man = 0
            count_women = 0
            for intern in interns:
                # _logger.info("intern.gender %s"%intern.gender)
                # ks = self.env['intern.internks'].browse(intern.internks_id)
                if intern.gender and intern.gender == 'nam':
                    count_man +=1
                else:
                    count_women += 1

            if count_man> vals['total_intern_men'] or count_women > vals['total_intern_women']:
                raise ValidationError("Số lượng nam/nữ ko phù hợp, có %d nam và %d nữ trong danh sách"%(count_man,count_women))
        return super(PhieuTraLoi,self).create(vals)

    @api.multi
    def write(self, vals):
        return super(PhieuTraLoi, self).write(vals)

    @api.onchange('interns','total_intern_men','total_intern_women')
    def _onchage_interns(self):

        count_man = 0
        count_women = 0
        for intern in self.interns:
            # _logger.info("intern.gender %s"%intern.gender)
            # ks = self.env['intern.internks'].browse(intern.internks_id)
            if intern.gender and intern.gender == 'nam':
                count_man += 1
            else:
                count_women += 1

        if count_man > self.total_intern_men or count_women > self.total_intern_women:
            raise Warning("Số lượng nam/nữ ko phù hợp, có %d nam và %d nữ trong danh sách" % (count_man, count_women))

    @api.multi
    @api.depends('interns','total_intern_men','total_intern_women')
    def _compute_len_interns(self):
        for rec in self:
            rec.len_interns_man = 0
            rec.len_interns_women = 0
            for intern in rec.interns:
                if intern.gender and intern.gender == 'nam':
                    rec.len_interns_man += 1
                else:
                    rec.len_interns_women += 1
            if rec.len_interns_man == rec.total_intern_men and rec.len_interns_women == rec.total_intern_women:
                rec.has_full = True
            else:
                rec.has_full = False


    len_interns_man = fields.Integer(compute=_compute_len_interns, store=True)
    len_interns_women = fields.Integer(compute=_compute_len_interns, store=True)
    has_full = fields.Boolean(compute=_compute_len_interns, store=True)
