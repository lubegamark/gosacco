angular.module('gosaccoApp')
   .controller('ShareCtrl', ['$scope','Member','$http', function($scope, Member, $http){
   	$scope.members = Member.query();
       var url = "http://localhost:8000";
   	function loadShares(id){
            $http.get(url+'/api/shares/'+id).success(function(res){
                $scope.share = res;

            });
        }
       loadShares(1);
   }]);