angular.module('gosaccoApp')
   .controller('SharepurchaseCtrl', ['$scope','$resource','Member','ShareType','SharePurchase', function($scope,$resource, Member, ShareType,SharePurchase){
   	   var vm =  this;
   	   vm.sharepurchase = {};
   	   $scope.members = Member.query();
        $scope.sharetypes = ShareType.query();

        $scope.sharePurchase = function(purchase){
            alert(angular.toJson(purchase));
            SharePurchase.save(purchase, function(result){
                alert(result);
            }, function(error){
               alert(angular.toJson(error));
            });
        }
   }]);
