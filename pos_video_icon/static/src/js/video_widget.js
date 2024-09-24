/**@odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { patch } from "@web/core/utils/patch";

patch(ProductScreen.prototype, {
static template
    videoPreview(){
        return console.log('hii');
    }
});




//odoo.define('your_module.ProductVideo', function (require) {
//'use strict'; const ProductItem = require('point_of_sale.ProductItem');
//const ProductItemVideo = ProductItem => class extends ProductItem {
//constructor() {
//super(...arguments); }
//// You can extend the render method to add click functionality
//renderElement() {
//super.renderElement();
//const videoUrl = this.product.video_url;
//if (videoUrl) {
//this.el.querySelector('.video-icon').addEventListener('click', () => { window.open(videoUrl, '_blank');
//});
//}
//}
//};
//return ProductItemVideo;
//});
