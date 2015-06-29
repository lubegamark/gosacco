angular.module('gosaccoApp')
   .controller('SecurityCtrl', ['$scope', function($scope){
   	  var vm = this;
   	  vm.securities = {};
   	  vm.securityFields = [
   	  {
            key:'security_type',
            type:'select',
            templateOptions:{
              label:'Security Type',
              options:[
                {name:"Buhiire Keneth", value:"Buhiire Keneth"},
                {name:"Semakula Kraiba", value:"Semakula Kraiba"},
                {name:"Lubega Mark", value:"Lubega Mark"},
                {name:"Ricardo Mandela", value:"Ricardo Mark"}],
              required:true
            }
       },
   	   {
            key: 'attached_to_loan',
            type: 'input',
            templateOptions: {
            	type:'text',
                label: 'Attached To Loan',
                required: true
            }
        },];
   }]);