angular.module('gosaccoApp')
   .controller('SharepurchaseCtrl', ['$scope','Member','ShareType', function($scope, Member, ShareType){
   	   var vm =  this;
   	   vm.sharepurchase = {};
   	   vm.sharepurchaseFields = [{
            key: 'member',
            type: 'select',
            templateOptions: {
                label: 'Member',
                options:Member.query(),
                valueProp:'id',
                labelProp:'user',
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
                options:ShareType.query(),
                valueProp:'share_class',
                labelProp:'share_class',
                required: true
            }
        },];
   }]);