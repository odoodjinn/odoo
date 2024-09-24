/**@odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Component } from "@odoo/owl";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
import { patch } from "@web/core/utils/patch";
patch(Orderline.prototype, {
    removeLine() {
        var pos_order = this.env.services.pos.get_order();
        var orderline = pos_order.orderlines.find((line) => line.full_product_name == this.props.line.productName);
        return pos_order.removeOrderline(orderline);
    }
});

class DeleteButton extends Component {
    static template = "point_of_sale.DeleteButton";
    removeOrder() {
        var order = this.env.services.pos.get_order();
        var lines = order.get_orderlines();
        if (lines.length){
        lines.filter(line => line.get_product()).forEach(line => order.removeOrderline(line));
        }
    }
}

ProductScreen.addControlButton({
component: DeleteButton,
});
