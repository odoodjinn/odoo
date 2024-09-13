/** @odoo-module **/
import { renderToElement } from "@web/core/utils/render";
import { jsonrpc } from "@web/core/network/rpc_service";

$(".custom_create").click(function(){
    var order_line_list = [];
    var rows = $('.order_line_table > tbody > tr.order_line');
    var tenant_id = $('#tenant_id').val();
    var due_date = $('#due_date').val();
    var company_id = $('#company_id').val();
    var type = $('#type').val();
    $.each(rows, function(row) {
        let property_id = $(this).find('select[name="property_id"]').val();
        let start_date = $(this).find('input[name="start_date"]').val();
        let end_date = $(this).find('input[name="end_date"]').val();
        order_line_list.push({
            'property_id': property_id,
            'start_date': start_date,
            'end_date': end_date,
        });
    });
    jsonrpc('/management/submit', {order_line_list, tenant_id, due_date, company_id, type}).then((res)=>{

    });
})
$("#add_line").click(function(){
    var $new_row = $('.add_extra_order_line').clone(true);
    $new_row.removeClass('d-none');
    $new_row.removeClass('add_extra_order_line');
    $new_row.addClass('order_line');
    $new_row.insertBefore($('.add_extra_order_line'));
})
$(".remove_line").click(function(){
    $(this).parent().parent().remove();
})
