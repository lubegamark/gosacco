angular.module('gosaccoApp')
   .controller('ShareCtrl', ['$scope','Share','$http', function($scope, Share, $http){
   	$scope.shares = Share.query();
   }]);
