angular.module('gosaccoApp')
   .controller('SharepurchaseCtrl', ['$scope','Member', function($scope, Member){
   	   var vm =  this;
   	   vm.sharepurchase = {};
   	   vm.sharepurchaseFields = [{
            key: 'member',
            type: 'select',
            templateOptions: {
                label: 'Member',
                options:Member.query(),
                valueProp:'id',
                labelProp:'{user.username}',
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
        },];
   }]);