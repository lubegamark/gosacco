angular.module('gosaccoApp')
   .controller('SecurityArticleCtrl', ['$scope', function($scope){
   	  var vm = this;
   	  vm.securityarticle = {};
   	  vm.securityarticleFields = [
   	  {
            key:'name',
            type:'input',
            templateOptions:{
              type:'text',
              label:'Name',
              required:true
            }
       },
   	   {
            key: 'type',
            type: 'input',
            templateOptions: {
            	type:'text',
                label: 'Type',
                required: true
            }
        },
        {
            key:'identification_type',
            type:'input',
            templateOptions:{
              type:'text',
              label:'Identification Type',
              required:true
            }
       },
       {
            key: 'identification',
            type: 'input',
            templateOptions: {
              type:'text',
                label: 'Identification',
                required: true
            }
        },
        {
            key:'loan_owner',
            type:'select',
            templateOptions:{
              label:'Loan Owner',
              options:[
                {name:"Buhiire Keneth", value:"Buhiire Keneth"},
                {name:"Semakula Kraiba", value:"Semakula Kraiba"},
                {name:"Lubega Mark", value:"Lubega Mark"},
                {name:"Ricardo Mandela", value:"Ricardo Mark"}],
              required:true
            }
       },
       {
            key: 'description',
            type: 'textarea',
            templateOptions: {
                label: 'Description',
                required: true
            }
        },
        {
            key:'security',
            type:'select',
            templateOptions:{
              label:'Security',
              options:[
                {name:"House", value:"House"},
                {name:"Car", value:"Car"},
                {name:"Television Set", value:"Television Set"},
                {name:"Fridge", value:"Fridge"}],
              required:true
            }
       },];
   }]);