/**@odoo-module*/
import { InputBox } from "./input_box"
import { patch } from "@web/core/utils/patch";
import { useState, useEffect, useRef } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";


patch(InputBox.prototype, {
    setup() {
        super.setup()
            this.InputClickMe = useRef("InputClickMe")
            this.orm = useService("orm")
            this.action = useService("action")
            this.state = useState({
            value: 0,
            next_val: 0
        })
        useEffect(
            (rec) => {
                this.state.next_val += rec
                console.log(rec, 'rec')
            },
            () => [this.state.value]
        )
    },
    demo(e){
        this.state.value += e
    },
    demofu(){
        console.log(this.InputClickMe.el.value)
    },
    async demofunc() {
        this.sale_order = await this.orm.searchRead("sale.order",[],['name'],{limit:5});
        console.log(this.sale_order,)
    },
    openSaleOrderFrom() {
        this.action.doAction({
            type: 'ir.actions.act_window',
            res_id: 5,
            res_model: 'sale.order',
            views: [[false, 'form']],
        })
        }
    });