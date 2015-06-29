angular.module('gosaccoApp')
   .controller('LoanFormCtrl', ['$scope', function($scope){
   	   var vm = this;
   	   vm.loanform = {};
   	   vm.loanformFields = [
       {
            key:'application',
            type:'select',
            templateOptions:{
              label:'Application ',
              options:[
                {name:"Buhiire Keneth", value:"Buhiire Keneth"},
                {name:"Semakula Kraiba", value:"Semakula Kraiba"},
                {name:"Lubega Mark", value:"Lubega Mark"},
                {name:"Ricardo Mandela", value:"Ricardo Mark"}],
              required:true
            }
       },
   	   {
            key: 'member',
            type: 'select',
            templateOptions: {
                label: 'Member Name',
                options:[
                {name:"Buhiire Keneth", value:"Buhiire Keneth"},
                {name:"Semakula Kraiba", value:"Semakula Kraiba"},
                {name:"Lubega Mark", value:"Lubega Mark"},
                {name:"Ricardo Mandela", value:"Ricardo Mark"}],
                placeholder:"Select a member",
                required: true
            }
        },
      {
            key:'approval_date',
            type:'input',
            templateOptions:{
              type:'date',
              label:'Approval Date',
              required:true
            }
      },
      {
            key: 'amount',
            type: 'input',
            templateOptions: {
                type: 'text',
                label: 'Amount',
                required: true
            }
      },
      {
      key:'payment_period',
      type:'input',
      templateOptions:{
          type:'date',
          label:'Payment Period',
          required:true
      }
    },
   	  {
   	  	    key:'loan_type',
   	  	    type:'select',
   	  	    templateOptions:{
   	  	    	label:"Loan Type",
   	  	    	options:[{name:"Short Term", value:"Short Term"},
   	  	    	{name:" Medium Term", value:"Medium Term"},
   	  	    	{name:"Long Term", value:"Long Term Term"}],
   	  	    	placeholder:"Select Loan Type",
   	  	    	required:true
   	  	    }
   	  },
      {
         key:'security_details',
         type:'textarea',
         templateOptions:{
          label:'Security Details',
          required:true
         }
      },
      {
         key:'security',
         type:'textarea',
         templateOptions:{
          label:'Security',
          required:true
         }
      },
      {
          key:'guarantors',
          type:'textarea',
          templateOptions:{
            label:'Guarantors',
            required:true
          }
      }
      ];
   }]);