/**@odoo-module **/
import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
export class DeleteButton extends Component {
    static template = "point_of_sale.DeleteButton";
    /** Setup function to initialize the component.**/
    setup() {
        this.pos = usePos();
    }

    /**Click event handler for the create button.**/
    async onClick() {
        var order = this.pos.get_order();
        var lines = order.get_orderlines();
//        console.log( lines.filter(line => line.get_product()), 'lines filter')
        if (lines.length){
        lines.filter(line => line.get_product()).forEach(line => order.removeOrderline(line));
        }
    }
}

/**Add the DeleteButton component to the control buttons in the ProductScreen. **/
ProductScreen.addControlButton({
component: DeleteButton,
});
