angular.module('gosaccoApp')
   .controller('SharetypeCtrl', ['$scope','$alert','ShareType', function($scope, $alert, ShareType){
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

    vm.addSharetype = function(){
        ShareType.save({
            share_class:vm.sharetype.share_class,
            share_price:vm.sharetype.share_price,
            minimum_shares:vm.sharetype.minimum_shares,
            maximum_shares:vm.sharetype.maximum_shares,
        }, function(){
            vm.sharetype.share_class='';
                vm.sharetype.share_price='';
                vm.sharetype.minimum_shares='';
                vm.sharetype.maximum_shares='';
                vm.sharetypeForm.$setPristine();
            $alert({
   	  			content:'New Sharetype has been added.',
   	  			placement:'top-right',
   	  			type:'success',
   	  			duration:3
   	  		});
        }, function(response){
            vm.sharetype.share_class='';
                vm.sharetype.share_price='';
                vm.sharetype.minimum_shares='';
                vm.sharetype.maximum_shares='';
                vm.sharetypeForm.$setPristine();
            $alert({
   	  			content:response.data.message,
   	  			placement:'top-right',
   	  			type:'danger',
   	  			duration:3
   	  		});
        });
    };
   }]);