angular.module('gosaccoApp')
   .controller('SharetypeCtrl', ['$scope', function($scope){
   	 var vm = this;
   	 vm.sharetype = {};
   	 vm.sharetypeFields = [
   	 {
            key: 'share_class',
            type: 'input',
            templateOptions: {
            	type:'text',
                label: 'Share Class',
                required: true
            }
        },
        {
            key: 'share_price',
            type: 'input',
            templateOptions: {
            	type:'text',
                label: 'Share Price',
                required: true
            }
        },
        {
            key: 'minimum_shares',
            type: 'input',
            templateOptions: {
            	type:'text',
                label: 'Minimum Shares',
                required: true
            }
        },
        {
            key: 'maximum_shares',
            type: 'input',
            templateOptions: {
            	type:'text',
                label: 'Maximum Shares',
                required: true
            }
        },];
   }]);