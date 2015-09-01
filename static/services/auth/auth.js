angular.module('gosaccoApp')
.factory('Auth',['$cookies','$http','SERVER', function($cookies, $http,SERVER){
  return {
   login: function(username, password){
     return $http.post(SERVER.url+'/api-auth/login/').success(function(data){
     console.log('logged in');
     });
   }
  };
}]);