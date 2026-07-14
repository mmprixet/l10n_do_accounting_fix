# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountMove(models.Model):
    _inherit = "account.move"

    # Fix: el módulo l10n_do_accounting (NETVUX) redefine este campo sin
    # store=True, lo que hace que la búsqueda de duplicados de NCF
    # (l10n_latam_document_number) no filtre correctamente y bloquee
    # facturas de proveedor válidas.
    #
    # Esta redeclaración no cambia ningún comportamiento visual ni de
    # negocio: solo obliga a Odoo a almacenar el campo en una columna
    # real de la base de datos y a hacerlo buscable/indexable.
    l10n_latam_document_number = fields.Char(
        string="Document Number",
        copy=False,
        readonly=False,
        store=True,
        index=True,
    )
