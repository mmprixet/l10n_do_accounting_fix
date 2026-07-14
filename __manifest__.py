{
    "name": "L10n DO Accounting - Fix Document Number Store",
    "version": "17.0.1.0.0",
    "summary": "Corrige el campo l10n_latam_document_number para que sea almacenado y buscable",
    "description": """
        Este módulo corrige un bug del módulo l10n_do_accounting (NETVUX),
        donde el campo l10n_latam_document_number queda registrado como
        store=False / searchable=False al combinarse con la definición
        original de Odoo (l10n_latam_invoice_document).

        Esto provoca que las búsquedas de duplicados de NCF (número de
        comprobante fiscal) no filtren correctamente, bloqueando facturas
        de proveedor válidas por falsos "duplicados".

        Este módulo no modifica ni una línea del código de NETVUX: solo
        hereda el modelo account.move y vuelve a declarar el campo con
        store=True, forzando a Odoo a crear la columna real en la base
        de datos y a indexarla para búsquedas.
    """,
    "author": "Interno - Tuamini",
    "category": "Accounting/Localizations",
    "depends": [
        "account",
        "l10n_latam_invoice_document",
        "l10n_do_accounting",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
}
