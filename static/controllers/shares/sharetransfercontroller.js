angular.module('gosaccoApp')
   .controller('SharetransferCtrl', ['$scope', function($scope){
   	  var vm =this;
   	  vm.sharetransfer = {};
   	  vm.sharetransferFields = [
   	  {
            key: 'seller',
            type: 'select',
            templateOptions: {
                label: 'Seller',
                options:[
                {name:"Buhiire Keneth", value:"Buhiire Keneth"},
                {name:"Semakula Kraiba", value:"Semakula Kraiba"},
                {name:"Lubega Mark", value:"Lubega Mark"},
                {name:"Ricardo Mandela", value:"Ricardo Mark"}],
                required: true
            }
        },
        {
            key: 'buyer',
            type: 'select',
            templateOptions: {
                label: 'Buyer',
                options:[
                {name:"Buhiire Keneth", value:"Buhiire Keneth"},
                {name:"Semakula Kraiba", value:"Semakula Kraiba"},
                {name:"Lubega Mark", value:"Lubega Mark"},
                {name:"Ricardo Mandela", value:"Ricardo Mark"}],
                required: true
            }
        },
        {
            key: 'share_type',
            type: 'select',
            templateOptions: {
                label: 'Share Type',
                options:[
                {name:"Bonds", value:"Bonds"},
                {name:"Partnership", value:"Partnership"},
                {name:"Equity", value:"Equity"},],
                required: true
            }
        },
        {
            key: 'number_of_shares',
            type: 'input',
            templateOptions: {
            	type:'text',
                label: 'Number Of Shares',
                required: true
            }
        },
        {
            key: 'date',
            type: 'input',
            templateOptions: {
            	type:'date',
                label: 'Date',
                required: true
            }
        },];
   }]);