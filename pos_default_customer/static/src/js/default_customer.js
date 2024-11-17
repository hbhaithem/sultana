/** @odoo-module **/
import { PosOrder } from "@point_of_sale/app/models/pos_order";
import {patch} from "@web/core/utils/patch";

patch(PosOrder.prototype, {

    setup() {
        super.setup(...arguments);
        debugger;
        if (this.config.default_partner_id) {
            this.set_partner(this.config.default_partner_id);
        }
    },
});
