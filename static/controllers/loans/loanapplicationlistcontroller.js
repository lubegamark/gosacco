angular.module('gosaccoApp')
   .controller('loanApplicationListCtrl', ['$scope','Loan', function($scope, Loan){
         $scope.loanapplications = Loan.query();
         console.log($scope.loanapplications);
   }]);
