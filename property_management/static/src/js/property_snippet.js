/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";
import { renderToElement } from "@web/core/utils/render";

//export function _chunk(array, size) {
//    const result = [];
//    for (let i = 0; i < array.length; i += size) {
//        result.push(array.slice(i, i + size));
//    }
//    return result;
//}
//var TopSellingProperties = PublicWidget.Widget.extend({
//        selector: '.dynamic_snippet',
//        willStart: async function () {
//            const data = await jsonrpc('/top_properties', {})
//            const property_data_list = data
//            Object.assign(this, {
//                property_data_list
//            })
//        },
//        start: function () {
//            const refEl = this.$el.find("#top_properties")
//            const { property_data_list} = this
//            const chunkData = chunk(property_data_list, 4)
//            refEl.html(renderToElement('property_management.property_snippet_carousel', {
//                property_data_list,
//                chunkData
//            }))
//        }
//    });
//PublicWidget.registry.property_list_snippet = TopSellingProperties;
//return TopSellingProperties;

publicWidget.registry.DynamicSnippet = publicWidget.Widget.extend({
   selector: '.dynamic_snippet',
   start: function () {
       const refEl = this.$el.find("#top_properties")
       var self = this;
//       var data = jsonrpc('/top_properties', {}).then((data) => {
//           self.$target.empty().append(data)
//       });
       const chunkData = chunk(property_data_list, 4)
        refEl.html(renderToElement('property_management.property_snippet_carousel', {
            property_data_list,
            chunkData
            }))
   }
});

export default publicWidget.registry.DynamicSnippet;
