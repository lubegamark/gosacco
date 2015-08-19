angular.module('gosaccoApp')
    .factory('auth',  ['$resource','SERVER', function($resource, SERVER){
        function add_auth_header(data, headersGetter){

            var headers = headersGetter();
            headers['Authorization'] = ('Basic ' + btoa(data.username +
                                        ':' + data.password));
        }


        return {
            auth: $resource(SERVER.url+'/api-auth/login\\/', {}, {
                login: {method: 'POST', transformRequest: add_auth_header},
                logout: {method: 'DELETE'}
            }),
            users: $resource(SERVER.url+'/api/users\\/', {}, {
                create: {method: 'POST'}
            })
        }
    }]);