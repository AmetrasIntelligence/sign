# Copyright 2023 Dixmit
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Sign Oca",
    "summary": """
        Allow to sign documents inside Odoo CE""",
    "version": "16.0.2.1.4",
    "license": "AGPL-3",
    "author": "Dixmit,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/sign",
    "depends": ["web_editor", "portal", "base_sparse_field"],
    "data": [
        "security/security.xml",
        "views/menu.xml",
        "data/data.xml",
        "wizards/res_config_settings_views.xml",
        "wizards/sign_oca_template_generate.xml",
        "wizards/sign_oca_template_generate_multi.xml",
        "views/res_partner_views.xml",
        "views/sign_oca_request_log.xml",
        "views/sign_oca_request.xml",
        "security/ir.model.access.csv",
        "views/sign_oca_field.xml",
        "views/sign_oca_role.xml",
        "views/sign_oca_template.xml",
        "templates/assets.xml",
    ],
    "demo": [
        "demo/sign_oca_template.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "sign_oca/static/src/components/sign_oca_pdf_common/sign_oca_pdf_common.xml",
            "sign_oca/static/src/components/sign_oca_configure/sign_oca_configure.xml",
            "sign_oca/static/src/components/sign_oca_pdf/sign_oca_pdf.xml",
            "sign_oca/static/src/elements/elements.xml",
            "sign_oca/static/src/scss/sign_oca.scss",
            "sign_oca/static/src/components/sign_oca_pdf_common/sign_oca_pdf_common.esm.js",
            "sign_oca/static/src/components/sign_oca_configure/sign_oca_configure.esm.js",
            "sign_oca/static/src/elements/text.esm.js",
            "sign_oca/static/src/elements/signature.esm.js",
            "sign_oca/static/src/elements/check.esm.js",
            "sign_oca/static/src/components/sign_oca_pdf/sign_oca_pdf.esm.js",
            "sign_oca/static/src/components/sign_oca_pdf/sign_oca_pdf_action.esm.js",
            "sign_oca/static/src/components/"
            "sign_oca_pdf_common/sign_oca_pdf_common_action.esm.js",
            "sign_oca/static/src/js/*.js",
            "sign_oca/static/src/xml/*.xml",
        ],
        "web.assets_frontend": [
            "sign_oca/static/src/components/sign_oca_pdf_common/sign_oca_pdf_common.xml",
            "sign_oca/static/src/components/sign_oca_configure/sign_oca_configure.xml",
            "sign_oca/static/src/components/sign_oca_pdf/sign_oca_pdf.xml",
            "sign_oca/static/src/elements/elements.xml",
            "sign_oca/static/src/scss/sign_oca.scss",
            "sign_oca/static/src/components/sign_oca_pdf_common/sign_oca_pdf_common.esm.js",
            "sign_oca/static/src/elements/text.esm.js",
            "sign_oca/static/src/elements/signature.esm.js",
            "sign_oca/static/src/elements/check.esm.js",
            "sign_oca/static/src/components/sign_oca_pdf/sign_oca_pdf.esm.js",
            "sign_oca/static/src/components/sign_oca_pdf_portal/sign_oca_pdf_portal.esm.js",
            "sign_oca/static/src/components/sign_oca_pdf_portal/sign_oca_pdf_portal.xml",
            "sign_oca/static/src/scss/portal.scss",
            "sign_oca/static/src/js/*.js",
            "sign_oca/static/src/xml/*.xml",
        ],
        "sign_oca.sign_assets": [
            "sign_oca/static/src/scss/sign.scss",
            "web/static/src/libs/fontawesome/css/font-awesome.css",
        ],
    },
    "maintainers": ["etobella"],
}
