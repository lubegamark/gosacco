angular.module('gosaccoApp')
   .factory('Share', ['$resource','SERVER', function($resource, SERVER){
   	 // var url ="http://localhost:8000";
   	 return $resource(SERVER.url+'/api/shares/sharelist');
   }])
    .factory('SharePurchase',['$resource','SERVER', function($resource, SERVER){
       return $resource(SERVER.url+'/api/shares/sharepurchase/');
    }]);
