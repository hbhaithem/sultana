########################################################################################################################
########################################################################################################################

    Set up the company:
        1- currency DZD
        2- Name
        3- logo

########################################################################################################################
########################################################################################################################

Uninstall modules:

1- spreadsheet_dashboard
2- pos_epson_printer

########################################################################################################################
########################################################################################################################
Configuration:

General Settings:
    1- Emails: set "Digest Email" as False
    2- Disable "Send SMS"
    3- Disable "Partner Autocomplete"
    4- Disable "Password Reset"
    5- Disable "Show Effect"
    6- Disable "Unsplash Image Library"

Purchase:
    1- disable "Receipt Reminder"
    2- disable "Product Variants"

Inventory:
    1- disable "SMS Confirmation"

Invoicing:
    1- Set "Fiscal Localization"
    2- Empty Taxes
    4- Disable "Snailmail"
    5- Disable "Total amount of invoice in letters"
    6- Disable "Taxes in company currency"
    6- Disable "Invoice Online Payment"

POS:
    1- remove all payment methods except cash
    2- check "Display Stock in POS" and "Restrict Product Out of Stock in POS"
    3- remove taxes
    4- set "Inventory Management" as "In real time (accurate but slower)"
    5- delete payment methods

    Set up categories:
        1- Product Categories (Cost FIFO)

########################################################################################################################
########################################################################################################################

Set default user groups for future users creation:

Point of Sale: User

Purchase: User

User Preferences:
    - Notification: check "Handle in Odoo"

########################################################################################################################
########################################################################################################################

Set partner email for new users

########################################################################################################################
########################################################################################################################

Archive all Taxes

########################################################################################################################
########################################################################################################################

Add default customer to POS

########################################################################################################################
########################################################################################################################

configure , in floats from lang
