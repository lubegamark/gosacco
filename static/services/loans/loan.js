angular.module('gosaccoApp')
   .factory('Loan', ['$resource','SERVER', function($resource, SERVER){
    // var url = "http://localhost:8000";
    return $resource(SERVER.url+'/api/loans/loanlist');
   }])
