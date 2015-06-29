angular.module('gosaccoApp')
   .factory('Member', ['$resource', function($resource){
   	var url = "http://localhost:8000";
   	return $resource(url+'/api/members');
   }])