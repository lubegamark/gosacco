angular.module('gosaccoApp')
   .controller('MemberCtrl', ['$scope','Member', function($scope, Member){
   	$scope.members = Member.query();
   }]);