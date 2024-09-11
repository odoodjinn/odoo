/** @odoo-module **/
import PublicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";
$("#add_line").click(function(){
    console.log('add line');
    var $new_row = $('.add_extra_order_line').clone(true);
    $new_row.removeClass('d-none');
    $new_row.removeClass('add_extra_order_line');
    $new_row.addClass('order_line');
    $new_row.insertBefore($('.add_extra_order_line'));
})
$(".remove_line").click(function(){
    console.log('remove line');
    $(this).parent().parent().remove();
})

