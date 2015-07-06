/**
 * Created by leona on 7/4/15.
 */
angular.module('gosaccoApp')
    .controller('LoanListCtrl',['$scope','Member', function($scope, Member){
        $scope.members = Member.query();
    }]);