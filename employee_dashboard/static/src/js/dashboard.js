/**@odoo-module **/
import { registry } from "@web/core/registry";
import { Component } from  "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

const actionRegistry = registry.category("actions");
class EmployeeDashboard extends Component {
    setup() {
         super.setup()
         this.orm = useService('orm')
         this._fetch_data()
   }
   _fetch_data(){
   var self = this;
  this.orm.call("hr.employee", "get_tiles_data", [], {}).then(function(result){
           $('#employee').append('<span>' + result.total_employee + '</span>');
//           $('#my_opportunity').append('<span>' + result.total_opportunity + '</span>');
//           $('#revenue').append('<span>' + result.currency + result.expected_revenue + '</span>');
//           console.log(result, '//result')
           });
       };
}
EmployeeDashboard.template = "employee_dashboard.EmployeeDashboard";
actionRegistry.add("employee_dashboard_tag", EmployeeDashboard);
