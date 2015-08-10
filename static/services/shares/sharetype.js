angular.module('gosaccoApp')
   .factory('ShareType', ['$resource','SERVER', function($resource, SERVER){
   	// var url = 'http://localhost:8000';
   	return $resource(SERVER.url+'/api/shares/sharetype/');
   }]);