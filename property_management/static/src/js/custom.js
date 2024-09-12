/** @odoo-module **/
import PublicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";
$(".custom_create").click(function(){
    order_line = [];
    rows = $('.order_line_table > tbody > tr.order_line');
    _.each(rows, function(row) {
    let property_id = $(row).find('select[name="property_id"]').val();
    let start_date = $(row).find('input[name="start_date"]').val();
    let end_date = $(row).find('input[name="end_date"]').val();
    console.log(property_id, start_date, end_date)
    order_line.push({
        'property': property_id,
        'start_date': start_date,
        'end_date': end_date,
    });
    });
    $('textarea[name="property_ids"]').val(JSON.stringify(order_line));
})
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
