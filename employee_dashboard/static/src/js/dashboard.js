/**@odoo-module **/
import { registry } from "@web/core/registry";
import { Component } from  "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { session } from "@web/session";

const actionRegistry = registry.category("actions");
var uid = session.uid
class EmployeeDashboard extends Component {
    setup() {
         super.setup()
         this.orm = useService('orm')
         this._fetch_data()
         this.action = useService("action")
         this.orm = useService("orm")
   }
   _fetch_data(){
        this.orm.call("hr.employee", "get_tiles_data", [], {}).then(function(result){
           $('#employee').append('<span>' + result.total_attendance + '</span>');
           $('#leaves').append('<span>' + result.total_leave + '</span>');
           $('#project').append('<span>' + result.total_project + '</span>');
           $('#information').append('<span>' + result.employee_info.name + '</span>',
            '<ul>','<li style="font-size: 12px;">'+ 'Job Position: ' + result.employee_info.position + '</li>',
                   '<li style="font-size: 12px;">'+ 'Department: ' + result.employee_info.department + '</li>',
                   '<li style="font-size: 12px;">'+ 'Experience: ' + result.employee_info.experience + ' years' + '</li>',
            '</ul>');
           });
       };
   attendanceTileClick(){
        this.action.doAction({
                type: 'ir.actions.act_window',
                res_model: 'hr.attendance',
                domain: [["employee_id.user_id", "=", uid]],
                views: [[false, 'list'], [false, 'form']],
                target: 'current',
            })
   }
   leaveTileClick(){
        this.action.doAction({
                type: 'ir.actions.act_window',
                res_model: 'hr.leave',
                domain: [["employee_id.user_id", "=", uid]],
                views: [[false, 'list'], [false, 'form']],
                target: 'current',
            })
   }
   projectTileClick(){
        this.action.doAction({
                type: 'ir.actions.act_window',
                res_model: 'project.project',
                domain: [["user_id", "=", uid]],
                views: [[false, 'list'], [false, 'form']],
                target: 'current',
            })
   }
   personalInfoTileClick(){
        var action_employee = this.action
        var employee_id = this.orm.search("hr.employee", [["user_id", "=", uid]]);
        this.orm.call("hr.employee", "get_tiles_data", [], {}).then(function(result){
            var eid = result.employee_info['id']
            action_employee.doAction({
                type: 'ir.actions.act_window',
                res_model: 'hr.employee',
                res_id: eid,
                views: [[false, "form"]],
                target: 'current',
            })
        })
   }
}
EmployeeDashboard.template = "employee_dashboard.EmployeeDashboard";
actionRegistry.add("employee_dashboard_tag", EmployeeDashboard);
