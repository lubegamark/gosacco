angular.module('gosaccoApp')
.controller('authCtrl', function($scope, auth) {
        // Angular does not detect auto-fill or auto-complete. If the browser
        // autofills "username", Angular will be unaware of this and think
        // the $scope.username is blank. To workaround this we use the
        // autofill-event polyfill [4][5]
        $scope.login=true;


        $scope.getCredentials = function(){
            return {username: $scope.username, password: $scope.password};
        };

        $scope.login = function(){
            auth.auth.login($scope.getCredentials()).
                $promise.
                    then(function(data){
                        // on good username and password
                        $scope.user = data.username;
                    }).
                    catch(function(data){
                        // on incorrect username and password
                        alert(angular.toJson(data));
                    });
        };

        $scope.logout = function(){
            auth.auth.logout(function(){
                $scope.user = undefined;
            });
        };
        $scope.register = function($event){
            // prevent login form from firing
            $event.preventDefault();
            // create user and immediatly login on success
            auth.users.create($scope.getCredentials()).
                $promise.
                    then($scope.login).
                    catch(function(data){
                        alert(data.data.username);
                    });
            };
    });