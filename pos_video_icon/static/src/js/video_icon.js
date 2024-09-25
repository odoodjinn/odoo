/**@odoo-module **/
import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
import { patch } from "@web/core/utils/patch";
import { ConfirmPopup } from "@point_of_sale/app/utils/confirm_popup/confirm_popup";
import { AbstractAwaitablePopup } from "@point_of_sale/app/popup/abstract_awaitable_popup";

export class VideoPopup extends AbstractAwaitablePopup {
   static template = "pos_product_video.VideoPopup";
   static defaultProps = {
       closePopup: ("Cancel"),
   };
}

patch(ProductCard.prototype, {
    videoPreview(e){
    e.stopPropagation();
    if(this.props.video_url){
        var url = this.props.video_url
        this.env.services.popup.add(VideoPopup, {
        title: 'Video Preview',
        body: url
        })
        }
    }
});
