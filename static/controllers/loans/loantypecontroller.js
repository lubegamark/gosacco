angular.module('gosaccoApp')
   .controller('LoanTypeCtrl', ['$scope', function($scope){
   	  var vm = this;
   	  vm.loantype = {};
   	  vm.loantypeFields =[
   	  {
            key:'loan_name',
            type:'input',
            templateOptions:{
              type:'text',
              label:'Loan Name',
              required:true
            }
       },
       {
            key:'interest',
            type:'input',
            templateOptions:{
              type:'text',
              label:'Interest',
              required:true
            }
       },
   	   {
            key: 'interest_period',
            type: 'select',
            templateOptions: {
                label: 'Interest Period',
                options:[
                {name:"Per Annum", value:"Per Annum"},
                {name:"Per Month", value:"Per Month"},
                {name:"Per Day", value:"Per Day"},
                ],
                placeholder:"Select an interest period",
                required: true
            }
        },
      {
            key:'processing_period',
            type:'input',
            templateOptions:{
              type:'text',
              label:'Processing Period',
              required:true
            }
      },
      {
            key: 'minimum_amount',
            type: 'input',
            templateOptions: {
                type: 'text',
                label: 'Minimum Amount',
                required: true
            }
      },
      {
      key:'minimum_membership',
      type:'input',
      templateOptions:{
          type:'text',
          label:'Minimum Membership Period',
          required:true
      }
    },   	  
      {
         key:'minimum_shares',
         type:'input',
         templateOptions:{
          type:'text',
          label:'Minimum Shares',
          required:true
         }
      },
      {
         key:'minimum_savings',
         type:'input',
         templateOptions:{
          type:'text',
          label:'Minimum Savings',
          required:true
         }
      },
   	  ];
   }]);