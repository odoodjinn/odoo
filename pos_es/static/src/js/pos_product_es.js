/** @odoo-module */
import { patch } from "@web/core/utils/patch";

odoo.define('pos_es.product_name_es', function(require){
    'use strict';
    const models = require('point_of_sale.models');
    models.load_fields('product.product', ['product_name_es']);
    const OrderLine = models.Orderline.prototype;
    models.OrderLine = models.Orderline.extend({
        get_product_translated_name: function(){
        return this.product.product_name_es || this.product.display_name;
        }
    });
});