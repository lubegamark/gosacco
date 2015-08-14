angular.module('gosaccoApp')
   .controller('DepositCtrl', ['$scope','Deposit', function($scope,Deposit){
   	  var vm = this;
 //  	  vm.deposit = {};

   	  $scope.addDeposit=function(deposit){
   	  Deposit.save(deposit,function(result){
   	    alert("result")
   	  },function(error){
   	    alert("error")

   	  });



   }


   }]);



