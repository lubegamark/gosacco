angular.module('gosaccoApp')
   .factory('Share', ['$resource', function($resource){
   	 var url ="http://localhost:8000";
   	 return $resource(url+'/api/shares/:member_id');
   }]);