angular.module('gosaccoApp')
   .factory('ShareType', ['$resource', function($resource){
   	var url = 'http://localhost:8000';
   	return $resource(url+'/api/shares/sharetype/');
   }]);