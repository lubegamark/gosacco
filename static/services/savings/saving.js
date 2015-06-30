angular.module('gosaccoApp')
   .factory('Saving', ['$resource', function($resource){
   	var url = "http:localhost:8000";
   	return $resource(url+"/api/savings/");
   }]);