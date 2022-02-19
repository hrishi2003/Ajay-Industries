// Copyright (c) 2022, aj.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Income Account Mapping', {
	refresh: function(frm) {
		set_filters(frm);
		}
	});
	
	function set_filters(frm){
	  frm.set_query('income_account', () => {
		return{
		  filters: {
			is_group: 0,
			account_type: 'Income Account'
		  }
		}
	  });
	}