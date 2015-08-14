angular.module('gosaccoApp')
   .factory('SavingsType', ['$resource','SERVER', function($resource, SERVER){
    // var url = "http://localhost:8000";
    return $resource(SERVER.url+"/api/savings/savingstypelist/");
   }]);
