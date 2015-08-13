angular.module('gosaccoApp')
   .factory('Saving', ['$resource','SERVER', function($resource, SERVER){
   	// var url = "http://localhost:8000";
   	return $resource(SERVER.url+"/api/savings/savingslist");
   }])
   .factory('Deposit', ['$resource','SERVER', function($resource, SERVER){
   	// var url = "http://localhost:8000";XSD
   	return $resource(SERVER.url+"/api/savings/savingscreate");
   }]);
