/**
 * Created by leona on 7/4/15.
 */
angular.module('gosaccoApp')
   .controller('ListSavingsCtrl', ['$scope','Saving','Member',function($scope, Saving, Member){
        $scope.savings = Saving.query();

        // $scope.get_member = function(id){
        // 	return Member.
        // }
        console.log($scope.savings)
    }]);